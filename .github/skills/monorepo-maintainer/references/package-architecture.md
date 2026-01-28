# Package Architecture

The command system leverages **uv workspaces** for efficient dependency management and command execution.

## Main Justfile (Root)

Located at the repository root, acts as the primary interface:
- **Workspace-aware**: Uses `uv sync` and `uv run` to manage the monorepo environment
- **Alias resolution**: Maps short names (e.g., `support`) to full package names
- **Centralized logic**: Defines standard commands (`start`, `test`) across the workspace

## Package Structure

Each package is a member of the updated uv workspace:
- **pyproject.toml**: Defines package-specific dependencies
- **Source layout**: Follows standard `src/<package_name>` structure
- **Workspace integration**: Packages can be run from the root using `uv run --package <name>`

## Shared Components

- **`shared` Package**: Contains core utilities, configuration (`config.py`), and shared logic. Most other packages should depend on this.
- **Dependency Management**:
  - **Shared**: Define common dev dependencies in the root `pyproject.toml`.
  - **Specific**: Define runtime dependencies in each package's `pyproject.toml`.
- **Environment Variables**: Managed via `.env` file (not committed) and loaded via `shared.config`.
