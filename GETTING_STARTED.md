# Getting Started Guide

Welcome! This guide will help you get started with the Pydantic AI Production Ready repository.

## What You'll Find Here

This repository is designed for both learners and practitioners who want to build production-ready AI applications using Pydantic AI Framework.

### 🎯 For Learners

Navigate to the `learning/` directory for structured learning materials:

1. **Start Here**: [`learning/01-fundamentals/`](learning/01-fundamentals/)
   - Introduction to Pydantic AI
   - Environment setup
   - Your first agent

2. **Build Skills**: [`learning/02-core-concepts/`](learning/02-core-concepts/)
   - Deep dive into agents
   - Working with models
   - Tool calling

3. **Advanced Topics**: [`learning/03-advanced-patterns/`](learning/03-advanced-patterns/)
   - Streaming responses
   - Error handling
   - Multi-agent systems

4. **Go to Production**: [`learning/04-production-deployment/`](learning/04-production-deployment/)
   - Monitoring
   - Scaling
   - Security

### 💻 For Developers

Use the `projects/` directory for hands-on development:

```bash
cd projects
uv sync                  # Install dependencies
uv run pytest           # Run tests
uv run python -m src.examples.chatbot  # Run examples
```

## Quick Start Options

### Option 1: DevContainer (Recommended)

**Best for**: Complete, isolated development environment

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install [VS Code](https://code.visualstudio.com/) + [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open this repo in VS Code
4. Press `F1` → "Dev Containers: Reopen in Container"
5. Wait for setup to complete (automatic!)

**What you get:**
- ✅ Python 3.12
- ✅ uv package manager
- ✅ PostgreSQL database
- ✅ Redis cache
- ✅ All dependencies installed

### Option 2: Local Setup

**Best for**: Working with existing local tools

1. **Install uv**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup**
   ```bash
   git clone https://github.com/Th3Un1q3/pydantic-ai-production-ready.git
   cd pydantic-ai-production-ready/projects
   uv sync
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## Your First Steps

### 1. Explore Examples

The repository includes working examples:

```bash
cd projects

# View available examples
ls -la src/examples/

# Simple chatbot (requires OPENAI_API_KEY)
uv run python -m src.examples.chatbot

# Data extraction
uv run python -m src.examples.data_extraction
```

### 2. Run Tests

Verify everything works:

```bash
cd projects
uv run pytest -v
```

### 3. Start Learning

Open and read through the learning materials:

1. [`learning/01-fundamentals/01-introduction.md`](learning/01-fundamentals/01-introduction.md)
2. Follow the lessons in order
3. Complete exercises in each module

### 4. Build Your Own Project

Start building in the `projects/src/` directory:

```python
# projects/src/my_agent.py
from pydantic_ai import Agent

agent = Agent('openai:gpt-4')
result = agent.run_sync('Hello!')
print(result.data)
```

## Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cd projects
cp .env.example .env
```

Required variables:
- `OPENAI_API_KEY` - Get from [OpenAI Platform](https://platform.openai.com/api-keys)

Optional variables:
- `ANTHROPIC_API_KEY` - For Claude models
- `DATABASE_URL` - For PostgreSQL (auto-configured in devcontainer)
- `REDIS_URL` - For Redis (auto-configured in devcontainer)

## Repository Structure

```
pydantic-ai-production-ready/
├── .devcontainer/          # DevContainer configuration
│   ├── devcontainer.json   # VS Code devcontainer settings
│   ├── docker-compose.yml  # Multi-service setup
│   ├── Dockerfile          # Container image
│   └── post-create.sh      # Setup script
│
├── learning/               # Learning materials
│   ├── 01-fundamentals/    # Start here!
│   ├── 02-core-concepts/   # Core Pydantic AI concepts
│   ├── 03-advanced-patterns/ # Advanced topics
│   ├── 04-production-deployment/ # Production guide
│   └── README.md           # Learning materials overview
│
├── projects/               # Python monorepo
│   ├── src/               # Source code
│   │   ├── examples/      # Example implementations
│   │   └── __init__.py
│   ├── tests/             # Test files
│   ├── pyproject.toml     # Dependencies & config
│   ├── .env.example       # Environment template
│   └── README.md          # Project documentation
│
├── README.md              # Main documentation
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE                # MIT License
└── .gitignore            # Git ignore rules
```

## Common Tasks

### Install Dependencies

```bash
cd projects
uv sync                    # Install base dependencies
uv sync --all-extras      # Install all optional dependencies
uv sync --extra openai    # Install specific extras
```

### Run Code

```bash
cd projects
uv run python -m src.examples.chatbot
```

### Test Code

```bash
cd projects
uv run pytest              # Run all tests
uv run pytest -v          # Verbose output
uv run pytest tests/test_basic.py  # Run specific test
```

### Format and Lint

```bash
cd projects
uv run black .            # Format code
uv run ruff check --fix . # Lint and fix
uv run mypy src           # Type checking
```

## Available Services (DevContainer)

When using the devcontainer, these services are automatically available:

- **PostgreSQL**: `localhost:5432`
  - User: `postgres`
  - Password: `postgres`
  - Database: `pydantic_ai_db`

- **Redis**: `localhost:6379`

## Need Help?

- 📖 **Documentation**: See [learning/](learning/) directory
- 🐛 **Issues**: [GitHub Issues](https://github.com/Th3Un1q3/pydantic-ai-production-ready/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Th3Un1q3/pydantic-ai-production-ready/discussions)
- 📚 **Pydantic AI Docs**: https://ai.pydantic.dev/

## Next Steps

1. ✅ Choose your setup method (DevContainer or Local)
2. ✅ Get the environment running
3. ✅ Run the examples
4. ✅ Start with [`learning/01-fundamentals/`](learning/01-fundamentals/)
5. ✅ Build your first agent!

Happy learning and building! 🚀
