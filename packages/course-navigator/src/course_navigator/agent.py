from pydantic_ai import Agent
from pydantic_ai.models import Model


def create_agent(model: str | Model) -> Agent:
    """
    Factory function to create the Course Navigator agent.

    Args:
        model: The LLM model instance to use.

    Returns:
        Agent: A configured pydantic-ai Agent.
    """
    return Agent(
        model,
        system_prompt="You are a helpful agent.",
    )
