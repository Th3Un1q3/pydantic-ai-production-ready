#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any, cast

DEFAULT_LOGS_ROOT = Path("/workspace/logs/copilot")
DEFAULT_VSCODE_WORKSPACE_STORAGE_ROOT = Path(
    "/home/vscode/.vscode-server/data/User/workspaceStorage"
)
USER_MESSAGE_PREVIEW_MAX_LEN = 120
USER_MESSAGE_PREVIEW_ITEM_MAX_LEN = 36
USER_MESSAGE_PREVIEW_RECENT_COUNT = 3
USER_MESSAGE_PREVIEW_SEPARATOR = " | "
MAX_STORED_USER_MESSAGES = 12


@dataclass
class TimeRange:
    from_dt: datetime
    to_dt: datetime


def parse_iso_datetime(value: str) -> datetime:
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"

    try:
        dt = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid ISO datetime: {value}") from exc

    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)


def parse_duration(value: str) -> timedelta:
    match = re.fullmatch(r"(?i)\s*(\d+)\s*([dhm])\s*", value)
    if not match:
        raise argparse.ArgumentTypeError("Invalid duration. Use forms like 7d, 24h, 30m.")

    amount = int(match.group(1))
    unit = match.group(2).lower()

    if unit == "d":
        return timedelta(days=amount)
    if unit == "h":
        return timedelta(hours=amount)
    return timedelta(minutes=amount)


