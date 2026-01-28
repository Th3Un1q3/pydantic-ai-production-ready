---
name: project-navigator
description: Guide for navigating the project structure, understanding the monorepo architecture, and using the `just` command runner to manage packages and workflows. Use this skill when the user asks about the project layout, how to add new packages, or how to run/test existing components.
---

# Project Navigator

This skill consolidates knowledge about the repository's structure, architecture, and tooling. Use it to understand where things are, how the monorepo works, and how to perform common tasks like adding or running packages.

## 1. Project Structure

The repository follows a clear structure for a production-ready AI monorepo:

- **Root**: Configuration files (`pyproject.toml`, `justfile`) and documentation.
- **`packages/`**: The core of the monorepo. Contains independent Python projects managed by `uv`.
  - **`shared/`**: Common utilities and config (e.g., `packages/shared`).
  - **`[agent-name]/`**: Specific agent implementations (e.g., `packages/internal-support-agent`).
- **`learning/`**: Educational content and modules.
- **`.devcontainer/`**: Docker and VS Code environment configuration.
- **`scripts/`**: Helper scripts.

### Key Concepts

- **Monorepo with `uv`**: The project uses `uv` workspaces. The root `pyproject.toml` defines the workspace members.
- **`just` Command Runner**: All tasks (install, test, run) are standardized using `just`.

## 2. Command System (`just`)

The project uses `just` as a unified interface for all operations. Do not run `uv` commands manually if a `just` command exists.

### Common Commands

- **Initialize**: `just init` (Installs all dependencies)
- **Start**: `just start [package]` (e.g., `just start support`)
- **Test**: `just test [package]` (e.g., `just test shared` or just `just test` for all)
- **Install**: `just install [package]` (e.g., `just install corporate`)
- **Check**: `just check [package]` (Runs format, lint, typecheck, and test)

**Note**: Package names often have aliases (e.g., `internal-support-agent` -> `support`).

## 3. Workflow: Creating a New Package

To add a new agent or package to the monorepo:

1. **Create Directory Structure**:

    ```bash
    mkdir -p packages/my-new-package/src packages/my-new-package/tests
    ```

2. **Create `pyproject.toml`**:
    Add the package-specific configuration in `packages/my-new-package/pyproject.toml`.

3. **Create `justfile`**:
    Create `packages/my-new-package/justfile` with standard commands:

    ```just
    start:
        uv run python src/main.py

    test:
        uv run pytest
    ```

4. **Register in Workspace**:
    Edit the root `pyproject.toml` to add the new package to `tool.uv.workspace.members`.

    ```toml
    [tool.uv.workspace]
    members = [
        # ... existing members
        "packages/my-new-package",
    ]
    ```

5. **Update Root `justfile`**:
    Add logic to the root `justfile` to handle the new package name in `install`, `start`, and `test` commands.

6. **Initialize**:
    Run `just init` or `just install my-new-package` to set up dependencies.

## 4. Package Architecture

- **`shared` Package**: Contains core utilities, configuration (`config.py`), and shared logic. Most other packages should depend on this.
- **Dependency Management**:
  - **Shared**: Define common dev dependencies in the root `pyproject.toml`.
  - **Specific**: Define runtime dependencies in each package's `pyproject.toml`.
- **Environment Variables**: Managed via `.env` file (not committed) and loaded via `shared.config`.

## 5. Learning Materials

The `learning/` directory contains progressive modules (`01-fundamentals`, etc.). Use the `learning-structure` skill (if available) to manage these, but be aware they exist as a parallel resource to the code in `packages/`.
