# Pydantic AI Production Ready - Packages Monorepo

This directory contains a **workspace-based Python monorepo** for multiple AI projects using Pydantic AI Framework.

## Monorepo Structure

```
/
├── pyproject.toml           # Workspace root configuration
├── packages/                # Individual projects/packages
│   ├── shared/             # Shared utilities and common code
│   │   ├── src/
│   │   ├── tests/
│   │   └── pyproject.toml
│   ├── internal-support-agent/   # Internal company support AI
│   │   ├── src/
│   │   ├── tests/
│   │   └── pyproject.toml
│   └── corporate-agentic-system/ # Multi-agent corporate system
│       ├── src/
│       ├── tests/
│       └── pyproject.toml
├── .env.example
└── README.md                # This file
```

## Why This Structure?

This **state-of-the-art monorepo** structure provides:

✅ **Scalability**: Each project has its own dependencies  
✅ **Code Reuse**: Shared code in `packages/shared`  
✅ **Independent Deployment**: Deploy projects separately  
✅ **Workspace Management**: uv handles cross-package dependencies  
✅ **Clear Boundaries**: Each project is self-contained  

## Getting Started

### Install All Packages

```bash
just install
# or directly with uv
uv sync
```

This installs all workspace packages and their dependencies.

### Work with Specific Package

```bash
# Using just (recommended)
just install support
just start support
just test support

# Or directly with uv
uv sync --package internal-support-agent
cd packages/internal-support-agent && uv run python src/agent.py
```

## Packages

### 📦 shared

Common utilities, helpers, and example code shared across projects.

**Location**: `packages/shared/`  
**Dependencies**: Core Pydantic AI dependencies  
**Use case**: Reusable components, base classes, utilities

### 🎫 internal-support-agent

AI agent for internal company support handling IT, HR, and general queries.

**Location**: `packages/internal-support-agent/`  
**Dependencies**: OpenAI, PostgreSQL, Redis  
**Use case**: Employee support, ticket creation, query routing

**Run demo**:
```bash
just start support
```

### 🏢 corporate-agentic-system

Multi-agent orchestrator for corporate workflow automation.

**Location**: `packages/corporate-agentic-system/`  
**Dependencies**: Anthropic (Claude), PostgreSQL, Redis  
**Use case**: Document processing, meeting scheduling, workflow planning

**Run demo**:
```bash
just start corporate
```

## Adding a New Project

1. **Create package directory**:
   ```bash
   mkdir -p packages/my-new-agent/{src,tests}
   ```

2. **Create `pyproject.toml`**:
   ```toml
   [project]
   name = "my-new-agent"
   version = "0.1.0"
   dependencies = [
       "pydantic-ai-shared",  # Use shared code
       "pydantic-ai>=0.0.13",
       # ... other deps
   ]
   ```

3. **Register in workspace** (`pyproject.toml` at root):
   ```toml
   [tool.uv.workspace]
   members = [
       "packages/shared",
       "packages/internal-support-agent",
       "packages/corporate-agentic-system",
       "packages/my-new-agent",  # Add this
   ]
   ```

4. **Sync workspace**:
   ```bash
   just install
   ```

## Development Workflow

### Running Tests

```bash
# All packages
just test

# Specific package
just test support

# With coverage
cd packages/internal-support-agent && uv run pytest --cov=src
```

### Code Formatting

```bash
# Format all packages
just format

# Lint all packages
just lint

# Type check
just typecheck
```

### Package-Specific Commands

Each package can be developed independently:

```bash
# Work in package directory
cd packages/internal-support-agent

# Install just this package's deps
just install support

# Run its code
just start support

# Run its tests
just test support
```

## Dependencies

### Shared Dependencies (workspace-level)

Defined in root `pyproject.toml`:
- pytest, black, ruff, mypy
- Available to all packages

### Package-Specific Dependencies

Each package defines its own in its `pyproject.toml`:
- **shared**: Core Pydantic AI stack
- **internal-support-agent**: + OpenAI, PostgreSQL, Redis
- **corporate-agentic-system**: + Anthropic, PostgreSQL, Redis

### Installing Optional Dependencies

```bash
# Install with all extras for a package
just install support
uv sync --package internal-support-agent --all-extras

# Install specific extras
uv sync --package internal-support-agent --extra postgres --extra redis
```

## Environment Configuration

Create `.env` in the root directory:

```bash
cp .env.example .env
# Edit .env with your keys
```

All packages share the same `.env` file:
```bash
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
```

## Deployment

Each package can be deployed independently:

### Docker Deployment

```dockerfile
# Example: Deploy internal-support-agent
FROM python:3.12
WORKDIR /app
COPY packages/shared ./packages/shared
COPY packages/internal-support-agent ./packages/internal-support-agent
COPY pyproject.toml ./
RUN pip install uv && uv sync --package internal-support-agent
CMD ["uv", "run", "python", "packages/internal-support-agent/src/agent.py"]
```

### Serverless Deployment

Each package is small enough to deploy as a serverless function.

## Best Practices

1. **Keep shared minimal**: Only truly shared code in `shared`
2. **Package independence**: Packages shouldn't depend on each other (except shared)
3. **Clear boundaries**: Each package serves a specific use case
4. **Consistent structure**: All packages follow same src/tests layout
5. **Version together**: Use same version for all packages

## Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- [Python Monorepo Best Practices](https://packaging.python.org/)