def parse_json_stream_objects(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8", errors="replace")
    decoder = json.JSONDecoder()
    results: list[dict[str, Any]] = []
    idx = 0
    size = len(text)

    while idx < size:
        start = text.find("{", idx)
        if start == -1:
            break

        try:
            value, end = decoder.raw_decode(text, start)
        except json.JSONDecodeError:
            idx = start + 1
            continue

        if isinstance(value, dict):
            results.append(value)
        idx = end

    return results


def parse_ndjson(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    if not path.exists():
        return events

    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                events.append(value)
    return events


def parse_ndjson_with_warnings(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    warnings: list[str] = []
    malformed_count = 0
    non_object_count = 0

    if not path.exists():
        warnings.append(f"Transcript file not found: {path}")
        return events, warnings

    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    value = json.loads(stripped)
                except json.JSONDecodeError:
                    malformed_count += 1
                    continue
                if isinstance(value, dict):
                    events.append(value)
                else:
                    non_object_count += 1
    except OSError as exc:
        warnings.append(f"Unable to read transcript file: {path} ({exc})")
        return events, warnings

    if malformed_count:
        warnings.append(f"Skipped {malformed_count} malformed transcript line(s).")
    if non_object_count:
        warnings.append(f"Skipped {non_object_count} non-object transcript line(s).")

    return events, warnings


def iso_or_none(value: datetime | None) -> str | None:
    if value is None:
        return None
    return value.astimezone(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _normalize_timestamp_value(raw: Any) -> datetime | None:
    if isinstance(raw, str):
        try:
            return parse_iso_datetime(raw)
        except argparse.ArgumentTypeError:
            return None

    if isinstance(raw, bool):
        return None

    if isinstance(raw, (int, float)):
        seconds = float(raw)
        if abs(seconds) > 1e12:
            seconds /= 1000.0
        try:
            return datetime.fromtimestamp(seconds, tz=UTC)
        except (OverflowError, OSError, ValueError):
            return None

    return None


def extract_timestamp(event: dict[str, Any]) -> datetime | None:
    for key in ("timestamp", "time", "start_time", "startTime", "end_time", "endTime"):
        raw = event.get(key)
        parsed = _normalize_timestamp_value(raw)
        if parsed is not None:
            return parsed

    payload = event.get("payload")
    if isinstance(payload, dict):
        raw = payload.get("timestamp")
        parsed = _normalize_timestamp_value(raw)
        if parsed is not None:
            return parsed

    return None


def extract_session_id(event: dict[str, Any], fallback: str | None = None) -> str | None:
    for key in ("sessionId", "session_id", "id"):
        value = event.get(key)
        if isinstance(value, str) and value:
            return value

    payload = event.get("payload")
    if isinstance(payload, dict):
        for key in ("sessionId", "session_id", "id"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return value

    return fallback


def _take_model(event: dict[str, Any]) -> str | None:
    for key in ("model", "modelName", "model_name"):
        value = event.get(key)
        if isinstance(value, str) and value:
            return value

    payload = event.get("payload")
    if isinstance(payload, dict):
        for key in ("model", "modelName", "model_name"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return value
    return None


def _take_transcript_path(event: dict[str, Any]) -> str | None:
    for key in ("transcript_path", "transcriptPath"):
        value = event.get(key)
        if isinstance(value, str) and value:
            return value

    payload = event.get("payload")
    if isinstance(payload, dict):
        for key in ("transcript_path", "transcriptPath"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return value
    return None


def _normalize_whitespace(value: str) -> str:
    return " ".join(value.split())


def _truncate_preview(value: str, limit: int = USER_MESSAGE_PREVIEW_MAX_LEN) -> str:
    normalized = _normalize_whitespace(value)
    if len(normalized) <= limit:
        return normalized
    if limit <= 1:
        return normalized[:limit]
    return normalized[: limit - 1] + "…"


def _extract_user_message_text(event: dict[str, Any]) -> str | None:
    payload = event.get("payload")
    if isinstance(payload, dict):
        payload_prompt = payload.get("prompt")
        if isinstance(payload_prompt, str) and payload_prompt.strip():
            return payload_prompt

    for key in ("text", "content", "message"):
        value = event.get(key)
        if isinstance(value, str) and value.strip():
            return value

    if isinstance(payload, dict):
        for key in ("text", "content", "message"):
            value = payload.get(key)
            if isinstance(value, str) and value.strip():
                return value

    return None


def _coerce_user_messages(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item.strip()]


def _build_user_message_preview(record: dict[str, Any]) -> str:
    user_messages = _coerce_user_messages(record.get("user_messages"))
    if not user_messages:
        return _truncate_preview(str(record.get("last_user_message") or ""))

    recent_messages = user_messages[-USER_MESSAGE_PREVIEW_RECENT_COUNT:]
    compact_items = [
        _truncate_preview(message, USER_MESSAGE_PREVIEW_ITEM_MAX_LEN) for message in recent_messages
    ]
    combined = USER_MESSAGE_PREVIEW_SEPARATOR.join(compact_items)
    return _truncate_preview(combined, USER_MESSAGE_PREVIEW_MAX_LEN)


def _ensure_record(store: dict[str, dict[str, Any]], session_id: str) -> dict[str, Any]:
    if session_id not in store:
        store[session_id] = {
            "session_id": session_id,
            "start_time": None,
            "end_time": None,
            "model": None,
            "transcript_path": None,
            "transcript_ref_status": "missing",
            "prompt_count": 0,
            "last_user_message": None,
            "user_messages": [],
        }
    return store[session_id]


def update_record_from_event(record: dict[str, Any], event: dict[str, Any]) -> None:
    timestamp = extract_timestamp(event)
    if timestamp is not None:
        if record["start_time"] is None or timestamp < record["start_time"]:
            record["start_time"] = timestamp
        if record["end_time"] is None or timestamp > record["end_time"]:
            record["end_time"] = timestamp

    model = _take_model(event)
    if model and not record.get("model"):
        record["model"] = model

    transcript_path = _take_transcript_path(event)
    if transcript_path and not record.get("transcript_path"):
        record["transcript_path"] = transcript_path
        record["transcript_ref_status"] = "provided"

    event_name = event.get("event")
    payload = event.get("payload")
    payload_prompt = payload.get("prompt") if isinstance(payload, dict) else None
    if event_name == "userMessage" or isinstance(payload_prompt, str):
        record["prompt_count"] = int(record.get("prompt_count") or 0) + 1
        user_message_text = _extract_user_message_text(event)
        if user_message_text is not None:
            record["last_user_message"] = user_message_text
            user_messages = _coerce_user_messages(record.get("user_messages"))
            user_messages.append(user_message_text)
            if len(user_messages) > MAX_STORED_USER_MESSAGES:
                user_messages = user_messages[-MAX_STORED_USER_MESSAGES:]
            record["user_messages"] = user_messages


def load_index_sessions(logs_root: Path) -> dict[str, dict[str, Any]]:
    index_path = logs_root / "session.log"
    objects = parse_json_stream_objects(index_path)

    sessions: dict[str, dict[str, Any]] = {}
    for obj in objects:
        session_id = extract_session_id(obj)
        if not session_id:
            continue
        record = _ensure_record(sessions, session_id)
        update_record_from_event(record, obj)

    return sessions


def infer_session_from_file(session_file: Path) -> dict[str, Any]:
    session_id = session_file.stem
    record: dict[str, Any] = {
        "session_id": session_id,
        "start_time": None,
        "end_time": None,
        "model": None,
        "transcript_path": None,
        "transcript_ref_status": "missing",
        "prompt_count": 0,
        "last_user_message": None,
        "user_messages": [],
    }

    for event in parse_ndjson(session_file):
        update_record_from_event(record, event)

    if record["start_time"] is None or record["end_time"] is None:
        modified_at = datetime.fromtimestamp(session_file.stat().st_mtime, tz=UTC)
        if record["start_time"] is None:
            record["start_time"] = modified_at
        if record["end_time"] is None:
            record["end_time"] = modified_at

    return record


def merge_fallback_sessions(logs_root: Path, sessions: dict[str, dict[str, Any]]) -> None:
    sessions_dir = logs_root / "sessions"
    if not sessions_dir.exists():
        return

    for session_file in sorted(sessions_dir.glob("*.ndjson")):
        session_id = session_file.stem
        fallback_record = infer_session_from_file(session_file)

        existing = sessions.get(session_id)
        if existing is None:
            fallback_record["transcript_ref_status"] = (
                "discovered" if fallback_record.get("transcript_path") else "missing"
            )
            sessions[session_id] = fallback_record
            continue

        for key in ("start_time", "end_time", "model", "transcript_path"):
            if existing.get(key) is None and fallback_record.get(key) is not None:
                existing[key] = fallback_record[key]

        if existing.get("transcript_path") and existing.get("transcript_ref_status") != "provided":
            existing["transcript_ref_status"] = "discovered"
        elif not existing.get("transcript_path"):
            existing["transcript_ref_status"] = "missing"

        existing_prompts = int(existing.get("prompt_count") or 0)
        fallback_prompts = int(fallback_record.get("prompt_count") or 0)
        if fallback_prompts > existing_prompts:
            existing["prompt_count"] = fallback_prompts

        existing_messages = _coerce_user_messages(existing.get("user_messages"))
        fallback_messages = _coerce_user_messages(fallback_record.get("user_messages"))
        if fallback_messages:
            merged_messages = existing_messages + [
                message for message in fallback_messages if message not in existing_messages
            ]
            if len(merged_messages) > MAX_STORED_USER_MESSAGES:
                merged_messages = merged_messages[-MAX_STORED_USER_MESSAGES:]
            existing["user_messages"] = merged_messages
            existing["last_user_message"] = merged_messages[-1]
        elif existing.get("last_user_message") is None and fallback_record.get("last_user_message"):
            existing["last_user_message"] = fallback_record.get("last_user_message")


def compute_time_range(args: argparse.Namespace) -> TimeRange:
    now = datetime.now(tz=UTC)

    if args.from_time or args.to_time:
        if args.last is not None:
            raise argparse.ArgumentTypeError("--last cannot be combined with --from/--to")

        from_dt = (
            parse_iso_datetime(args.from_time)
            if args.from_time
            else datetime.min.replace(tzinfo=UTC)
        )
        to_dt = parse_iso_datetime(args.to_time) if args.to_time else now
    else:
        duration = parse_duration(args.last or "14d")
        to_dt = now
        from_dt = now - duration

    if from_dt > to_dt:
        raise argparse.ArgumentTypeError("--from must be earlier than or equal to --to")

    return TimeRange(from_dt=from_dt, to_dt=to_dt)


def in_range(record: dict[str, Any], time_range: TimeRange) -> bool:
    start = record.get("start_time")
    end = record.get("end_time")

    if isinstance(start, datetime) and isinstance(end, datetime):
        return not (end < time_range.from_dt or start > time_range.to_dt)

    candidate = start if isinstance(start, datetime) else end if isinstance(end, datetime) else None
    if candidate is None:
        return False
    return time_range.from_dt <= candidate <= time_range.to_dt


def normalized_record(record: dict[str, Any], _logs_root: Path) -> dict[str, Any]:
    session_id = str(record.get("session_id"))
    transcript_path = record.get("transcript_path")
    transcript_ref_status = record.get("transcript_ref_status")
    if not isinstance(transcript_ref_status, str) or transcript_ref_status not in {
        "provided",
        "discovered",
        "missing",
    }:
        transcript_ref_status = "provided" if transcript_path else "missing"

    return {
        "session_id": session_id,
        "start_time": iso_or_none(record.get("start_time")),
        "end_time": iso_or_none(record.get("end_time")),
        "model": record.get("model"),
        "transcript_path": transcript_path,
        "transcript_ref_status": transcript_ref_status,
        "prompt_count": int(record.get("prompt_count") or 0),
        "user_message_preview": _build_user_message_preview(record),
    }


def format_table(records: list[dict[str, Any]]) -> str:
    headers = [
        "SESSION_ID",
        "START",
        "END",
        "PROMPTS",
        "USER_MESSAGE_PREVIEW",
        "MODEL",
        "TRANSCRIPT",
        "TRANSCRIPT_REF",
    ]
    rows: list[list[str]] = []

    for item in records:
        transcript_short = str(item.get("transcript_path") or "")
        rows.append(
            [
                str(item.get("session_id") or ""),
                str(item.get("start_time") or "-"),
                str(item.get("end_time") or "-"),
                str(item.get("prompt_count") or 0),
                str(item.get("user_message_preview") or ""),
                str(item.get("model") or "-"),
                transcript_short,
                str(item.get("transcript_ref_status") or "missing"),
            ]
        )

    widths = [len(header) for header in headers]
    for row in rows:
        for idx, value in enumerate(row):
            if idx == 6:
                widths[idx] = min(max(widths[idx], len(value)), 60)
            elif idx == 4:
                widths[idx] = min(max(widths[idx], len(value)), USER_MESSAGE_PREVIEW_MAX_LEN)
            else:
                widths[idx] = max(widths[idx], len(value))

    def trunc(value: str, width: int) -> str:
        if len(value) <= width:
            return value
        if width <= 1:
            return value[:width]
        return value[: width - 1] + "…"

    output = [
        "  ".join(trunc(h, widths[i]).ljust(widths[i]) for i, h in enumerate(headers)),
        "  ".join("-" * widths[i] for i in range(len(headers))),
    ]
    for row in rows:
        output.append("  ".join(trunc(v, widths[i]).ljust(widths[i]) for i, v in enumerate(row)))

    return "\n".join(output)


def cmd_list(args: argparse.Namespace) -> int:
    logs_root = Path(args.logs_root)
    try:
        time_range = compute_time_range(args)
    except argparse.ArgumentTypeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    sessions = load_index_sessions(logs_root)
    merge_fallback_sessions(logs_root, sessions)

    filtered = [record for record in sessions.values() if in_range(record, time_range)]
    filtered = [
        record
        for record in filtered
        if int(record.get("prompt_count") or 0) >= max(args.min_prompts, 0)
    ]
    filtered.sort(
        key=lambda record: (
            record.get("start_time") or datetime.min.replace(tzinfo=UTC),
            record.get("end_time") or datetime.min.replace(tzinfo=UTC),
        ),
        reverse=True,
    )

    limited = filtered[: max(args.limit, 0)]
    output_records = [normalized_record(record, logs_root) for record in limited]

    if args.format == "json":
        print(json.dumps(output_records, indent=2))
    else:
        print(format_table(output_records))

    return 0


def render_pretty(events: list[dict[str, Any]], session_id: str, path: Path) -> str:
    start_time: datetime | None = None
    end_time: datetime | None = None
    model: str | None = None
    transcript_path: str | None = None
    prompt_count = 0

    snippets: list[str] = []
    for event in events:
        ts = extract_timestamp(event)
        if ts is not None:
            if start_time is None or ts < start_time:
                start_time = ts
            if end_time is None or ts > end_time:
                end_time = ts

        if model is None:
            model = _take_model(event)

        if transcript_path is None:
            transcript_path = _take_transcript_path(event)

        payload = event.get("payload")
        payload_prompt = payload.get("prompt") if isinstance(payload, dict) else None
        if event.get("event") == "userMessage" or isinstance(payload_prompt, str):
            prompt_count += 1

        if len(snippets) < 8:
            text = ""
            if isinstance(payload_prompt, str):
                one_line = " ".join(payload_prompt.split())
                text = one_line[:120] + ("…" if len(one_line) > 120 else "")
            label = str(event.get("event") or "event")
            prefix = iso_or_none(ts) or "-"
            snippets.append(f"- {prefix} {label}{(': ' + text) if text else ''}")

    summary_lines = [
        f"session_id: {session_id}",
        f"file: {path}",
        f"events: {len(events)}",
        f"start_time: {iso_or_none(start_time) or '-'}",
        f"end_time: {iso_or_none(end_time) or '-'}",
        f"prompt_count: {prompt_count}",
        f"model: {model or '-'}",
        f"transcript_path: {transcript_path or '-'}",
        "",
        "event_snippets:",
    ]
    summary_lines.extend(snippets if snippets else ["- (no events parsed)"])
    return "\n".join(summary_lines)


def _extract_event_type(event: dict[str, Any]) -> str:
    for key in ("event_type", "type", "event"):
        value = event.get(key)
        if isinstance(value, str) and value:
            return value

    payload = event.get("payload")
    if isinstance(payload, dict):
        for key in ("event_type", "type", "event"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return value

    return ""


def _is_assistant_event(event: dict[str, Any]) -> bool:
    event_type = _extract_event_type(event).lower()
    if not event_type:
        return False

    if "assistant.message" in event_type:
        return True
    if event_type.startswith("assistant."):
        return True
    return "assistant" in event_type and ("message" in event_type or "response" in event_type)


def _is_tool_call_event(event: dict[str, Any]) -> bool:
    event_type = _extract_event_type(event).lower()
    if not event_type:
        return False

    tool_markers = (
        "function",
        "tool.execution_start",
        "tool.execution_complete",
    )
    if event_type in tool_markers:
        return True

    return (
        "function" in event_type
        or "tool.execution_start" in event_type
        or "tool.execution_complete" in event_type
    )


def _event_excerpt(event: dict[str, Any], limit: int = 140) -> str:
    payload = event.get("payload") if isinstance(event.get("payload"), dict) else {}
    candidates: list[Any] = [
        event.get("text"),
        event.get("content"),
        event.get("message"),
        payload.get("text") if isinstance(payload, dict) else None,
        payload.get("content") if isinstance(payload, dict) else None,
        payload.get("message") if isinstance(payload, dict) else None,
        payload.get("prompt") if isinstance(payload, dict) else None,
    ]

    text = next((value for value in candidates if isinstance(value, str) and value.strip()), "")
    normalized = " ".join(text.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[:limit] + "…"


def _resolve_allowed_roots(
    logs_root: Path, allow_transcript_roots: list[str] | None = None
) -> list[Path]:
    roots: list[Path] = [
        Path("/workspace"),
        logs_root,
        DEFAULT_VSCODE_WORKSPACE_STORAGE_ROOT,
    ]

    if allow_transcript_roots:
        roots.extend(Path(raw_path) for raw_path in allow_transcript_roots if raw_path)

    resolved_roots: list[Path] = []
    for root in roots:
        try:
            resolved = root.expanduser().resolve(strict=False)
        except OSError:
            continue
        if resolved not in resolved_roots:
            resolved_roots.append(resolved)

    return resolved_roots


def _is_path_allowed(candidate: Path, allowed_roots: list[Path]) -> bool:
    try:
        resolved = candidate.expanduser().resolve(strict=False)
    except OSError:
        return False

    for root in allowed_roots:
        if resolved == root or resolved.is_relative_to(root):
            return True

    return False


def _resolve_transcript_path(raw_path: str, logs_root: Path) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        return candidate
    return logs_root / candidate


def _find_transcript_fallback_candidates(
    session_id: str, allowed_roots: list[Path]
) -> tuple[list[Path], list[str], list[str]]:
    filename = f"{session_id}.jsonl"
    patterns = [
        f"**/GitHub.copilot-chat/transcripts/{filename}",
        f"**/{filename}",
    ]

    collected: dict[Path, Path] = {}
    searched_roots: list[str] = []

    for root in allowed_roots:
        if not root.exists() or not root.is_dir():
            continue

        searched_roots.append(str(root))
        try:
            for candidate in root.rglob(filename):
                if not candidate.is_file():
                    continue
                if not _is_path_allowed(candidate, allowed_roots):
                    continue
                resolved_candidate = candidate.expanduser().resolve(strict=False)
                if resolved_candidate not in collected:
                    collected[resolved_candidate] = candidate
        except OSError:
            continue

    candidates = [collected[path] for path in collected]
    return candidates, searched_roots, patterns


def _choose_transcript_fallback(candidates: list[Path], session_id: str) -> Path | None:
    if not candidates:
        return None

    preferred_suffix = Path("GitHub.copilot-chat") / "transcripts" / f"{session_id}.jsonl"
    preferred = [
        candidate
        for candidate in candidates
        if candidate.as_posix().endswith(str(preferred_suffix))
    ]
    pool = preferred if preferred else candidates

    def _mtime(candidate: Path) -> float:
        try:
            return candidate.stat().st_mtime
        except OSError:
            return float("-inf")

    return max(pool, key=_mtime)


def build_transcript_payload(
    session_events: list[dict[str, Any]],
    logs_root: Path,
    session_id: str | None,
    include_assistant: bool,
    include_tool_calls: bool,
    include_full_events: bool,
    allow_transcript_roots: list[str] | None = None,
) -> dict[str, Any]:
    warnings: list[str] = []
    source_path: str | None = None
    resolved_path: str | None = None
    fallback_used = False
    fallback_candidates_count = 0

    allowed_roots = _resolve_allowed_roots(logs_root, allow_transcript_roots)
    allowed_roots_str = [str(root) for root in allowed_roots]
    path_allowed = False

    transcript_raw_path: str | None = None
    for event in session_events:
        transcript_raw_path = _take_transcript_path(event)
        if transcript_raw_path:
            break

    base_payload: dict[str, Any] = {
        "source_path": source_path,
        "resolved_path": resolved_path,
        "fallback_used": fallback_used,
        "fallback_candidates_count": fallback_candidates_count,
        "allowed_roots": allowed_roots_str,
        "path_allowed": path_allowed,
        "event_count": 0,
        "warnings": warnings,
    }
    if include_assistant:
        base_payload["assistant_events"] = []
    if include_tool_calls:
        base_payload["tool_call_events"] = []
    if include_full_events:
        base_payload["all_events"] = []

    active_transcript_path: Path | None = None
    if transcript_raw_path:
        transcript_path = _resolve_transcript_path(transcript_raw_path, logs_root)
        source_path = transcript_raw_path
        active_transcript_path = transcript_path

    if (active_transcript_path is None or not active_transcript_path.exists()) and session_id:
        candidates, searched_roots, search_patterns = _find_transcript_fallback_candidates(
            session_id=session_id,
            allowed_roots=allowed_roots,
        )
        fallback_candidates_count = len(candidates)
        chosen_fallback = _choose_transcript_fallback(candidates, session_id)

        if chosen_fallback is not None:
            active_transcript_path = chosen_fallback
            fallback_used = True
            if source_path is None:
                source_path = f"fallback-discovered:{session_id}"
        else:
            roots_summary = ", ".join(searched_roots) if searched_roots else "(none)"
            pattern_summary = ", ".join(search_patterns)
            if transcript_raw_path:
                warnings.append(
                    "Transcript metadata path could not be resolved and fallback search found no matches. "
                    f"session_id={session_id}; source_path={transcript_raw_path}; roots=[{roots_summary}]; patterns=[{pattern_summary}]"
                )
            else:
                warnings.append(
                    "Transcript metadata missing and fallback search found no matches. "
                    f"session_id={session_id}; roots=[{roots_summary}]; patterns=[{pattern_summary}]"
                )

    if active_transcript_path is None:
        if not transcript_raw_path and not session_id:
            warnings.append(
                "Transcript metadata missing and no session_id was provided for fallback search."
            )
        base_payload["source_path"] = source_path
        base_payload["resolved_path"] = resolved_path
        base_payload["fallback_used"] = fallback_used
        base_payload["fallback_candidates_count"] = fallback_candidates_count
        base_payload["path_allowed"] = path_allowed
        return base_payload

    try:
        resolved_path = str(active_transcript_path.expanduser().resolve(strict=False))
    except OSError:
        resolved_path = str(active_transcript_path)

    base_payload["source_path"] = source_path
    base_payload["resolved_path"] = resolved_path
    base_payload["fallback_used"] = fallback_used
    base_payload["fallback_candidates_count"] = fallback_candidates_count

    path_allowed = _is_path_allowed(active_transcript_path, allowed_roots)
    base_payload["path_allowed"] = path_allowed

    if not path_allowed:
        allowed_roots_pretty = ", ".join(allowed_roots_str)
        warnings.append(
            f"Refused to load transcript outside allowed roots ({allowed_roots_pretty}): {active_transcript_path}"
        )
        return base_payload

    transcript_events, parse_warnings = parse_ndjson_with_warnings(active_transcript_path)
    warnings.extend(parse_warnings)

    payload: dict[str, Any] = {
        "source_path": source_path,
        "resolved_path": resolved_path,
        "fallback_used": fallback_used,
        "fallback_candidates_count": fallback_candidates_count,
        "allowed_roots": allowed_roots_str,
        "path_allowed": path_allowed,
        "event_count": len(transcript_events),
        "warnings": warnings,
    }

    if include_assistant:
        payload["assistant_events"] = [
            event for event in transcript_events if _is_assistant_event(event)
        ]

    if include_tool_calls:
        payload["tool_call_events"] = [
            event for event in transcript_events if _is_tool_call_event(event)
        ]

    if include_full_events:
        payload["all_events"] = transcript_events

    return payload


def render_transcript_pretty(transcript: dict[str, Any]) -> str:
    lines: list[str] = [
        "",
        "transcript:",
        f"source_path: {transcript.get('source_path') or '-'}",
        f"resolved_path: {transcript.get('resolved_path') or '-'}",
        f"fallback_used: {transcript.get('fallback_used')}",
        f"fallback_candidates_count: {transcript.get('fallback_candidates_count')}",
        f"path_allowed: {transcript.get('path_allowed')}",
        f"event_count: {transcript.get('event_count', 0)}",
    ]

    allowed_roots = transcript.get("allowed_roots")
    if isinstance(allowed_roots, list):
        lines.append("allowed_roots:")
        lines.extend(f"- {root}" for root in allowed_roots)

    warnings = transcript.get("warnings")
    if isinstance(warnings, list) and warnings:
        lines.append("warnings:")
        lines.extend(f"- {warning}" for warning in warnings)

    assistant_events = transcript.get("assistant_events")
    if isinstance(assistant_events, list):
        lines.append(f"assistant_event_count: {len(assistant_events)}")
        lines.append("assistant_event_excerpts:")
        if assistant_events:
            for event in assistant_events[:5]:
                event_type = _extract_event_type(event) or "event"
                excerpt = _event_excerpt(event)
                lines.append(f"- {event_type}{(': ' + excerpt) if excerpt else ''}")
        else:
            lines.append("- (none)")

    tool_call_events = transcript.get("tool_call_events")
    if isinstance(tool_call_events, list):
        lines.append(f"tool_call_event_count: {len(tool_call_events)}")
        lines.append("tool_call_event_excerpts:")
        if tool_call_events:
            for event in tool_call_events[:5]:
                event_type = _extract_event_type(event) or "event"
                excerpt = _event_excerpt(event)
                lines.append(f"- {event_type}{(': ' + excerpt) if excerpt else ''}")
        else:
            lines.append("- (none)")

    all_events = transcript.get("all_events")
    if isinstance(all_events, list):
        lines.append(f"all_events_count: {len(all_events)}")
        lines.append("all_events:")
        if all_events:
            for event in all_events:
                lines.append(json.dumps(event, ensure_ascii=False, indent=2))
        else:
            lines.append("- (none)")

    return "\n".join(lines)


def cmd_read(args: argparse.Namespace) -> int:
    logs_root = Path(args.logs_root)
    session_id = args.id
    path = logs_root / "sessions" / f"{session_id}.ndjson"

    if not path.exists():
        print(f"Session file not found: {path}", file=sys.stderr)
        return 1

    if args.format == "raw":
        print(path.read_text(encoding="utf-8", errors="replace"), end="")
        return 0

    events = parse_ndjson(path)

    include_transcript = (
        args.include_transcript
        or args.include_assistant
        or args.include_tool_calls
        or args.include_full_events
    )

    transcript_payload: dict[str, Any] | None = None
    if include_transcript:
        transcript_payload = build_transcript_payload(
            session_events=events,
            logs_root=logs_root,
            session_id=session_id,
            include_assistant=args.include_assistant,
            include_tool_calls=args.include_tool_calls,
            include_full_events=args.include_full_events,
            allow_transcript_roots=args.allow_transcript_root,
        )

    if args.format == "json":
        output: dict[str, Any] = {
            "session_id": session_id,
            "session_events": events,
        }
        if transcript_payload is not None:
            output["transcript"] = transcript_payload
        print(json.dumps(output, indent=2))
        return 0

    pretty_output = render_pretty(events, session_id, path)
    if transcript_payload is not None:
        pretty_output += render_transcript_pretty(transcript_payload)

    print(pretty_output)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="List and read GitHub Copilot session logs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser(
        "list", help="List sessions in a time range from Copilot logs."
    )
    list_parser.add_argument(
        "--from",
        dest="from_time",
        help="Start ISO datetime (UTC Z or offset), e.g. 2026-02-18T00:00:00Z",
    )
    list_parser.add_argument(
        "--to",
        dest="to_time",
        help="End ISO datetime (UTC Z or offset), e.g. 2026-02-25T23:59:59+00:00",
    )
    list_parser.add_argument(
        "--last",
        help="Relative duration window like 7d, 24h, 30m (default 14d if no range set).",
    )
    list_parser.add_argument("--limit", type=int, default=50, help="Maximum rows to return.")
    list_parser.add_argument(
        "--min-prompts",
        type=int,
        default=2,
        help=(
            "Minimum prompt_count required to include a session in list output "
            "(default 2; set to 1 to include single-prompt sessions)."
        ),
    )
    list_parser.add_argument(
        "--format",
        choices=("table", "json"),
        default="table",
        help="Output format.",
    )
    list_parser.add_argument(
        "--logs-root",
        default=str(DEFAULT_LOGS_ROOT),
        help="Copilot logs root directory.",
    )
    list_parser.set_defaults(func=cmd_list)

    read_parser = subparsers.add_parser("read", help="Read a specific session file by session id.")
    read_parser.add_argument("--id", required=True, help="Session id (permissive).")
    read_parser.add_argument(
        "--format",
        choices=("raw", "json", "pretty"),
        default="pretty",
        help="Output format.",
    )
    read_parser.add_argument(
        "--logs-root",
        default=str(DEFAULT_LOGS_ROOT),
        help="Copilot logs root directory.",
    )
    read_parser.add_argument(
        "--include-transcript",
        action="store_true",
        help="Load transcript artifact summary on demand.",
    )
    read_parser.add_argument(
        "--include-assistant",
        action="store_true",
        help="Include assistant transcript events.",
    )
    read_parser.add_argument(
        "--include-tool-calls",
        action="store_true",
        help="Include tool call transcript events.",
    )
    read_parser.add_argument(
        "--include-full-events",
        action="store_true",
        help="Include all transcript events.",
    )
    read_parser.add_argument(
        "--allow-transcript-root",
        action="append",
        default=[],
        metavar="PATH",
        help=(
            "Additional allowed root for transcript_path reads. " "May be provided multiple times."
        ),
    )
    read_parser.set_defaults(func=cmd_read)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    func = cast(Callable[[argparse.Namespace], int], args.func)
    return func(args)


if __name__ == "__main__":
    raise SystemExit(main())
