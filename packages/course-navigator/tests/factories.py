"""Pytest fixtures for building test data in course-navigator tests."""

from __future__ import annotations

import random
import string
from collections.abc import Callable

import pytest
from course_navigator.models import CourseAnswer, CourseReference, NavigatorDeps


@pytest.fixture
def random_generator() -> random.Random:
    """Provide a deterministic random generator for stable tests."""

    return random.Random(42)


@pytest.fixture
def random_string(random_generator: random.Random) -> Callable[[int], str]:
    """Return a callable that generates random alphanumeric strings."""

    def _build_random_string(length: int = 8) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(random_generator.choices(alphabet, k=length))

    return _build_random_string


@pytest.fixture
def navigator_deps(
    random_generator: random.Random,
    random_string: Callable[[int], str],
) -> NavigatorDeps:
    """Build a valid ``NavigatorDeps`` instance for tests."""

    difficulty = random_generator.choice(["Beginner", "Intermediate", "Advanced"])
    return NavigatorDeps(user_name=random_string(10), difficulty=difficulty)


@pytest.fixture
def course_reference_data(random_string: Callable[[int], str]) -> dict[str, str]:
    """Build dictionary data for creating a ``CourseReference``."""

    return {"path": f"{random_string(5)}.md", "title": random_string(12)}


@pytest.fixture
def course_answer(
    course_reference_data: dict[str, str],
    random_string: Callable[[int], str],
) -> CourseAnswer:
    """Build a valid ``CourseAnswer`` instance with a single reference."""

    refs_list: list[CourseReference] = [CourseReference(**course_reference_data)]
    return CourseAnswer(summary=random_string(20), references=refs_list)
