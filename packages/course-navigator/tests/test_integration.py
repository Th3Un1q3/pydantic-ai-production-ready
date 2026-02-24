import pytest
from course_navigator.agent import create_agent
from course_navigator.models import CourseAnswer
from course_navigator.tests.factories import build_course_answer, build_navigator_deps
from pydantic_ai import ModelMessage, ModelResponse, ToolCallPart, UsageLimits, models
from pydantic_ai.models.function import AgentInfo, FunctionModel

# the factory module can generate both deps and answers.  the
# model implementation below captures a single expected answer via
# closure so that the test asserts against non‑constant values.


# note: we deliberately declare the model function inside the test
# rather than at module level. keeping it local avoids accidental
# reuse and makes the dependency on ``expected`` explicit.


@pytest.mark.asyncio
async def test_agent_runs_with_test_model() -> None:
    models.ALLOW_MODEL_REQUESTS = False

    deps = build_navigator_deps()

    # choose an expected answer and build a model that always returns it
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
