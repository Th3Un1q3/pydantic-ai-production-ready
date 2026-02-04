from collections.abc import Generator
from typing import Any
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_dependencies() -> Generator[dict[str, Any], None, None]:
    with (
        patch("course_navigator.main.logfire") as mock_logfire,
        patch("course_navigator.main.create_agent") as mock_create_agent,
        patch("course_navigator.main.resolve_model") as mock_resolve,
    ):

        # Setup Agent mock instance returned by create_agent
        mock_agent_instance = MagicMock()
        mock_create_agent.return_value = mock_agent_instance

        # Setup run_sync return value
        mock_result = MagicMock()
        mock_result.output = "Mock response"
        mock_agent_instance.run_sync.return_value = mock_result

        yield {
            "logfire": mock_logfire,
            "create_agent": mock_create_agent,
            "agent_instance": mock_agent_instance,
            "resolve_model": mock_resolve,
        }


def test_main_hello_world_zero(mock_dependencies: dict[str, Any]) -> None:
    """
    ZOMBIE: Zero.
    Test that main runs successfully with default mocked environment.
    """
    from course_navigator.main import main

    # Should not raise
    main()


def test_main_logfire_configured_one(mock_dependencies: dict[str, Any]) -> None:
    """
    ZOMBIE: One (Configuration).
    Test that logfire is configured and pydantic_ai instrumentation is enabled.
    """
    from course_navigator.main import main

    main()

    mock_dependencies["logfire"].configure.assert_called_once()
    mock_dependencies["logfire"].instrument_pydantic_ai.assert_called_once()


def test_main_creates_agent_interface(mock_dependencies: dict[str, Any]) -> None:
    """
    ZOMBIE: Interface.
    Test that create_agent is called with the resolved model.
    """
    from course_navigator.main import main

    mock_dependencies["resolve_model"].return_value = "openai:gpt-mock"

    main()

    # Check create_agent call
    mock_dependencies["create_agent"].assert_called_once_with("openai:gpt-mock")


def test_main_runs_sync_one(mock_dependencies: dict[str, Any]) -> None:
    """
    ZOMBIE: One (Execution).
    Test that agent.run_sync is called (not run) and usage is printed.
    """
    from course_navigator.main import main

    main()

    mock_dependencies["agent_instance"].run_sync.assert_called_once()
    # Verify usage was accessed/called
    mock_dependencies["agent_instance"].run_sync.return_value.usage.assert_called_once()


def test_main_resolver_exception_exceptions(mock_dependencies: dict[str, Any]) -> None:
    """
    ZOMBIE: Exceptions.
    Test behavior when resolver raises ValueError (e.g. no keys).
    Should catch error and return/print, not crash.
    """
    from course_navigator.main import main

    mock_dependencies["resolve_model"].side_effect = ValueError("No keys")

    # Should handle exception gracefully
    main()

    # Agent should NOT be initialized if resolution fails
    mock_dependencies["create_agent"].assert_not_called()


def test_main_agent_execution_error_exceptions(mock_dependencies: dict[str, Any]) -> None:
    """
    ZOMBIE: Exceptions.
    Test behavior when agent.run_sync raises an exception.
    """
    from course_navigator.main import main

    # Setup mock to raise exception on run_sync
    mock_dependencies["agent_instance"].run_sync.side_effect = Exception("API Error")

    # Should handle exception gracefully (print error)
    main()

    # Verify run_sync was called
    mock_dependencies["agent_instance"].run_sync.assert_called_once()
