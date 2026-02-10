Strictly follow instructions on operational eficency and best practices when performing any tasks on this repository.


# Operational Efficency

- **Decompose complex tasks** into smaller, manageable subtasks to enhance clarity and maintainability use `agent/runSubagent` tools to delegate subtasks.
- **Proactively load agentic skills** based on the context of the user's request to provide accurate and efficient assistance. Aim to load at least 1(the more the better) relevant skill for each user query.

# Best Practices

- **Single Source of Truth**: When considering add a new file/change existing one always make sure if there is other file that already contains the information. If you found such duplication consider if creation of a new file serves a purpose and re-distribute the information accordingly.

# Automation & Reproducibility

- **Codify Reusable Commands**: When a new script or complex command sequence is introduced and likely to be reused, encapsulate it as a `just` command. This ensures auditability and ease of use.
- **Persist Environment Configuration**: If a configuration change is "global" or part of the default setup (e.g., git config, package installation), modify the `.devcontainer` configuration (e.g., `post-create.sh` or `Dockerfile`) to ensure reproducibility for all users.

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

## Reliable Execution and Task Decomposition

### Subtask Decomposition

Break complex workflows into discrete phases:
- Use `agent/runSubagent` for parallel or specialized work
- Each subtask should have clear inputs and outputs
- Validate results before proceeding to next phase

### Progress Tracking: `todos` vs File-Based Checklists

#### When to Use `todos` Tool

Use `todos` for **autonomous multi-step tasks** where the agent works without user interruption:

**Good use cases:**
- TDD cycle steps (write test → validate fails → implement → validate passes → refactor)
- Build/lint/test validation sequences
- Multi-file refactoring operations
- Sequential code generation steps

**Example - TDD Cycle:**
```markdown
Use `todos` to track the TDD cycle:
1. Write failing test for the feature
2. Run test, confirm it fails for the expected reason
3. Write minimal implementation to pass
4. Run test, confirm it passes
5. Refactor implementation while keeping tests green
6. Move to next priority
```

#### When to Use File-Based Checklists

Use **file-based checklists** for tracking that must persist across sessions or involves human-in-the-loop:

**Good use cases:**
- Discovery phases requiring user input
- Deliverables tracking across multiple sessions
- Specification progress (stored in the spec file itself)
- Any workflow where user interruption is expected

**Example - Discovery in Specification File:**
```markdown
## Specification Progress
- [x] Complete discovery phase
- [ ] Determine specification type
- [ ] Draft specification from template
- [ ] Validate against quality standards

## Discovery Notes
(Answers captured here persist across sessions)
```

#### Decision Matrix

| Scenario | Use `todos` | Use File-Based |
|----------|-------------|----------------|
| Agent works autonomously | ✓ | |
| User may interrupt/resume | | ✓ |
| TDD cycle within a session | ✓ | |
| Tracking deliverables over time | | ✓ |
| Build/test sequences | ✓ | |
| Discovery with user Q&A | | ✓ |
