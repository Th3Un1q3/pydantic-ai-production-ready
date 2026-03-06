from collections.abc import Generator
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest


@pytest.fixture
def mock_dependencies() -> Generator[dict[str, Any], None, None]:
    with (
        patch("course_navigator.main.logfire") as mock_logfire,
        patch("course_navigator.main.create_agent") as mock_create_agent,
        patch("course_navigator.main.resolve_model") as mock_resolve,
        patch("course_navigator.main.asyncio") as mock_asyncio,
    ):
        mock_agent_instance = MagicMock(spec=["to_cli"])
        mock_agent_instance.to_cli = AsyncMock()
        mock_create_agent.return_value = mock_agent_instance
        mock_asyncio.run.side_effect = lambda coro: coro.close()

        yield {
            "logfire": mock_logfire,
            "create_agent": mock_create_agent,
            "agent_instance": mock_agent_instance,
            "resolve_model": mock_resolve,
            "asyncio": mock_asyncio,
        }


def test_main_cli_default_mode_uses_asyncio_run(mock_dependencies: dict[str, Any]) -> None:
    from course_navigator.main import main

    main()

    mock_dependencies["logfire"].configure.assert_called_once()
    mock_dependencies["logfire"].instrument_pydantic_ai.assert_called_once()
    mock_dependencies["create_agent"].assert_called_once()
    mock_dependencies["asyncio"].run.assert_called_once()
    mock_dependencies["agent_instance"].to_cli.assert_called_once()


def test_main_empty_argv_defaults_to_cli(mock_dependencies: dict[str, Any]) -> None:
    from course_navigator.main import main

    main([])

    mock_dependencies["asyncio"].run.assert_called_once()


def test_main_ui_mode_prints_placeholder(mock_dependencies: dict[str, Any]) -> None:
    from course_navigator.main import main

    _ = mock_dependencies

    with patch("course_navigator.main.print") as mock_print:
        main(["ui"])

    mock_print.assert_any_call("UI mode not yet implemented.")


def test_main_unknown_command_exits(mock_dependencies: dict[str, Any]) -> None:
    from course_navigator.main import main

    _ = mock_dependencies

    with (
        patch("course_navigator.main.print") as mock_print,
        patch("course_navigator.main.sys.exit") as mock_exit,
    ):
        main(["unknown"])

    mock_print.assert_any_call("Unknown command: LaunchMode.UNKNOWN")
    mock_exit.assert_called_once_with(1)


def test_main_handles_resolver_error(mock_dependencies: dict[str, Any]) -> None:
    from course_navigator.main import main

    mock_dependencies["resolve_model"].side_effect = ValueError("No keys")

    with patch("course_navigator.main.print") as mock_print:
        main([])

    mock_print.assert_called_once_with("Configuration Error: No keys")
    mock_dependencies["create_agent"].assert_not_called()
    mock_dependencies["asyncio"].run.assert_not_called()
