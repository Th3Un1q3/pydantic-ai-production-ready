from pydantic_ai import Agent, RunContext
from pydantic_ai.models import Model
from pydantic_ai_shared.config import LEARNING_ROOT

from course_navigator.models import CourseAnswer, NavigatorDeps
from course_navigator.tools import read_lesson, set_allowed_paths
from course_navigator.utils import build_index, get_indexed_paths


def create_agent(model: str | Model, deps: NavigatorDeps) -> Agent[NavigatorDeps, CourseAnswer]:
    """
    Factory function to create the Course Navigator agent.

    Args:
        model: The LLM model instance to use.
        deps: Dependencies for personalization and configuration.

    Returns:
        Agent: A configured pydantic-ai Agent.
    """
    index = build_index(LEARNING_ROOT)
    set_allowed_paths(get_indexed_paths(LEARNING_ROOT))

    agent: Agent[NavigatorDeps, CourseAnswer] = Agent(
        model,
        deps_type=NavigatorDeps,
        output_type=CourseAnswer,
        tools=[read_lesson],
    )

    @agent.system_prompt
    def dynamic_system_prompt(ctx: RunContext[NavigatorDeps]) -> str:
        return (
            "You are a helpful course navigator agent.\n\n"
            f"User: {ctx.deps.user_name}\n"
            f"Difficulty Level: {ctx.deps.difficulty}\n\n"
            "Available Learning Materials:\n"
            f"{index}\n\n"
            "Use the read_lesson tool to access full content when needed.\n"
            "Only use file paths listed in the Available Learning Materials."
        )

    return agent
