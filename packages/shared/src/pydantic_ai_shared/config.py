"""
Shared configuration for all projects.
"""

from pathlib import Path

# Default model configurations
DEFAULT_MODEL_OPENAI = "openai:gpt-4"
DEFAULT_MODEL_ANTHROPIC = "anthropic:claude-3-5-sonnet-20241022"
DEFAULT_MODEL_OPENROUTER = "openrouter:openai/gpt-4o"

LEARNING_ROOT = Path(__file__).resolve().parents[4] / "learning"
