from pathlib import Path
from unittest.mock import MagicMock, patch

from course_navigator.utils import build_index, get_indexed_paths


def _write_lesson(
    path: Path,
    *,
    status: str,
    title: str,
    description: str,
) -> None:
    content = (
        "---\n"
        f"description: {description}\n"
        "tags:\n"
        f"  - status:{status}\n"
        "---\n\n"
        f"# {title}\n"
        "\nBody text.\n"
    )
    path.write_text(content, encoding="utf-8")


def test_build_index_filters_draft_and_parses_title(tmp_path: Path) -> None:
    published = tmp_path / "lessons" / "published.md"
    draft = tmp_path / "lessons" / "draft.md"
    published.parent.mkdir(parents=True, exist_ok=True)

    _write_lesson(
        published,
        status="published",
        title="Published Lesson",
        description="Published description",
    )
    _write_lesson(
        draft,
        status="draft",
        title="Draft Lesson",
        description="Draft description",
    )

    index = build_index(tmp_path)

    assert "lessons/published.md" in index
    assert "Published Lesson" in index
    assert "Published description" in index
    assert "lessons/draft.md" not in index


def test_build_index_skips_missing_frontmatter(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    lesson.write_text("# Title\n\nBody", encoding="utf-8")

    index = build_index(tmp_path)

    assert "lesson.md" not in index


def test_build_index_skips_unclosed_frontmatter(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    content = "---\n" "description: Missing end\n" "tags:\n" "  - status:published\n" "# Title\n"
    lesson.write_text(content, encoding="utf-8")

    index = build_index(tmp_path)

    assert "lesson.md" not in index


def test_build_index_skips_missing_title(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    content = (
        "---\n" "description: No title\n" "tags:\n" "  - status:published\n" "---\n\n" "Body only\n"
    )
    lesson.write_text(content, encoding="utf-8")

    index = build_index(tmp_path)

    assert "lesson.md" not in index


def test_build_index_includes_entries_without_description(tmp_path: Path) -> None:
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


def test_get_indexed_paths_includes_non_draft(tmp_path: Path) -> None:
    published = tmp_path / "published.md"
    content = (
        "---\n"
        "description: Published\n"
        "tags:\n"
        "  - status:published\n"
        "---\n\n"
        "# Published\n"
    )
    published.write_text(content, encoding="utf-8")

    paths = get_indexed_paths(tmp_path)

    assert "published.md" in paths


def test_build_index_includes_when_no_status_tag(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    content = (
        "---\n"
        "description: No status\n"
        "tags:\n"
        "  - topic:core\n"
        "  -\n"
        "---\n\n"
        "# Untagged Status\n"
    )
    lesson.write_text(content, encoding="utf-8")

    index = build_index(tmp_path)

    assert "lesson.md" in index


def test_build_index_handles_blank_frontmatter_lines(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    content = (
        "---\n"
        "description: With blanks\n"
        "\n"
        "tags:\n"
        "  - status:published\n"
        "---\n\n"
        "# Blank Lines\n"
    )
    lesson.write_text(content, encoding="utf-8")

    index = build_index(tmp_path)

    assert "lesson.md" in index


def test_build_index_uses_frontmatter_library(tmp_path: Path) -> None:
    lesson = tmp_path / "lesson.md"
    lesson.write_text("---\ndescription: X\n---\n\n# Title\n", encoding="utf-8")

    mock_post = MagicMock()
    mock_post.metadata = {"description": "X", "tags": ["status:published"]}
    mock_post.content = "# Title\n"

    with patch("course_navigator.utils.frontmatter.load", return_value=mock_post) as mock_load:
        index = build_index(tmp_path)

    mock_load.assert_called_once_with(lesson)
    assert "lesson.md" in index
