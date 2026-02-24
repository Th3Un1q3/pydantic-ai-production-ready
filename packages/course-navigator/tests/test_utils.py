from collections.abc import Callable
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from course_navigator.utils import build_index, get_indexed_paths


@pytest.fixture
def write_lesson(tmp_path: Path) -> Callable[..., None]:
    """Helper for creating a lesson file with frontmatter.

    The returned function ensures the parent directory exists and writes a
    minimal markdown file containing ``description`` and a ``status`` tag.
    """

    def _writer(
        path: Path, *, status: str = "published", title: str = "Title", description: str = ""
    ) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        content = (
            "---\n"
            f"description: {description}\n"
            "tags:\n"
            f"  - status:{status}\n"
            "---\n\n"
            f"# {title}\n\n"
            "Body text.\n"
        )
        path.write_text(content, encoding="utf-8")

    return _writer


def test_build_index_filters_out_draft_lessons(
    write_lesson: Callable[..., None],
    tmp_path: Path,
) -> None:
    published = tmp_path / "lessons" / "published.md"
    draft = tmp_path / "lessons" / "draft.md"

    write_lesson(
        published, status="published", title="Published Lesson", description="Published description"
    )
    write_lesson(draft, status="draft", title="Draft Lesson", description="Draft description")

    index = build_index(tmp_path)

    assert "lessons/published.md" in index
    assert "Published Lesson" in index
    assert "Published description" in index
    assert "lessons/draft.md" not in index


def test_build_index_skips_invalid_frontmatter(tmp_path: Path) -> None:
    """Any of several malformed frontmatter cases should be ignored."""

    bad_cases = [
        "# Title\n\nBody",  # completely missing delimiters
        "---\ndescription: Missing end\ntags:\n  - status:published\n# Title\n",  # no closing '---'
        "---\ndescription: No title\ntags:\n  - status:published\n---\n\nBody only\n",  # missing heading
    ]

    for idx, content in enumerate(bad_cases):
        lesson = tmp_path / f"bad_{idx}.md"
        lesson.write_text(content, encoding="utf-8")
        index = build_index(tmp_path)
        assert f"bad_{idx}.md" not in index


def test_build_index_includes_entry_without_description(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    content = (
        "---\n"
        "tags:\n"
        "  - status:published\n"
        "references:\n"
        "  next: ./next.md\n"
        "---\n\n"
        "# Title Only\n"
        "\nBody\n"
    )
    lesson.write_text(content, encoding="utf-8")

    index = build_index(tmp_path)

    assert "lesson.md" in index
    assert "Title Only" in index
    assert "|" in index
    assert "description" not in index


def test_get_indexed_paths_filters_and_includes(tmp_path: Path) -> None:
    published = tmp_path / "published.md"
    published.write_text(
        "---\ndescription: Published\ntags:\n  - status:published\n---\n\n# Published\n",
        encoding="utf-8",
    )
    untagged = tmp_path / "lesson.md"
    untagged.write_text(
        "---\ndescription: No status\ntags:\n  - topic:core\n  -\n---\n\n# Untagged Status\n",
        encoding="utf-8",
    )

    paths = get_indexed_paths(tmp_path)

    assert "published.md" in paths
    assert "lesson.md" in paths


def test_build_index_blank_lines_and_frontmatter_library(tmp_path: Path) -> None:
    # blank lines should not confuse the parser, and we should use the
    # external frontmatter library when available.
    lesson = tmp_path / "lesson.md"
    lesson.write_text("---\ndescription: X\n---\n\n# Title\n", encoding="utf-8")

    mock_post = MagicMock()
    mock_post.metadata = {"description": "X", "tags": ["status:published"]}
    mock_post.content = "# Title\n"

    with patch("course_navigator.utils.frontmatter.load", return_value=mock_post) as mock_load:
        index = build_index(tmp_path)

    mock_load.assert_called_once_with(lesson)
    assert "lesson.md" in index
