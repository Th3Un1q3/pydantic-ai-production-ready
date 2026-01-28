---
name: project-navigator
description: Guide for navigating the project structure, understanding the monorepo architecture, and using the `just` command runner to manage packages and workflows. Use this skill when the user asks about the project layout, how to add new packages, or how to run/test existing components.
---

# Project Navigator

This skill consolidates knowledge about the repository's structure, architecture, and tooling. Use it to understand where things are, how the monorepo works, and how to perform common tasks like adding or running packages.

## Project Structure

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

## Command System (`just`)

The project uses `just` as a unified interface for all operations. Do not run `uv` commands manually if a `just` command exists.

### Common Commands

- **Initialize**: `just init` (Installs all dependencies)
- **Start**: `just start [package]` (e.g., `just start support`)
- **Test**: `just test [package]` (e.g., `just test shared` or just `just test` for all)
- **Install**: `just install [package]` (e.g., `just install corporate`)
- **Check**: `just check [package]` (Runs format, lint, typecheck, and test)

**Note**: Package names often have aliases (e.g., `internal-support-agent` -> `support`).

## Workflow: Creating a New Package

See [Workflow: Creating a New Package](./references/new-package-workflow.md) for the detailed step-by-step guide on adding a new package to the monorepo.

## Package Architecture

See [Package Architecture](./references/package-architecture.md) for details on shared utilities, dependency management, and environment variables.

## Learning Materials

The `learning/` directory contains progressive modules (`01-fundamentals`, etc.). Use the `learning-structure` skill (if available) to manage these, but be aware they exist as a parallel resource to the code in `packages/`.
