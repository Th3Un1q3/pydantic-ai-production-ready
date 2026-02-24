import os
from unittest.mock import patch

import pytest

from pydantic_ai_shared.resolver import resolve_model


def test_resolve_model_raises_when_no_provider_api_key_present() -> None:
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(
            ValueError,
            match="Please set one of OPENROUTER_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY",
        ):
            resolve_model()


def test_resolve_model_returns_openai_default_when_only_openai_key_present() -> None:
    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-oa-..."}, clear=True):
        model = resolve_model()
        assert isinstance(model, str)
        assert model.startswith("openai:")


def test_resolve_model_prefers_provider_order_openrouter_then_anthropic_then_openai() -> None:
    with patch.dict(
        os.environ,
        {
            "OPENROUTER_API_KEY": "sk-or-...",
            "ANTHROPIC_API_KEY": "sk-ant-...",
            "OPENAI_API_KEY": "sk-oa-...",
        },
    ):
        model = resolve_model()
        assert isinstance(model, str)
        assert model.startswith("openrouter:")

    with patch.dict(
        os.environ, {"ANTHROPIC_API_KEY": "sk-ant-...", "OPENAI_API_KEY": "sk-oa-..."}, clear=True
    ):
        model = resolve_model()
        assert isinstance(model, str)
        assert model.startswith("anthropic:")

    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-oa-..."}, clear=True):
        model = resolve_model()
        assert isinstance(model, str)
        assert model.startswith("openai:")


def test_resolve_model_uses_provider_default_override_when_set() -> None:
    with patch.dict(
        os.environ,
        {
            "OPENROUTER_API_KEY": "sk-or",
            "DEFAULT_MODEL_OPENROUTER": "openrouter:meta-llama/llama-3.1-8b-instruct",
        },
        clear=True,
    ):
        assert resolve_model() == "openrouter:meta-llama/llama-3.1-8b-instruct"

    with patch.dict(
        os.environ,
        {"OPENAI_API_KEY": "sk-oa", "DEFAULT_MODEL_OPENAI": "openai:gpt-4-turbo-preview"},
        clear=True,
    ):
        assert resolve_model() == "openai:gpt-4-turbo-preview"

    with patch.dict(
        os.environ,
        {"ANTHROPIC_API_KEY": "sk-ant", "DEFAULT_MODEL_ANTHROPIC": "anthropic:claude-3-opus"},
        clear=True,
    ):
        assert resolve_model() == "anthropic:claude-3-opus"


def test_resolve_model_rejects_positional_argument() -> None:
    with pytest.raises(TypeError):
        resolve_model("some-tag")  # type: ignore[call-arg]
