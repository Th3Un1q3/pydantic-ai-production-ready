# Workflow: Creating a New Package

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
        "packages/shared",
        "packages/internal-support-agent",
        "packages/corporate-agentic-system",
        "packages/my-new-package",  # Add this
    ]
    ```

5. **Initialize**:
    Run `just init` or `just install my-new-package` to set up dependencies.

6. **Verify**:

    ```bash
    just start my-new-package
    just test my-new-package
    ```
