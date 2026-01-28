# Package Architecture

- **`shared` Package**: Contains core utilities, configuration (`config.py`), and shared logic. Most other packages should depend on this.
- **Dependency Management**:
  - **Shared**: Define common dev dependencies in the root `pyproject.toml`.
  - **Specific**: Define runtime dependencies in each package's `pyproject.toml`.
- **Environment Variables**: Managed via `.env` file (not committed) and loaded via `shared.config`.
