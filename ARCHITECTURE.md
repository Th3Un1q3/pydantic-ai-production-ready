# Architecture Overview

This document describes the architecture and design decisions for the Pydantic AI Production Ready monorepo.

## Repository Structure

The canonical repository and package layout is maintained in:

- [`.github/instructions/monorepo.instructions.md`](.github/instructions/monorepo.instructions.md)

This document focuses on architecture rationale and design decisions rather than repeating the directory tree.

## Projects Monorepo Architecture

### Design Philosophy

The `` directory implements a **workspace-based monorepo** using uv, designed for:

1. **Scalability**: Support multiple independent projects
2. **Code Reuse**: Share common utilities without duplication
3. **Independent Deployment**: Deploy projects separately
4. **Clear Boundaries**: Each project is self-contained
5. **Type Safety**: Full type checking across packages

### Workspace Structure

Use the workspace boundary rules and structure contract in:

- [`.github/instructions/monorepo.instructions.md`](.github/instructions/monorepo.instructions.md)

### Package Dependency Graph

```text
┌─────────────────────────────────────────┐
│         Workspace Root                  │
│    (Development dependencies)           │
└─────────────────────────────────────────┘
            │
            ├──────────────┬──────────────┐
            ▼              ▼              ▼
    ┌──────────────┐ ┌──────────────┐
    │   shared     │ │    course-   │
    │              │ │   navigator  │
    └──────────────┘ └──────────────┘
                            │
                            └──────┬───────┘
                                   ▼
                            ┌──────────────┐
                            │   shared     │
                            │  (runtime)   │
                            └──────────────┘
```

## Package Descriptions

### 1. Workspace Root (``)

**Purpose**: Define workspace members and shared development dependencies

**Key Features**:

- Workspace member declaration
- Shared dev dependencies (pytest, black, ruff, mypy)
- No runtime dependencies
- Unified tooling configuration

**Technology**: uv workspace (similar to npm/yarn workspaces)

### 2. Shared Package (`packages/shared/`)

**Purpose**: Common utilities and reusable components

**Dependencies**:

- Core: pydantic-ai, pydantic, loguru, httpx
- Optional: openai, anthropic

**Exports**:

- Configuration management (`config.py`)
- Example implementations
- Common utilities

**Use Case**: Imported by other packages to avoid code duplication

### 3. Course Navigator (`packages/course-navigator/`)

**Purpose**: AI agent for navigating course materials and answering student queries.

**Dependencies**:

- Runtime: pydantic-ai-shared, openai
- Optional: postgres, redis

**Key Features**:

- Student support
- Material search
- Progress tracking

**Default Model**: OpenAI GPT-4

**Deployment**: Standalone service or container

## Design Patterns

### 1. Workspace Pattern

**Why**: Enables multiple projects with independent dependencies while sharing code

**Implementation**: uv workspace with explicit member declaration

**Benefits**:

- Single dependency resolution
- Simplified cross-package imports
- Unified tooling
- Independent versioning

### 2. Shared Configuration

**Why**: Consistent model selection and configuration across packages

**Implementation**: `shared/src/config.py` with environment variable overrides

**Benefits**:

- Centralized defaults
- Environment-specific configuration
- Type-safe configuration access

### 3. Package-Specific Dependencies

**Why**: Each project has different requirements

**Implementation**: Package-level pyproject.toml with specific dependencies

**Examples**:

- `course-navigator`: Needs OpenAI for student interactions and PostgreSQL for progress tracking

### 4. Optional Dependencies

**Why**: Users only install what they need

**Implementation**: `[project.optional-dependencies]` groups

**Examples**:

- `--extra openai`: OpenAI integration
- `--extra postgres`: PostgreSQL support
- `--extra redis`: Redis caching

## Technology Choices

### uv Package Manager

**Why uv?**

- ✅ **Fast**: 10-100x faster than pip
- ✅ **Workspace Support**: Native monorepo support
- ✅ **Lock Files**: Reproducible builds
- ✅ **Modern**: Built with Rust, active development

**Alternatives Considered**:

- Poetry: Good but slower, less monorepo focus
- pip-tools: Lacks workspace support
- PDM: Good but less mature workspace support

### Pydantic AI Framework

**Why Pydantic AI?**

- ✅ **Type Safety**: Full type checking
- ✅ **Validation**: Structured outputs with Pydantic
- ✅ **Tool Calling**: Native function execution
- ✅ **Model Agnostic**: Works with any LLM provider

