# Workflow: Creating a New Package

To add a new agent or package to the monorepo:

1. **Create Directory Structure**:

    Create the package structure ensuring the inner source package name (snake_case) matches what you intend to import.

    ```bash
    # Create the package root and test directory
    mkdir -p packages/my-new-package/tests

    # Create the source directory with the package name (snake_case)
    mkdir -p packages/my-new-package/src/my_new_package

    # Create __init__.py to make it a package
    touch packages/my-new-package/src/my_new_package/__init__.py
    ```

2. **Create `pyproject.toml`**:
    Create a configuration in `packages/my-new-package/pyproject.toml`. Include the build system configuration to ensure the package is installed correctly in editable mode.

    ```toml
    [project]
    name = "my-new-package"
    version = "0.1.0"
    description = "Description of my new package"
    requires-python = ">=3.12"
    dependencies = [
        "pydantic-ai-shared", # Use shared code
        "pydantic-ai>=0.0.13",
    ]

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [tool.hatchling.build.targets.wheel]
    packages = ["src/my_new_package"]
    ```

3. **Create `justfile`**:
    Create `packages/my-new-package/justfile` with standard commands. Using `python -m` is preferred for running installed modules.

    ```just
    start:
        uv run python -m my_new_package.main

    test:
        uv run pytest
    ```

4. **Register in Workspace**:
    Edit the root `pyproject.toml` to add the new package to `tool.uv.workspace.members`.

    ```toml
    [tool.uv.workspace]
    members = [
        "packages/shared",
        "packages/course-navigator",
        "packages/my-new-package",  # Add this
    ]
    ```

5. **Install Minimal Dependencies**:
    Add only the strictly required libraries. `uv add` will automatically install the latest versions:

    ```bash
    # Add external dependencies (installs latest)
    uv add --package my-new-package pydantic

    # Add internal dependency
    uv add --package my-new-package pydantic-ai-shared
    ```

6. **Initialize**:
    Run `just init` to sync the workspace.

7. **Verify**:

    ```bash
    just start my-new-package
    just test my-new-package
    ```
