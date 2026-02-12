from dataclasses import is_dataclass

import pytest
from course_navigator.models import CourseAnswer, CourseReference, NavigatorDeps
from pydantic import ValidationError


def test_course_reference_one() -> None:
    ref = CourseReference(path="learning/intro.md", title="Intro")

    assert ref.path == "learning/intro.md"
    assert ref.title == "Intro"


def test_course_reference_interface_invalid_types() -> None:
    with pytest.raises(ValidationError):
        CourseReference(path=123, title="Intro")  # type: ignore[arg-type]


def test_course_answer_one() -> None:
    answer = CourseAnswer(
        summary="Overview",
        references=[{"path": "learning/intro.md", "title": "Intro"}],  # type: ignore[list-item]
    )

    assert answer.summary == "Overview"
    assert len(answer.references) == 1
    assert answer.references[0].path == "learning/intro.md"


def test_navigator_deps_one() -> None:
    deps = NavigatorDeps(
        user_name="Student",
        difficulty="Beginner",
    )

    assert is_dataclass(deps)
    assert deps.user_name == "Student"
    assert deps.difficulty == "Beginner"
    assert not hasattr(deps, "learning_root")


def test_navigator_deps_rejects_learning_root() -> None:
    with pytest.raises(TypeError):
        NavigatorDeps(  # type: ignore[call-arg]
            user_name="Student",
            difficulty="Beginner",
            learning_root="/learning",
        )
