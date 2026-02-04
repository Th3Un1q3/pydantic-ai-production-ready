"""
Tests for Pydantic AI Shared utilities.
"""

import pytest


def test_basic() -> None:
    """Test that basic assertions work."""
    assert True


def test_config() -> None:
    """Test configuration module."""
    from pydantic_ai_shared import config

    # Test that logic has been moved to constants
    assert hasattr(config, "DEFAULT_MODEL_OPENAI")
    assert hasattr(config, "DEFAULT_MODEL_ANTHROPIC")
    assert hasattr(config, "DEFAULT_MODEL_OPENROUTER")

    # Test basic string integrity
    assert "openai" in config.DEFAULT_MODEL_OPENAI.lower()
    assert "anthropic" in config.DEFAULT_MODEL_ANTHROPIC.lower()


@pytest.mark.asyncio
async def test_async() -> None:
    """Test that async tests work."""
    assert True
