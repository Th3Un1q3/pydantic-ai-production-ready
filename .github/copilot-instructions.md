Strictly follow instructions on operational eficency and best practices when performing any tasks on this repository.


# Operational Efficency

- **Decompose complex tasks** into smaller, manageable subtasks to enhance clarity and maintainability use `agent/runSubagent` tools to delegate subtasks.
- **Proactively load agentic skills** based on the context of the user's request to provide accurate and efficient assistance. Aim to load at least 1(the more the better) relevant skill for each user query.

# Best Practices

- **Single Source of Truth**: When considering add a new file/change existing one always make sure if there is other file that already contains the information. If you found such duplication consider if creation of a new file serves a purpose and re-distribute the information accordingly.

# Pydantic AI Monorepo Guidelines

## Architecture & Organization
- **Monorepo Structure**: This is a `uv`-managed Python monorepo.
  - Root `pyproject.toml` defines the workspace.
  - Projects live in `packages/<project-name>`.
  - Shared code lives in `packages/shared` (package name: `pydantic-ai-shared`).
- **Service Boundaries**: Each package in `packages/` is a self-contained project with its own `src/` and `tests/`.
- **Imports**: Use absolute imports for external packages. Import shared code via `pydantic_ai_shared`.
  - Example: `from pydantic_ai_shared.config import get_default_model`

## Development Workflow
- **Command Runner**: Use `just` for all lifecycle tasks. Do not run raw `python` or `pytest` commands if a `just` recipe exists.
  - Install/Sync: `just install` (wraps `uv sync`)
  - Run Project: `just start <package_name>`
    - aliases: `navigator` -> `course-navigator`
  - Test: `just test <package_name>` or `just test` (all)
  - Format/Lint: `just format`, `just lint`
- **Dependency Management**:
  - Add dependencies via `uv add --package <package_name> <dependency>`.
  - All projects share a lockfile at the root.

## Coding Conventions
- **Framework**: Use `pydantic-ai` for all agent implementations.
- **Pattern**: Agents are classes wrapping `pydantic_ai.Agent`.
  - See [packages/course-navigator/src/course_navigator/agent.py](packages/course-navigator/src/course_navigator/agent.py) for the reference implementation.
- **Typing**: Python 3.12+ features. Use `pydantic.BaseModel` for structured I/O.
- **Async**: Prefer `asyncio` for I/O operations.

## Environment & Integration
- **Apps**: `course-navigator` (single agent).
- **Configuration**: Environment variables loaded via `dotenv`. Check `.env.example`.

## Spec-Based Development

For significant changes, use the specification-driven workflow:

1. **Create Specification**: Use `/write-spec` or the `spec-writer` skill
   - Discovery phase gathers requirements
   - Produces structured spec in `specs/{type}/SPEC-{id}-{title}.md`

2. **Implement Specification**: Use `/implement-spec` or the `spec-implementer` skill
   - Phased implementation with validation gates
   - TDD workflow for Python code
   - Automatic documentation updates

### Specification Types
| Type | Use For | Location |
|------|---------|----------|
| `feature` | New functionality | `specs/features/` |
| `package` | New packages | `specs/packages/` |
| `learning` | Educational content | `specs/learning/` |
| `change` | Refactoring | `specs/changes/` |

### Prompts
- `/write-spec` - Invoke to create a new specification
- `/implement-spec` - Invoke to execute a specification file
