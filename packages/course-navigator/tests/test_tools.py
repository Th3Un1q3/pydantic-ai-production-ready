from pathlib import Path
from unittest.mock import Mock

import pytest
from course_navigator.tools import read_lesson
from pydantic_ai import RunContext


def write_indexed_lesson(learning_root: Path, relative_path: str, body: str) -> str:
    lesson_path = learning_root / relative_path
    lesson_path.parent.mkdir(parents=True, exist_ok=True)
    lesson_text = f"---\n---\n# Indexed Lesson\n\n{body}\n"
    lesson_path.write_text(lesson_text, encoding="utf-8")
    return lesson_text


def test_read_lesson_returns_content_for_allowed_relative_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    lesson_text = write_indexed_lesson(tmp_path, "lesson.md", "content")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)

    ctx = Mock(spec=RunContext)

    assert read_lesson(ctx, "lesson.md") == lesson_text


def test_read_lesson_rejects_absolute_path(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", Path("/tmp"))

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="Invalid file path"):
        read_lesson(ctx, "/etc/passwd")


def test_read_lesson_rejects_empty_path(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", Path("/tmp"))

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="empty"):
        read_lesson(ctx, " ")


def test_read_lesson_rejects_traversal(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", Path("/tmp"))

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="Invalid file path"):
        read_lesson(ctx, "../secret.md")


def test_read_lesson_requires_allowlist(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    lesson = tmp_path / "lesson.md"
    lesson.write_text("content", encoding="utf-8")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="not indexed"):
        read_lesson(ctx, "lesson.md")


def test_read_lesson_missing_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)
    monkeypatch.setattr("course_navigator.tools._indexed_paths", lambda: {"missing.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="File not found"):
        read_lesson(ctx, "missing.md")


def test_read_lesson_blocks_symlink_escape(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    root = tmp_path / "root"
    root.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    secret = outside / "secret.md"
    secret.write_text("secret", encoding="utf-8")

    alias = root / "alias"
    alias.symlink_to(outside, target_is_directory=True)

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", root)
    monkeypatch.setattr("course_navigator.tools._indexed_paths", lambda: {"alias/secret.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="Access denied"):
        read_lesson(ctx, "alias/secret.md")


def test_read_lesson_rejects_when_allowlist_is_empty(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    write_indexed_lesson(tmp_path, "lesson.md", "content")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)
    monkeypatch.setattr("course_navigator.tools._indexed_paths", lambda: set())

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="not indexed"):
        read_lesson(ctx, "lesson.md")


def test_read_lesson_enforces_exact_allowed_path_boundary(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    write_indexed_lesson(tmp_path, "lesson.md", "content")
    disallowed = tmp_path / "lesson.md.bak"
    disallowed.write_text("backup", encoding="utf-8")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="not indexed"):
        read_lesson(ctx, "lesson.md.bak")


def test_read_lesson_normalizes_dot_prefix_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    lesson_text = write_indexed_lesson(tmp_path, "lesson.md", "content")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)

    ctx = Mock(spec=RunContext)

    assert read_lesson(ctx, "./lesson.md") == lesson_text
