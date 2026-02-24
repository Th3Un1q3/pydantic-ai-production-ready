from pathlib import Path
from unittest.mock import Mock

import pytest
from course_navigator.tools import read_lesson, set_allowed_paths
from pydantic_ai import RunContext


def test_read_lesson_returns_content_for_allowed_relative_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    lesson = tmp_path / "lesson.md"
    lesson.write_text("content", encoding="utf-8")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)
    set_allowed_paths({"lesson.md"})

    ctx = Mock(spec=RunContext)

    assert read_lesson(ctx, "lesson.md") == "content"


def test_read_lesson_rejects_absolute_path(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", Path("/tmp"))
    set_allowed_paths({"lesson.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="Invalid file path"):
        read_lesson(ctx, "/etc/passwd")


def test_read_lesson_rejects_empty_path(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", Path("/tmp"))
    set_allowed_paths({"lesson.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="empty"):
        read_lesson(ctx, " ")


def test_read_lesson_rejects_traversal(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", Path("/tmp"))
    set_allowed_paths({"lesson.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="Invalid file path"):
        read_lesson(ctx, "../secret.md")


def test_read_lesson_requires_allowlist(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    lesson = tmp_path / "lesson.md"
    lesson.write_text("content", encoding="utf-8")

    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)
    set_allowed_paths({"other.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="not indexed"):
        read_lesson(ctx, "lesson.md")


def test_read_lesson_missing_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("course_navigator.tools.LEARNING_ROOT", tmp_path)
    set_allowed_paths({"missing.md"})

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
    set_allowed_paths({"alias/secret.md"})

    ctx = Mock(spec=RunContext)

    with pytest.raises(ValueError, match="Access denied"):
        read_lesson(ctx, "alias/secret.md")
