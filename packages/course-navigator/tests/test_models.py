from dataclasses import is_dataclass

import pytest
from course_navigator.models import CourseAnswer, CourseReference, NavigatorDeps
from pydantic import ValidationError


def test_course_reference_preserves_factory_path_and_title(
    course_reference_data: dict[str, str],
) -> None:
    ref_dict = course_reference_data
    ref = CourseReference(**ref_dict)  # type: ignore[arg-type]

    assert ref.path == ref_dict["path"]
    assert ref.title == ref_dict["title"]


def test_course_reference_raises_validation_error_for_non_string_path() -> None:
    with pytest.raises(ValidationError):
        CourseReference(path=123, title="Intro")  # type: ignore[arg-type]


def test_course_answer_factory_provides_summary_and_single_reference(
    course_answer: CourseAnswer,
) -> None:
    answer = course_answer

    assert isinstance(answer.summary, str) and answer.summary
    assert len(answer.references) == 1
    assert answer.references[0].path.endswith(".md")


def test_navigator_deps_factory_returns_dataclass_with_user_and_difficulty(
    navigator_deps: NavigatorDeps,
) -> None:
    deps = navigator_deps

    assert is_dataclass(deps)
    assert isinstance(deps.user_name, str) and deps.user_name
    assert isinstance(deps.difficulty, str) and deps.difficulty
    assert not hasattr(deps, "learning_root")


def test_navigator_deps_rejects_learning_root() -> None:
    with pytest.raises(TypeError):
        NavigatorDeps(  # type: ignore[call-arg]
            user_name="Student",
            difficulty="Beginner",
            learning_root="/learning",  # type: ignore
        )