### Project Structure

**Why src/ layout?**

- ✅ **Import Safety**: Prevents accidental imports from dev directory
- ✅ **Testing**: Forces proper package installation
- ✅ **Standards**: Follows Python packaging best practices

## DevContainer Architecture

### Multi-Service Setup

```text
┌─────────────────────────────────────┐
│     VS Code Dev Container           │
├─────────────────────────────────────┤
│  Python 3.12 + uv                   │
│  All workspace packages installed   │
└─────────────────────────────────────┘
            │
            ├──────────────┬──────────────┐
            ▼              ▼              ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │  PostgreSQL  │ │    Redis     │ │  Project     │
    │   :5432      │ │    :6379     │ │  Services    │
    └──────────────┘ └──────────────┘ └──────────────┘
```

**Services**:

- **App Container**: Python development environment
- **PostgreSQL**: Database for persistent storage
- **Redis**: Caching and pub/sub

**Benefits**:

- Reproducible environment
- All dependencies included
- No local setup required
- Easy onboarding

## Scalability Considerations

### Adding New Projects

**Steps**:

1. Create package directory: `packages/new-project/`
2. Add `pyproject.toml` with dependencies
3. Register in workspace root
4. Run `uv sync`

**Time to Add**: < 5 minutes

### Independent Deployment

Each package can be deployed separately:

**Docker**:

```dockerfile
COPY packages/shared ./packages/shared
COPY packages/my-project ./packages/my-project
RUN uv sync --package my-project
```

**Serverless**:

- Each package is small enough for Lambda/Cloud Functions
- Share layer for common dependencies

### Testing Strategy

**Levels**:

1. **Unit Tests**: Per-package tests
2. **Integration Tests**: Cross-package interactions
3. **E2E Tests**: Full workflow tests

**Execution**:

```bash
# All packages
uv run pytest

# Specific package
cd packages/internal-support-agent && uv run pytest

# With coverage
uv run pytest --cov=src
```

## Learning Materials Architecture

### Modular Design

**Philosophy**: Progressive, self-contained modules

**Structure**:

- Each module is independent
- Progressive complexity
- Hands-on exercises
- References to working code

**Benefits**:

- Easy for learners to follow
- Simple for content creators to extend
- Clear learning path

## Security Considerations

### 1. API Key Management

- ✅ Environment variables in `.env`
- ✅ Never committed to git (`.gitignore`)
- ✅ Example template provided (`.env.example`)

### 2. Dependency Security

- ✅ Lock files for reproducibility
- ✅ Minimal dependencies
- ✅ Well-maintained packages only

### 3. Code Security

- ✅ Type checking with mypy
- ✅ Linting with ruff
- ✅ CodeQL scanning
- ✅ No secrets in code

## Future Extensibility

### Planned Additions

1. **More Example Projects**:
   - Document processing agent
   - Customer service bot
   - Data analysis agent

2. **Advanced Features**:
   - Shared middleware
   - Common testing utilities
   - Deployment templates

3. **Integration Examples**:
   - Vector databases
   - Observability tools
   - API frameworks

### Extension Points

- **New Packages**: Add to `packages/`
- **New Learning Modules**: Add to `learning/`
- **New Services**: Add to `.devcontainer/docker-compose.yml`

## Performance Characteristics

### Build Time

- **Cold Start**: ~30s (all packages)
- **Incremental**: ~2s (single package)
- **Test Suite**: ~5s (without API calls)

### Resource Usage

- **Development**: ~2GB RAM
- **Production (per service)**: ~512MB RAM
- **Database**: ~256MB RAM

## Monitoring and Observability

### Logging

- **Library**: loguru (structured logging)
- **Levels**: DEBUG, INFO, WARNING, ERROR
- **Output**: Structured JSON in production

### Metrics

- **Package**: Built-in Python metrics
- **Custom**: Per-project instrumentation

## Conclusion

This architecture provides a **scalable, maintainable, and production-ready** foundation for building AI applications with Pydantic AI. The workspace-based monorepo enables:

1. **Multiple projects** with independent lifecycles
2. **Code sharing** without duplication
3. **Type safety** across the entire codebase
4. **Easy onboarding** with DevContainers
5. **Production deployment** flexibility

The design balances **simplicity** for new users with **power** for advanced use cases.
