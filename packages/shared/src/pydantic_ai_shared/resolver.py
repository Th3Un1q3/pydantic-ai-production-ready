import os

from pydantic_ai.models import Model

from .config import DEFAULT_MODEL_ANTHROPIC, DEFAULT_MODEL_OPENAI, DEFAULT_MODEL_OPENROUTER


def resolve_model() -> str | Model:
    """
    Resolve the default model based on environment variables.

    Args:
        None: Capability tags and other arguments are explicitly not supported.

    Returns:
        A model identifier string or a Model instance.

    Prioritizes:
    1. OpenRouter (OPENROUTER_API_KEY)
    2. Anthropic (ANTHROPIC_API_KEY)
    3. Default (OpenAI)
    """
    if os.getenv("OPENROUTER_API_KEY"):
        return os.getenv("DEFAULT_MODEL_OPENROUTER", DEFAULT_MODEL_OPENROUTER)

    if os.getenv("ANTHROPIC_API_KEY"):
        return os.getenv("DEFAULT_MODEL_ANTHROPIC", DEFAULT_MODEL_ANTHROPIC)

    if os.getenv("OPENAI_API_KEY"):
        return os.getenv("DEFAULT_MODEL_OPENAI", DEFAULT_MODEL_OPENAI)

    raise ValueError(
        "No LLM provider API keys found. "
        "Please set one of OPENROUTER_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY environment variables."
    )
