---
description: 'Coding rules, organization standards, and architectural guidelines for Python development in the monorepo.'
applyTo: '**/*.py'
---

# Python Coding Standards and Organization

This document defines the coding standards and architectural principles for Python development within this monorepo.

## Architecture & Organization

- **Monorepo Structure**: Follow the guidelines in [.github/instructions/monorepo.instructions.md](.github/instructions/monorepo.instructions.md) for workspace boundaries, `shared` package usage, and project relationships.
- **Imports**: Use absolute imports for external packages. Import shared code via `pydantic_ai_shared` as defined in the monorepo standards.
  - Example: `from pydantic_ai_shared.config import get_default_model`

## Coding Conventions

- **Typing**: Use Python 3.12+ features.
- **Domain-Specific Naming**: Names must reveal domain and intent, not structural pattern. `build_course_answer()` communicates more than `answer_factory()`; `validate_enrollment_deadline()` communicates more than `validate()`. Apply this to all variables, functions, classes, and modules — including test helpers, utilities, and internal abstractions. Generic suffixes like `_factory`, `_helper`, `_util`, `_manager`, or `_handler` MUST be qualified with a domain noun.
- **Structured I/O**: Use `pydantic.BaseModel` for all structured input and output.
- **Framework**: Use `pydantic-ai` for all agent implementations.
- **Agent Pattern**: Agents are classes wrapping `pydantic_ai.Agent`.
- **Async**: Prefer `asyncio` for all I/O operations.

## Mandatory API Verification

**STOP AND VERIFY**: Before implementing any code that interacts with an external library (e.g., `pydantic-ai`, `logfire`):

1. **Query Documentation**: Use `mcp_context7_query-docs` to get exact method signatures and return types.
2. **Verify Attributes**: Do not "guess" attribute names (e.g., `.data` vs `.output`). **You must see the attribute in the documentation output or code snippet.**
3. **No "Dreamed" APIs**: If you cannot verify the API, do not write the code. Ask the user for clarification or search again.

## Environment & Configuration

- Use `dotenv` for loading environment variables.
- Check `.env.example` in package roots for required variables.
- **Lifecycle Ops**: Use `just` for all tasks. See [.github/instructions/command-execution.instructions.md](.github/instructions/command-execution.instructions.md) for the operational policy.

## Quality Standards

- **TDD Requirement**: All Python development MUST follow the [.github/instructions/test-implementation.instructions.md](.github/instructions/test-implementation.instructions.md).
- **Type Checking**: Run `just check` frequently to catch type errors immediately.
