from unittest.mock import Mock, patch

from course_navigator.agent import create_agent
from pydantic_ai import Agent
from pydantic_ai.models import Model


def test_create_agent_one() -> None:
    """
    ZOMBIE: One/Interface.
    Test that create_agent returns an Agent with the correct configuration.
    """
    # Create a mock that passes isinstance(x, Model) check
    mock_model = Mock(spec=Model)

    agent = create_agent(mock_model)

    assert isinstance(agent, Agent)
    assert agent.model is mock_model


def test_create_agent_uses_correct_prompt() -> None:
    """
    Verify the specific system prompt is used.
    """
    mock_model = Mock(spec=Model)

    with patch("course_navigator.agent.Agent") as MockAgent:
        create_agent(mock_model)

        MockAgent.assert_called_once()
        args, kwargs = MockAgent.call_args
        assert args[0] == mock_model
        assert kwargs.get("system_prompt") == "You are a helpful agent."
