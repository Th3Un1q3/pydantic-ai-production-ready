---
description: 'Canonical just workflows, package aliases, and the no-raw-CLI-tools operational policy.'
applyTo: '**'
excludeAgent: 'orchestrator'
---

# Command Execution and Lifecycle Policy

Guidelines for executing tasks, managing dependencies, and maintaining operational consistency across the monorepo using `just`.

## General Principles

- **Single Interface**: `just` is the ONLY entry point for all development, build, and test operations.
- **Encapsulation**: Raw CLI tools (like `npm`, `python`, `pytest`, `uv`, `ruff`) MUST be wrapped in `just` recipes.
- **No Raw CLI Policy**: NEVER run tools like `pip install`, `pytest`, `black`, or `ruff` directly in the terminal. Use the corresponding `just` recipe to ensure the correct environment and flags are used.
- **Reproducibility**: Commands must behave identically in the dev container and CI environment.

## Canonical Workflows

In all commands below, `<package>` is the **directory name** of the package under `packages/` (e.g., `course-navigator`, `shared`). Use `just packages` when you need to enumerate them.

### 1. Environment Initialization
- `just init`: Complete first-time setup (creates `.env`, syncs dependencies, opens key files).
- `just install`: Sync dependencies across all workspace members (wraps `uv sync`).

### 2. Development Lifecycle
- `just start <package>`: Launch a specific agent or service (e.g., `just start course-navigator`).
- `just check <package>`: Comprehensive validation (format + lint + typecheck + test). Use this before committing.
- `just fix <package>`: Automatically correct formatting and linting violations.
- `just packages`: List all available packages (use this to find the correct directory name for other commands).
- `just tree`: Display the package directory structure.
- `just info`: Show environment details (Python version, `uv` version, workspace status).

### 3. Testing and Quality
- `just test [package]`: Run the test suite for a specific package or the entire workspace (`all`).
- `just lint`: Check the entire repository or a specific package for linting errors.
- `just format`: Format the code using project-standard tools (Black).
- `just typecheck`: Run static type analysis (Mypy).
- `just lint-md`: Lint and auto-fix Markdown files.

## Operational Policies

- **Auditable Commands**: If a sequence of commands is likely to be repeated, codify it as a `just` recipe in the `justfile`.
- **Background Tasks**: Long-running processes (e.g., servers, watch modes) must be managed through `just` to ensure proper environment loading.
- **Environment Awareness**: `just` recipes automatically load environment variables from `.env` in the root.
- **Automation-First Remediation**: When checks fail, run available auto-fix commands first before manual edits. Use `just fix <package>` for package formatting/lint issues, and run `just lint-md` when the failures involve Markdown files.
- **Manual-Fallback Handoff**: If auto-fix does not fully resolve issues (especially formatting/markup edge cases), provide an explicit manual-fix handoff rather than silently stopping.
- **Unresolved Issue Reporting Template**: For each remaining issue, report: `file`, `issue`, `why auto-fix failed`, `manual action required`.
- **Proactive Quality Gate**: After completing any code-changing task (new files, refactors, edits), you MUST run `just check <package>` — not merely `just test <package>`. Passing tests does not mean the code is clean: `just check` validates format, lint, typecheck, and tests in a single pass, and type errors or linting violations will not surface from `just test` alone.

## Troubleshooting

- **Dependency Inconsistency**: If imports fail or tools behave unexpectedly, run `just install` to synchronize the `uv` lockfile.
- **`just: command not found`**: Ensure `just` is installed and on your PATH.
- **Command Discovery**: Run `just` (or `just --list`) to list all available commands and their descriptions.

## Cross-References

- See [monorepo.instructions.md](monorepo.instructions.md) for repository structure and package boundaries.
- See [python.instructions.md](python.instructions.md) for Python-specific runtime guidance.
