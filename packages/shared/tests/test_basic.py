"""
Tests for Pydantic AI Shared utilities.
"""
import pytest


def test_basic():
    """Test that basic assertions work."""
    assert True


def test_config():
    """Test configuration module."""
    from pydantic_ai_shared import config
    
    # Test that we can get default models
    openai_model = config.get_default_model("openai")
    assert isinstance(openai_model, str)
    assert "openai" in openai_model or "gpt" in openai_model.lower()
    
    anthropic_model = config.get_default_model("anthropic")
    assert isinstance(anthropic_model, str)
    assert "anthropic" in anthropic_model or "claude" in anthropic_model.lower()


@pytest.mark.asyncio
async def test_async():
    """Test that async tests work."""
    assert True

