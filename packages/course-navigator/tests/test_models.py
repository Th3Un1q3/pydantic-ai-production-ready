from dataclasses import is_dataclass

import pytest
from course_navigator.models import CourseReference, NavigatorDeps
from course_navigator.tests.factories import (
    build_course_answer,
    build_course_reference_data,
    build_navigator_deps,
)
from pydantic import ValidationError


def test_course_reference_one() -> None:
    # use the factory to generate random values and verify they stick
    ref_dict = build_course_reference_data()
    ref = CourseReference(**ref_dict)  # type: ignore[arg-type]

    assert ref.path == ref_dict["path"]
    assert ref.title == ref_dict["title"]


def test_course_reference_interface_invalid_types() -> None:
    with pytest.raises(ValidationError):
        CourseReference(path=123, title="Intro")  # type: ignore[arg-type]


def test_course_answer_one() -> None:
    # ensure factory creates a valid object and that its data is
    # honoured
    answer = build_course_answer()

    assert isinstance(answer.summary, str) and answer.summary
    assert len(answer.references) == 1
    assert answer.references[0].path.endswith(".md")


def test_navigator_deps_one() -> None:
    deps = build_navigator_deps()

    assert is_dataclass(deps)
    # factory returns random strings so we simply verify the types
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
