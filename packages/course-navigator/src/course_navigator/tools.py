from pathlib import PurePath

from pydantic_ai import RunContext
from pydantic_ai_shared.config import LEARNING_ROOT

from course_navigator.models import NavigatorDeps

_ALLOWED_PATHS: set[str] = set()


def set_allowed_paths(paths: set[str]) -> None:
    global _ALLOWED_PATHS
    _ALLOWED_PATHS = {PurePath(path).as_posix() for path in paths}


def read_lesson(ctx: RunContext[NavigatorDeps], file_path: str) -> str:
    clean_path = file_path.strip()
    if not clean_path:
        raise ValueError("Invalid file path: empty")

    pure_path = PurePath(clean_path)
    if pure_path.is_absolute() or ".." in pure_path.parts:
        raise ValueError(f"Invalid file path: {file_path}")

    normalized = pure_path.as_posix()
    if normalized not in _ALLOWED_PATHS:
        raise ValueError(f"File path not indexed: {file_path}")

    full_path = LEARNING_ROOT / normalized
    try:
        full_path.resolve().relative_to(LEARNING_ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"Access denied: {file_path}") from exc

    if not full_path.is_file():
        raise ValueError(f"File not found: {file_path}")

    return full_path.read_text(encoding="utf-8")
