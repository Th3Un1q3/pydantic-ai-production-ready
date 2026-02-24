Strictly follow instructions on operational eficency and best practices when performing any tasks on this repository.


# Operational Efficency

- **Decompose complex tasks** into smaller, manageable subtasks to enhance clarity and maintainability use `agent/runSubagent` tools to delegate subtasks.
- **Instruction-First Composition**: Use modular instruction files in `.github/instructions/` as the primary source of guidance. Load modules dynamically based on task context and file types.
- **Precedence & Conflict Resolution**: Resolve overlap by precedence:
  1. `monorepo` (Policy & Boundaries)
  2. `command-execution` (Operational Rules)
  3. `test-implementation` (Process Gates)
  4. `python-tests` (Test Mechanics)
  5. `python` (Code Style/Structure)
  Higher precedence modules own the normative rules in case of overlap. If duplication is discovered, keep one canonical rule and replace duplicates with cross-references.

# Best Practices

- **Single Source of Truth**: When considering add a new file/change existing one always make sure if there is other file that already contains the information. If you found such duplication consider if creation of a new file serves a purpose and re-distribute the information accordingly.
- **Codify Reusable Commands**: When a new script or complex command sequence is introduced and likely to be reused, encapsulate it as a `just` command. This ensures auditability and ease of use.
- **Never Call CLI Tools Directly**: Always wrap CLI tool invocations in `just` commands. Do not run `npm`, `python`, `pytest`, or other tools directly - use the appropriate `just` recipe instead.
- **Environment Configuration**: As you always operate in dev container, follow the [dev container configuration guidelines](.github/instructions/devcontainer.instructions.md) when adding new software, packages, tools, or modifying existing ones. These instructions ensure maintainable, modular, and performant dev container setups by routing changes to the appropriate files (devcontainer.json, Dockerfile, or post-create.sh). Never install or configure software manually without updating the dev container configuration.

# Pydantic AI Monorepo Guidelines

## Architecture & Organization
- **Monorepo Structure**: Use `.github/instructions/monorepo.instructions.md` as the canonical source for repository layout and package boundaries.
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

1. **Create Specification**: Use `/write-spec` or the [spec-writing](.github/instructions/spec-writing.instructions.md) instruction module.
   - Discovery phase gathers requirements
   - Produces structured spec in `specs/{type}/SPEC-{id}-{title}.md`

2. **Implement Specification**: Use `/implement-spec` or the [spec-navigating](.github/instructions/spec-navigating.instructions.md) and [spec-implementation](.github/instructions/spec-implementation.instructions.md) instruction modules.
   - Phased implementation with validation gates
   - TDD workflow for Python code
   - Automatic documentation updates

### Specification Types
| Type       | Use For             | Location          |
| ---------- | ------------------- | ----------------- |
| `feature`  | New functionality   | `specs/features/` |
| `package`  | New packages        | `specs/packages/` |
| `learning` | Educational content | `specs/learning/` |
| `change`   | Refactoring         | `specs/changes/`  |

### Prompts
- `/write-spec` - Invoke to create a new specification
- `/implement-spec` - Invoke to execute a specification file

## Reliable Execution and Task Decomposition

### Instruction Module Composition

The assistant uses instruction modules as the primary behavior source. These modules compose based on the context of the task.

| Trigger                    | Modules to Load                                        |
| -------------------------- | ------------------------------------------------------ |
| **Any task**               | `monorepo`, `command-execution`, `tasks-decomposition` |
| **Python code changes**    | `python` (default), `api-verification` (if external)   |
| **Behavioral changes**     | `test-implementation` (adds TDD process)                |
| **Adding/Editing tests**   | `python-tests`                                         |
| **Implementing a Spec**    | `spec-navigating`, `spec-implementation`               |
| **Writing/Updating Spec**  | `spec-writing`                                         |
| **Modifying instructions** | `instruction-authoring`                                |
| **Updating `/learning`**   | `learning-operations`                                  |

### Instruction Module Catalog

This catalog is the source of truth for module responsibilities. Every module maps 1:1 to a file in `.github/instructions/`.

| Name                  | Responsibility                                                                  | Scope                                                                                                                                                                                                                         | Source From            |
| --------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `python`              | Define Python coding rules and code organization standards for the monorepo     | Typing conventions, async preferences, package/module structure, code style guidelines                                                                                                                                        | `python-development`   |
| `monorepo`            | Guide repository navigation, workspace boundaries, and project relationships. | Workspace/package boundaries, shared package usage, package membership                                                                                                                                                        | `monorepo-maintainer`  |
| `test-implementation` | Provide guidance on TDD process (Red-Green-Refactor) and behavioral coverage.  | Red-green-refactor gates, ZOMBIE checklist, process flow                                                                                                                                                                      | `python-development`   |
| `python-tests`        | Define Python test craftsmanship using pytest.                                 | Fixtures, parametrization, assertions, mocking practices                                                                                                                                                                      | `python-development`   |
| `command-execution`   | Define canonical just workflows and package aliases.                          | just recipe usage, alias resolution, no-raw-CLI policy                                                                                                                                                                        | `command-runner`       |
| `api-verification`    | Enforce mandatory library/API verification before implementation.              | Doc lookup workflow, interface verification gates, non-guessing rule                                                                                                                                                          | `python-development`   |
| `spec-writing`        | Guidance on writing specifications (discovery, templates, validation).         | Discovery phase, template selection, quality requirements                                                                                                                                                                     | `spec-writer`          |
| `spec-navigating`     | Guide reading and validating specs before coding.                              | Story interpretation, dependency mapping, validation checklist                                                                                                                                                                | `spec-implementer`     |
| `spec-implementation` | Guide implementing specs with checkpoints and status transitions.              | Phase gates, validation checkpoints, status transitions                                                                                                                                                                       | `spec-implementer`     |
| `tasks-decomposition` | Guide breaking down multi-step work and subagent usage.                        | Subagent usage, [P] parallelization, progress tracking policy                                                                                                                                                                 | `spec-implementer`     |
| `learning-operations` | Guide learning content operations and maintenance.                             | Scaffold/validate /learning, cross-linking, sync checks                                                                                                                                                                       | `learning-ops`         |
| `instruction-authoring`| Guide creating and maintaining instruction modules.                            | Modular ownership, progressive disclosure, anti-duplication                                                                                                                                                                   | `skill-creator`        |

### Migration Status (SPEC-004)

The SPEC-004 transformation is **Completed**.

- **Completed**: All migration waves (Wave 0 - Wave 4). The guidance system is now 100% modular instruction-first. Legacy skills have been retired and removed.
