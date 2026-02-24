import asyncio

import pytest


def test_shared_package_sanity_assertion_passes() -> None:
    from pydantic_ai_shared import __version__

    assert isinstance(__version__, str)
    assert __version__.count(".") == 2


def test_shared_config_exposes_default_model_constants() -> None:
    from pydantic_ai_shared import config

    assert hasattr(config, "DEFAULT_MODEL_OPENAI")
    assert hasattr(config, "DEFAULT_MODEL_ANTHROPIC")
    assert hasattr(config, "DEFAULT_MODEL_OPENROUTER")

    assert "openai" in config.DEFAULT_MODEL_OPENAI.lower()
    assert "anthropic" in config.DEFAULT_MODEL_ANTHROPIC.lower()


@pytest.mark.asyncio
async def test_shared_test_harness_supports_async_execution() -> None:
    result = await asyncio.sleep(0, result="async-ok")
    assert result == "async-ok"
