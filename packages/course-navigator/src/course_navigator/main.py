import asyncio
import sys
from enum import Enum

import logfire
from pydantic_ai_shared.resolver import resolve_model

from course_navigator.agent import create_agent
from course_navigator.models import NavigatorDeps


def _configure_logging() -> None:
    """Configure Logfire and instrument Pydantic AI integrations."""
    logfire.configure(send_to_logfire="if-token-present")
    logfire.instrument_pydantic_ai()


class LaunchMode(Enum):
    CLI = "cli"
    UI = "ui"
    UNKNOWN = "unknown"


def _parse_launch_mode(argv: list[str] | None = None) -> LaunchMode:
    if argv is None or len(argv) == 0:
        return LaunchMode.CLI
    cmd = argv[0].lower()
    return LaunchMode(cmd) if cmd in (m.value for m in LaunchMode) else LaunchMode.UNKNOWN


def _build_agent_deps(argv: list[str] | None = None) -> NavigatorDeps:
    return NavigatorDeps(user_name="Student", difficulty="Beginner")


def main(argv: list[str] | None = None) -> None:
    _configure_logging()

    launch_mode = _parse_launch_mode(argv)

    try:
        model = resolve_model()
    except ValueError as exc:
        print(f"Configuration Error: {exc}")
        return

    deps = _build_agent_deps()

    agent = create_agent(model, deps)

    if launch_mode is LaunchMode.CLI:
        asyncio.run(agent.to_cli(deps=deps))
        return

    if launch_mode is LaunchMode.UI:
        print("UI mode not yet implemented.")
        return

    print(f"Unknown command: {launch_mode}")
    sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
