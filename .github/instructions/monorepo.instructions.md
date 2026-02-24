---
description: 'Navigation, workspace boundaries, project relationships, and package development rules for the monorepo.'
applyTo: '**'
---

# Monorepo Architecture and Navigation

Guidelines for navigating the repository structure, understanding workspace boundaries, and maintaining the project architecture.

## Repository Structure Source of Truth

This file is the canonical source for repository and package structure rules.

- Do not duplicate global directory trees in other docs unless they are scoped to a single subdirectory (for example `specs/README.md` describing only `specs/`).
- When another document needs structure context, reference this file instead of copying folder trees.
- If structure changes, update this file first, then update links in dependent docs.

## Canonical Repository Layout

The repository is a `uv`-managed Python monorepo organized for clarity and isolation:

- **Root**: Global configuration (`pyproject.toml`, `justfile`), [specs/](../../specs/), and top-level documentation.
- **[packages/](../../packages/)**: Core application logic.
   - **[packages/shared/](../../packages/shared/)**: Common utilities, shared models, and base configurations (`pydantic-ai-shared`).
   - **`packages/[package-name]/`**: Domain-specific feature packages (for example `course-navigator`) with independent `src/` and `tests/`.
- **[learning/](../../learning/)**: Educational content and modules.
- **[specs/](../../specs/)**: Architecture decisions and implementation plans.
- **[.devcontainer/](../../.devcontainer/)**: Deterministic VS Code development environment.
- **[scripts/](../../scripts/)**: Administrative and automation scripts.

## Workspace Boundaries

- **`uv` Workspaces**: The repository uses `uv` workspaces. The root `pyproject.toml` defines the entire workspace. All packages share a single lockfile (`uv.lock`) at the root.
- **Self-Containment**: Each package in [packages/](../../packages/) MUST be self-contained. Internal logic should be inside the package's `src/` directory.
- **Shared Code**: Logic intended for reuse across multiple packages MUST reside in [packages/shared/](../../packages/shared/). Import it via `pydantic_ai_shared`.

## Project Relationships

- **Dependency Flow**: Feature packages may depend on `shared`. `shared` MUST NEVER depend on feature packages.
- **Isolation**: Packages should communicate via well-defined interfaces or shared data models. Avoid circular dependencies between packages.
- **Environment Variables**: Managed via a root [.env](.env) file (copied from `.env.example` during `just init`) and loaded via `pydantic_ai_shared`.

## Package Creation Ritual

When adding a new package to the monorepo, follow these steps:

1. **Directory Structure**:
   - Create `packages/[name]/src/[snake_case_name]` and `packages/[name]/tests`.
   - Ensure an `__init__.py` exists in the source directory.
2. **`pyproject.toml`**:
   - Define `name`, `version`, and `dependencies`.
   - MUST include `pydantic-ai-shared` as a dependency for any agent package.
   - Use `hatchling` as the build backend.
   - Configure `tool.hatchling.build.targets.wheel` to include `src/[snake_case_name]`.
3. **Registration**: Add the path to `tool.uv.workspace.members` in the root [pyproject.toml](../../pyproject.toml).
4. **Local `justfile`**: Create a package `justfile` that imports the root structure or defines local lifecycle tasks (e.g., `start`, `test`).
5. **Synchronization**: Run `just install` to update the workspace lockfile.
6. **Validation**: Verify the new package with `just check [name]`.

## Code Organization Standards

- **Absolute Imports**: Always use absolute imports for external and internal packages.
- **Source Layout**: Adhere to the `src/` layout (e.g., `src/[package_name]/...`) for all Python packages to ensure clean distribution and testing.
- **Specifications First**: Significant structural changes or new packages MUST have a corresponding specification in [specs/](../../specs/) before implementation.

## Structure Maintenance Rules

- Treat this file as SSOT for global repository layout.
- Keep examples representative and minimal; avoid exhaustive generated trees.
- Prefer stable path patterns (`packages/[name]/src/[snake_case_name]`) over volatile package lists.
- If a package is added/renamed/removed, verify references in [README.md](../../README.md), [ARCHITECTURE.md](../../ARCHITECTURE.md), and [packages/README.md](../../packages/README.md).

## Scoped Structure Docs (Allowed)

The following docs may describe their own local subtree only:

- [packages/README.md](../../packages/README.md) for package-level orientation
- [specs/README.md](../../specs/README.md) for specification folder conventions
- [learning/README.md](../../learning/README.md) for learning module organization

These files must reference this instruction file for global repository structure.

## Cross-References

- See [command-execution.instructions.md](command-execution.instructions.md) for task runner details.
- See [python.instructions.md](python.instructions.md) for coding standards.
