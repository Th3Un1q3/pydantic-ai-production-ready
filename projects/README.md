# Pydantic AI Production Ready - Projects

This directory contains the Python monorepo for all project implementations using Pydantic AI Framework.

## Structure

```
projects/
├── src/              # Source code for projects
│   ├── __init__.py
│   └── ...
├── tests/            # Test files
│   ├── __init__.py
│   └── ...
├── pyproject.toml    # Project configuration and dependencies
└── README.md         # This file
```

## Getting Started

### Using uv (recommended)

Install dependencies:
```bash
cd projects
uv sync
```

Run tests:
```bash
uv run pytest
```

Run a specific module:
```bash
uv run python -m src.module_name
```

### Development

Format code:
```bash
uv run black .
uv run ruff check --fix .
```

Type checking:
```bash
uv run mypy src
```

## Dependencies

Core dependencies:
- **pydantic-ai**: The main AI framework
- **pydantic**: Data validation using Python type annotations
- **loguru**: Logging made simple
- **httpx**: Modern HTTP client

Optional dependencies:
- **openai**: For OpenAI models integration
- **anthropic**: For Anthropic (Claude) models integration
- **postgres**: For PostgreSQL database support
- **redis**: For Redis caching and pub/sub

Install optional dependencies:
```bash
uv sync --extra openai
uv sync --extra anthropic
uv sync --extra postgres
uv sync --extra redis
```

Or install all extras:
```bash
uv sync --all-extras
```
