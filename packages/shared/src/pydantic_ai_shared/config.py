"""
Shared configuration for all projects.
"""
import os

# Default model configurations
DEFAULT_MODEL_OPENAI = "openai:gpt-4"
DEFAULT_MODEL_ANTHROPIC = "anthropic:claude-3-5-sonnet-20241022"

# Get from environment or use defaults
def get_default_model(provider: str = "openai") -> str:
    """Get default model for a provider.
    
    Args:
        provider: Model provider ('openai' or 'anthropic')
        
    Returns:
        Model identifier string
    """
    env_var = f"DEFAULT_MODEL_{provider.upper()}"
    if provider == "openai":
        return os.getenv(env_var, DEFAULT_MODEL_OPENAI)
    elif provider == "anthropic":
        return os.getenv(env_var, DEFAULT_MODEL_ANTHROPIC)
    else:
        raise ValueError(f"Unknown provider: {provider}")
