"""Test data factories for the course-navigator package.

These helpers produce randomly generated values so that tests
cannot accidentally pass by hard‑coding specific strings. Having
random data increases the chance that a bug which depends on a
fixed value will be caught.

We intentionally keep the randomness modest so that tests remain
fast and deterministic enough for CI; the global seed is not
reset, but most of our factories generate only a few characters.
"""

from __future__ import annotations

import random
import string
from typing import Any

from course_navigator.models import CourseAnswer, CourseReference, NavigatorDeps


def _random_string(length: int = 8) -> str:
    """Return a simple random alphanumeric string."""
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choices(alphabet, k=length))


def build_navigator_deps() -> NavigatorDeps:
    """Return a randomly‑populated :class:`NavigatorDeps`.

    We use ``build_`` instead of ``create_`` because nothing is being
    persisted; the object is constructed in memory only.  This mirrors the
    naming convention used elsewhere in the workspace.
    """

    # difficulty is currently a free‑form string but we pick from a
    # small set so the values are plausible.
    difficulty = random.choice(["Beginner", "Intermediate", "Advanced"])
    return NavigatorDeps(user_name=_random_string(10), difficulty=difficulty)


def build_course_reference_data() -> dict[str, Any]:
    """Return the raw data for a course reference.

    This constructs a dict instead of a full ``CourseReference`` so callers
    can choose whether to convert it or leave it as a payload.  The naming
    (`build_` + ``_data``) highlights that no persistence occurs.
    """

    return {"path": f"{_random_string(5)}.md", "title": _random_string(12)}


def build_course_answer() -> CourseAnswer:
    """Build a :class:`CourseAnswer` with randomized contents.

    Internally uses :func:`build_course_reference_data` to obtain the
    reference payload and then instantiates a ``CourseReference`` so that the
    returned object is valid for existing tests.
    """

    raw = build_course_reference_data()
    refs_list: list[CourseReference] = [CourseReference(**raw)]
    return CourseAnswer(summary=_random_string(20), references=refs_list)
