"""Pytest configuration for course-navigator tests."""

from collections.abc import Generator

import pytest
from course_navigator import tools
from pydantic_ai import models

pytest_plugins = ["course_navigator.tests.factories"]


@pytest.fixture(autouse=True)
def isolate_global_test_state() -> Generator[None, None, None]:
    original_allow_model_requests = models.ALLOW_MODEL_REQUESTS
    original_allowed_paths = tools._ALLOWED_PATHS.copy()

    yield

    models.ALLOW_MODEL_REQUESTS = original_allow_model_requests
    tools._ALLOWED_PATHS = original_allowed_paths
