import os
from unittest.mock import patch

import pytest

from pydantic_ai_shared.resolver import resolve_model


def test_resolve_no_provider_zero_exception():
    """
    ZOMBIE: Zero.
    Calling resolve_model() with no API keys in environment should raise an exception.
    """
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(
            ValueError,
            match="Please set one of OPENROUTER_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY",
        ):
            resolve_model()


def test_resolve_default_with_openai_one():
    """
    ZOMBIE: One.
    Calling resolve_model() with just OpenAI key returns default OpenAI model.
    """
    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-oa-..."}, clear=True):
        model = resolve_model()
        assert model.startswith("openai:")


def test_resolve_env_precedence_boundary():
    """
    ZOMBIE: Boundary.
    Test precedence: OpenRouter > Anthropic > OpenAI.
    """
    # 1. OpenRouter (highest priority)
    with patch.dict(
        os.environ,
        {
            "OPENROUTER_API_KEY": "sk-or-...",
            "ANTHROPIC_API_KEY": "sk-ant-...",
            "OPENAI_API_KEY": "sk-oa-...",
        },
    ):
        assert resolve_model().startswith("openrouter:")

    # 2. Anthropic (No OpenRouter)
    with patch.dict(
        os.environ, {"ANTHROPIC_API_KEY": "sk-ant-...", "OPENAI_API_KEY": "sk-oa-..."}, clear=True
    ):
        assert resolve_model().startswith("anthropic:")

    # 3. OpenAI (No others)
    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-oa-..."}, clear=True):
        assert resolve_model().startswith("openai:")


def test_resolve_provider_default_overrides_boundary():
    """
    ZOMBIE: Boundary.
    Test that specific model overrides work when that provider is active.
    e.g. DEFAULT_MODEL_OPENAI overrides the hardcoded default.
    """
    # Override OpenAI Default
    with patch.dict(
        os.environ,
        {"OPENAI_API_KEY": "sk-oa", "DEFAULT_MODEL_OPENAI": "openai:gpt-4-turbo-preview"},
        clear=True,
    ):
        assert resolve_model() == "openai:gpt-4-turbo-preview"

    # Override Anthropic Default
    with patch.dict(
        os.environ,
        {"ANTHROPIC_API_KEY": "sk-ant", "DEFAULT_MODEL_ANTHROPIC": "anthropic:claude-3-opus"},
        clear=True,
    ):
        assert resolve_model() == "anthropic:claude-3-opus"


def test_interface_no_args():
    """
    ZOMBIE: Interface.
    Ensure we do NOT accept arguments as per requirement "don't even provide such an option".
    """
    # Attempting to pass an argument should raise TypeError
    with pytest.raises(TypeError):
        resolve_model("some-tag")
