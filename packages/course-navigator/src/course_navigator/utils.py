from dataclasses import dataclass
from pathlib import Path

import frontmatter  # type: ignore[import-untyped]


@dataclass(frozen=True)
class IndexEntry:
    path: str
    title: str
    description: str | None


def _status_from_tags(tags: list[str | None]) -> str | None:
    for tag in tags:
        if not isinstance(tag, str):
            continue
        if tag.startswith("status:"):
            return tag.split(":", 1)[1].strip()
    return None


def _extract_title(content: str) -> str | None:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return None


def _has_frontmatter(path: Path) -> bool:
    with path.open(encoding="utf-8") as file_handle:
        lines = file_handle.readlines()

    if not lines or lines[0].strip() != "---":
        return False

    return any(line.strip() == "---" for line in lines[1:])


def _collect_entries(learning_root: Path) -> list[IndexEntry]:
    entries: list[IndexEntry] = []
    for path in sorted(learning_root.rglob("*.md")):
        if not _has_frontmatter(path):
            continue

        post = frontmatter.load(path)
        tags = post.metadata.get("tags", [])
        status = _status_from_tags(tags if isinstance(tags, list) else [])
        if status == "draft":
            continue

        title = _extract_title(post.content)
        if not title:
            continue

        description = post.metadata.get("description")
        description_value = str(description).strip() if description else None
        rel_path = path.relative_to(learning_root).as_posix()
        entries.append(IndexEntry(rel_path, title, description_value))

    return entries


def build_index(learning_root: Path) -> str:
    entries = _collect_entries(learning_root)
    lines: list[str] = []
    for entry in entries:
        if entry.description:
            lines.append(f"- {entry.path} | {entry.title} | {entry.description}")
        else:
            lines.append(f"- {entry.path} | {entry.title}")
    return "\n".join(lines)


def get_indexed_paths(learning_root: Path) -> set[str]:
    return {entry.path for entry in _collect_entries(learning_root)}
