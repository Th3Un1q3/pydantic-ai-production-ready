#!/usr/bin/env python3
"""Read a JSON/JSONC MCP config, normalize it, substitute ${env:VAR} placeholders,
rename top-level `servers` -> `mcpServers`, and emit compact JSON to stdout.

Usage: python3 scripts/transform_mcp.py path/to/.vscode/mcp.json

Exit codes:
 - 0 : OK (prints JSON to stdout) or file missing (prints nothing)
 - 2 : parse / processing error (message on stderr)
"""
import json
import os
import re
import sys


def strip_jsonc(text: str) -> str:
    # Safely strip comments from JSONC while preserving strings.
    # Iterate characters and skip comment sequences only when not inside a string.
    out = []
    i = 0
    n = len(text)
    in_string = False
    string_quote = None
    escape = False
    while i < n:
        c = text[i]
        if in_string:
            out.append(c)
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == string_quote:
                in_string = False
            i += 1
            continue
        # not in string
        if c == '"' or c == "'":
            in_string = True
            string_quote = c
            out.append(c)
            i += 1
            continue
        # single-line comment
        if c == '/' and i + 1 < n and text[i + 1] == '/':
            i += 2
            while i < n and text[i] not in '\r\n':
                i += 1
            continue
        # block comment
        if c == '/' and i + 1 < n and text[i + 1] == '*':
            i += 2
            while i + 1 < n and not (text[i] == '*' and text[i + 1] == '/'):
                i += 1
            i += 2 if i + 1 <= n else 0
            continue
        out.append(c)
        i += 1
    res = ''.join(out)
    # remove trailing commas before } or ]
    res = re.sub(r',\s*(?=[}\]])', '', res)
    return res


def _resolve_env_var(name: str) -> tuple[str, str | None]:
    """Resolve an environment variable for placeholder `name`.

    Strategy (in order):
    1. exact match
    2. case-insensitive exact match
    3. key endswith name (case-insensitive)
    4. key contains name (case-insensitive)

    Returns (value, matched_key) or ("", None) if not found.
    """
    # exact
    if name in os.environ:
        return os.environ[name], name
    # case-insensitive exact
    lname = name.lower()
    for k, v in os.environ.items():
        if k.lower() == lname:
            return v, k
    # endswith
    candidates = [k for k in os.environ.keys() if k.lower().endswith(lname)]
    if candidates:
        # prefer the shortest candidate (most specific suffix)
        candidates.sort(key=len)
        k = candidates[0]
        return os.environ[k], k
    # contains
    candidates = [k for k in os.environ.keys() if lname in k.lower()]
    if candidates:
        candidates.sort(key=len)
        k = candidates[0]
        return os.environ[k], k
    return "", None


def walk_replace_env(obj):
    if isinstance(obj, str):
        def repl(m):
            name = m.group(1)
            val, matched = _resolve_env_var(name)
            if val == "":
                # warn but continue
                print(f"warning: env var {name} not set (no matching OS env)", file=sys.stderr)
            elif matched is not None and matched != name:
                # informative message when we used a different env var name
                print(f"info: substituted placeholder {name} with env var {matched}", file=sys.stderr)
            return val
        return re.sub(r"\$\{env:([A-Za-z0-9_]+)\}", repl, obj)
    if isinstance(obj, dict):
        return {k: walk_replace_env(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk_replace_env(x) for x in obj]
    return obj


def main():
    if len(sys.argv) < 2:
        print("usage: transform_mcp.py PATH_TO_MCP_JSON", file=sys.stderr)
        return 2

    p = sys.argv[1]
    if not os.path.exists(p):
        # no file -> silently return nothing so callers can fallback
        return 0

    try:
        raw = open(p, "r", encoding="utf-8").read()
    except Exception as e:
        print(f"failed to read {p}: {e}", file=sys.stderr)
        return 2

    try:
        cleaned = strip_jsonc(raw)
        data = json.loads(cleaned)
    except Exception as e:
        print(f"failed to parse {p}: {e}", file=sys.stderr)
        return 2

    # rename 'servers' -> 'mcpServers' if present
    if isinstance(data, dict) and "servers" in data:
        data["mcpServers"] = data.pop("servers")

    # replace ${env:VAR} placeholders across the structure
    data = walk_replace_env(data)

    # emit compact JSON
    try:
        out = json.dumps(data, separators=(",", ":"))
        sys.stdout.write(out)
        return 0
    except Exception as e:
        print(f"failed to serialize transformed JSON: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
