# Pydantic AI Production Ready

> There is a difference between demo magic and enterprise reality. This project teaches you how to bring magic to reality.

Build your production-ready AI application with Pydantic AI Framework

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

This repository provides a comprehensive framework for building production-ready AI applications using [Pydantic AI](https://ai.pydantic.dev/). It includes:

- **📚 Modular Learning Materials**: Progressive, extensible content for developers and content creators
- **🛠️ Production-Ready Project Structure**: Python monorepo using `uv` with best practices
- **🐳 DevContainer Setup**: Fully configured development environment with Docker Compose
- **🚀 Example Implementations**: Real-world examples and patterns

## 🏗️ Repository Structure

```
.
├── .devcontainer/          # DevContainer configuration with Docker Compose
│   ├── devcontainer.json
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── post-create.sh
├── learning/               # Modular learning materials
│   ├── 01-fundamentals/
│   ├── 02-core-concepts/
│   ├── 03-advanced-patterns/
│   └── 04-production-deployment/
├──                # Python monorepo with uv
│   ├── src/               # Source code
│   ├── tests/             # Test files
│   └── pyproject.toml     # Project configuration
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Quick Start

### Option 1: Using DevContainer (Recommended)

1. **Prerequisites**
   - [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - [VS Code](https://code.visualstudio.com/) with [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in Container**

   ```bash
   # Clone the repository
   git clone https://github.com/Th3Un1q3/pydantic-ai-production-ready.git
   cd pydantic-ai-production-ready

   # Open in VS Code
   code .

   # Press F1 and select "Dev Containers: Reopen in Container"
   ```

3. **Start Coding**
   The devcontainer will automatically:
   - Set up Python 3.12
   - Install `uv` package manager
   - Install `just` command runner
   - Start PostgreSQL and Redis
   - Install all dependencies

4. **Use Commands**

   ```bash
   just init          # Initialize environment
   just start support # Start internal support agent
   just test          # Run all tests
   ```

### Option 2: Local Setup (Not Recommended)

1. **Install Prerequisites**

   Ensure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) and [just](https://just.systems/man/en/chapter_4.html) installed.

2. **Clone and Setup**

   ```bash
   git clone https://github.com/Th3Un1q3/pydantic-ai-production-ready.git
   cd pydantic-ai-production-ready

   # Initialize environment (installs all dependencies)
   just init

   # Or manually
   # No need to cd && uv sync
   ```

3. **Explore Commands**

   ```bash
   just              # List all available commands
   just help         # Show detailed help
   just start support # Start internal support agent
   just test         # Run all tests
   ```

## 📋 Command System

This repository uses `just` for task automation. See **[COMMANDS.md](COMMANDS.md)** for detailed documentation.

### Common Commands

```bash
# Discovery
just                  # List all commands
just help            # Show detailed help

# Installation
just install         # Install all packages
just install support # Install specific package

# Development
just start support   # Start internal support agent (auto-installs)
just start corporate # Start corporate system (auto-installs)

# Testing
just test            # Test all packages
just test support    # Test specific package

# Code Quality
just format          # Format all code
just lint            # Lint all code
just check           # Run all checks (format + lint + typecheck + test)

# Utilities
just clean           # Clean build artifacts
just tree            # Show project structure
just info            # Show environment info
```

**Key Features:**

- ✅ **Discoverable**: Run `just` to see all commands
- ✅ **Automatic Dependencies**: `just start` installs if needed
- ✅ **Modular**: Per-package commands available
- ✅ **Consistent**: Predictable command structure

## 📚 Learning Path

Start your journey with the modular learning materials in the `learning/` directory:

1. **[Fundamentals](learning/01-fundamentals/)** - Get started with Pydantic AI basics
2. **[Core Concepts](learning/02-core-concepts/)** - Master agents, models, and tools
3. **[Advanced Patterns](learning/03-advanced-patterns/)** - Implement production patterns
4. **[Production Deployment](learning/04-production-deployment/)** - Deploy and scale

Each module includes:

- 📖 Comprehensive guides
- 💻 Hands-on exercises
- 🔗 Links to working examples

## 🛠️ Development

See **[COMMANDS.md](COMMANDS.md)** for complete command reference.

### Quick Development Workflow

```bash
# Work on a package
just install support        # Install dependencies
just start support          # Start the application
just test support           # Run tests
just check support          # Run all quality checks

# Or use convenient shortcuts
just install-support
just start-support
just test-support
```

### Manual Development (without just)

If you prefer to use uv directly:

```bash
# No need to cd

# Install dependencies
uv sync

# Run tests
uv run pytest

# Format code
uv run black .
uv run ruff check --fix .

# Type checking
uv run mypy packages/*/src
```

```

### Available Services (in DevContainer)

- **PostgreSQL**: `localhost:5432`
- **Redis**: `localhost:6379`

### Environment Variables

Create a `.env` file in the `` directory:

```bash
# OpenAI
OPENAI_API_KEY=your_key_here

# Database (devcontainer)
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/pydantic_ai_db

# Redis (devcontainer)
REDIS_URL=redis://redis:6379
```

## 🎓 For Content Creators

The learning materials are designed to be extensible. See [learning/README.md](learning/README.md) for:

- Module structure guidelines
- Content creation templates
- Best practices for educational content

## 🤝 Contributing

Contributions are welcome! Whether you're:

- Adding new learning materials
- Improving examples
- Fixing bugs
- Adding features

Please feel free to open issues or pull requests.

## 📦 Dependencies

Core dependencies:

- **pydantic-ai**: The main framework
- **pydantic**: Data validation
- **loguru**: Logging
- **httpx**: HTTP client

Optional dependencies (install with `uv sync --extra <name>`):

- `openai`: OpenAI integration
- `anthropic`: Anthropic (Claude) integration
- `postgres`: PostgreSQL support
- `redis`: Redis support

## 🔧 Technologies

- **Python 3.12+**: Latest Python features
- **uv**: Fast Python package manager
- **Pydantic AI**: AI framework
- **Docker Compose**: Multi-service development
- **DevContainers**: Reproducible environments

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Pydantic AI](https://ai.pydantic.dev/) - The amazing AI framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation library
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

## 📞 Support

- 📖 [Documentation](learning/)
- 🐛 [Issue Tracker](https://github.com/Th3Un1q3/pydantic-ai-production-ready/issues)
- 💬 [Discussions](https://github.com/Th3Un1q3/pydantic-ai-production-ready/discussions)

---

**Happy Building! 🚀**
