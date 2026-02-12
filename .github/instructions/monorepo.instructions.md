---
description: 'Navigation, workspace boundaries, project relationships, and package development rules for the monorepo.'
applyTo: '**'
---

# Monorepo Architecture and Navigation

Guidelines for navigating the repository structure, understanding workspace boundaries, and maintaining the project architecture.

## Repository Structure

The repository is a `uv`-managed Python monorepo organized for clarity and isolation:

- **Root**: Global configuration (`pyproject.toml`, `justfile`), [specs/](specs/), and top-level documentation.
- **[packages/](packages/)**: The core application logic.
  - **[packages/shared](packages/shared)**: Common utilities, shared models, and base configurations (`pydantic-ai-shared`).
  - **`[package-name]/`**: Domain-specific feature packages (e.g., `course-navigator`). Each resides in its own folder with independent `src/` and `tests/`.
- **[learning/](learning/)**: Educational content and modules designed as a parallel resource to the codebase.
- **[specs/](specs/)**: Documentation for architecturally significant decisions and implementation plans.
- **[.devcontainer/](.devcontainer/)**: Deterministic development environment configuration for VS Code.
- **[scripts/](scripts/)**: Administrative and automation scripts.

## Workspace Boundaries

- **`uv` Workspaces**: The repository uses `uv` workspaces. The root `pyproject.toml` defines the entire workspace. All packages share a single lockfile (`uv.lock`) at the root.
- **Self-Containment**: Each package in [packages/](packages/) MUST be self-contained. Internal logic should be inside the package's `src/` directory.
- **Shared Code**: Logic intended for reuse across multiple packages MUST reside in [packages/shared](packages/shared). Import it via `pydantic_ai_shared`.

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
3. **Registration**: Add the path to `tool.uv.workspace.members` in the root [pyproject.toml](pyproject.toml).
4. **Local `justfile`**: Create a [justfile](justfile) in the package directory that imports the root structure or defines local lifecycle tasks (e.g., `start`, `test`).
5. **Synchronization**: Run `just install` to update the workspace lockfile.
6. **Validation**: Verify the new package with `just check [name]`.

## Code Organization Standards

- **Absolute Imports**: Always use absolute imports for external and internal packages.
- **Source Layout**: Adhere to the `src/` layout (e.g., `src/[package_name]/...`) for all Python packages to ensure clean distribution and testing.
- **Specifications First**: Significant structural changes or new packages MUST have a corresponding specification in [specs/](specs/) before implementation.

## Cross-References

- See [command-execution.instructions.md](command-execution.instructions.md) for task runner details.
- See [python.instructions.md](python.instructions.md) for coding standards.
