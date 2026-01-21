"""
Example test to verify the test infrastructure is working.
"""
import pytest

import src


def test_basic():
    """Test that basic assertions work."""
    assert True


def test_import():
    """Test that we can import the main package."""
    assert hasattr(src, "__version__")


@pytest.mark.asyncio
async def test_async():
    """Test that async tests work."""
    assert True
