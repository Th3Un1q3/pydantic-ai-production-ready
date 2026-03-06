from pathlib import PurePath

from pydantic_ai import RunContext
from pydantic_ai_shared.config import LEARNING_ROOT

from course_navigator.models import NavigatorDeps
from course_navigator.utils import get_indexed_paths


def _indexed_paths() -> set[str]:
    return {PurePath(path).as_posix() for path in get_indexed_paths(LEARNING_ROOT)}


def read_lesson(_ctx: RunContext[NavigatorDeps], file_path: str) -> str:
    """Read the content of a lesson file.

    Args:
        ctx: The run context containing dependencies.
        file_path: The relative path to the lesson file.

    Returns:
        The content of the lesson file as a string.

    Raises:
        ValueError: If the file path is invalid or the file cannot be accessed.
    """
    clean_path = file_path.strip()
    if not clean_path:
        raise ValueError("Invalid file path: empty")

    pure_path = PurePath(clean_path)
    if pure_path.is_absolute() or ".." in pure_path.parts:
        raise ValueError(f"Invalid file path: {file_path}")

    normalized = pure_path.as_posix()
    if normalized not in _indexed_paths():
        raise ValueError(f"File path not indexed: {file_path}")

    full_path = LEARNING_ROOT / normalized
    try:
        full_path.resolve().relative_to(LEARNING_ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"Access denied: {file_path}") from exc

    if not full_path.is_file():
        raise ValueError(f"File not found: {file_path}")

    return full_path.read_text(encoding="utf-8")
