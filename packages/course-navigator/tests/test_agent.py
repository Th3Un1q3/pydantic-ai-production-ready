from unittest.mock import Mock, patch

from course_navigator.agent import create_agent
from course_navigator.models import CourseAnswer, NavigatorDeps
from course_navigator.tools import read_lesson
from pydantic_ai.models import Model


def test_create_agent_configures_prompt_and_tools() -> None:
    mock_model = Mock(spec=Model)
    deps = NavigatorDeps(
        user_name="Student",
        difficulty="Beginner",
    )

    with (
        patch("course_navigator.agent.Agent") as MockAgent,
        patch("course_navigator.agent.build_index", return_value="INDEX") as mock_build_index,
        patch(
            "course_navigator.agent.get_indexed_paths", return_value={"lesson.md"}
        ) as mock_indexed_paths,
        patch("course_navigator.agent.set_allowed_paths") as mock_set_allowed_paths,
    ):
        create_agent(mock_model, deps)

        mock_build_index.assert_called_once()
        mock_indexed_paths.assert_called_once()
        mock_set_allowed_paths.assert_called_once_with({"lesson.md"})

        MockAgent.assert_called_once()
        args, kwargs = MockAgent.call_args
        assert args[0] == mock_model
        assert kwargs.get("deps_type") is NavigatorDeps
        assert kwargs.get("output_type") is CourseAnswer
        assert kwargs.get("tools") == [read_lesson]
        assert kwargs.get("system_prompt") is None

        system_prompt_factory = MockAgent.return_value.system_prompt.call_args[0][0]
        assert callable(system_prompt_factory)
        ctx = Mock()
        ctx.deps = deps
        prompt = system_prompt_factory(ctx)
        assert "INDEX" in prompt
        assert deps.user_name in prompt
        assert deps.difficulty in prompt
