"""Pytest configuration for course-navigator tests."""

from collections.abc import Iterator

import pytest
from pydantic_ai import models

pytest_plugins = ["tests.factories"]

models.ALLOW_MODEL_REQUESTS = False


@pytest.fixture
def allow_model_requests() -> Iterator[None]:
    """Temporarily allow real model requests for a single test.

    Use this only for tests that intentionally hit an external provider.
    Do not use it for unit tests; keep those deterministic with mocked/stubbed models.
    """
    with models.override_allow_model_requests(True):
        yield
