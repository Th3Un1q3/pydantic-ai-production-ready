import pytest
from course_navigator.agent import create_agent
from course_navigator.models import CourseAnswer, NavigatorDeps
from pydantic_ai import ModelMessage, ModelResponse, ToolCallPart, UsageLimits, models
from pydantic_ai.models.function import AgentInfo, FunctionModel


async def _model_function(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
    output_tool = info.output_tools[0]
    return ModelResponse(
        parts=[
            ToolCallPart(
                output_tool.name,
                {
                    "summary": "Test summary",
                    "references": [{"path": "lesson.md", "title": "Lesson"}],
                },
            )
        ]
    )


@pytest.mark.asyncio
async def test_agent_runs_with_test_model() -> None:
    models.ALLOW_MODEL_REQUESTS = False

    deps = NavigatorDeps(
        user_name="Student",
        difficulty="Beginner",
    )
    model = FunctionModel(_model_function)

    agent = create_agent(model, deps)
    result = await agent.run(
        "Summarize the lesson",
        deps=deps,
        usage_limits=UsageLimits(request_limit=1),
    )

    assert isinstance(result.output, CourseAnswer)
    assert result.output.summary == "Test summary"
