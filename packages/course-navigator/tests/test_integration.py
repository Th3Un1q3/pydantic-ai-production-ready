import pytest
from course_navigator.agent import create_agent
from course_navigator.models import CourseAnswer
from course_navigator.tests.factories import build_course_answer, build_navigator_deps
from pydantic_ai import ModelMessage, ModelResponse, ToolCallPart, UsageLimits, models
from pydantic_ai.models.function import AgentInfo, FunctionModel


@pytest.mark.asyncio
async def test_create_agent_run_returns_course_answer_from_function_model() -> None:
    models.ALLOW_MODEL_REQUESTS = False

    deps = build_navigator_deps()
    expected = build_course_answer()

    def _model_function(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        output_tool = info.output_tools[0]
        return ModelResponse(
            parts=[
                ToolCallPart(
                    output_tool.name,
                    {"summary": expected.summary, "references": expected.references},
                )
            ]
        )

    model = FunctionModel(_model_function)

    agent = create_agent(model, deps)
    result = await agent.run(
        "Summarize the lesson",
        deps=deps,
        usage_limits=UsageLimits(request_limit=1),
    )

    assert isinstance(result.output, CourseAnswer)
    assert result.output.summary == expected.summary
    assert result.output.references == expected.references
