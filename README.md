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

Global repository structure is maintained in one canonical location for Copilot and contributors:

- [`.github/instructions/monorepo.instructions.md`](.github/instructions/monorepo.instructions.md)

For folder-specific structure details, use local docs:

- [`learning/README.md`](learning/README.md)
- [`packages/README.md`](packages/README.md)
- [`specs/README.md`](specs/README.md)

## 🚀 Quick Start

For detailed setup instructions, please refer to **[GETTING_STARTED.md](GETTING_STARTED.md)**.

### In a Nutshell (DevContainer)

1. **Clone & Open**: `git clone ...` then open in VS Code.
2. **Reopen in Container**: Use the "Dev Containers: Reopen in Container" command.
3. **Initialize**: Run `just init` in the terminal.
4. **Run**: `just start course-navigator`

## 📋 Command System

This repository uses `just` for task automation. See **[COMMANDS.md](COMMANDS.md)** for detailed documentation, available commands, and usage examples.

## 📚 Learning Path

Start your journey with the modular learning materials in the `learning/` directory:

1. **[Fundamentals](learning/01-fundamentals/)** - Get started with Pydantic AI basics
2. **[Learning Roadmap](learning/README.md)** - Current module index and contributor guidance

Each module includes:

- 📖 Comprehensive guides
- 💻 Hands-on exercises
- 🔗 Links to working examples

## 🛠️ Development

See **[COMMANDS.md](COMMANDS.md)** for the comprehensive command reference and development workflows.

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

## 📝 Spec-Based Development

This repository supports specification-driven development for AI-assisted implementation:

### Workflow

1. **Write a Specification**: Use `/write-spec` in GitHub Copilot to create a comprehensive spec
2. **Implement the Specification**: Use `/implement-spec` to execute with validation

### Benefits

- **AI-Assisted Authoring**: Discovery phase ensures complete requirements
- **Phased Implementation**: Validation gates prevent regressions
- **Quality Assurance**: Measurable success criteria and acceptance tests
- **Documentation**: Automatic updates to docs and changelog

### Quick Start

```text
# In GitHub Copilot Chat: create a specification (interactive)
/write-spec

# In GitHub Copilot Chat: implement an existing specification
/implement-spec specs/features/SPEC-001-feature-name.md
```

### GitHub Copilot Hooks

This repository includes automated hooks for GitHub Copilot:

- **Markdown Linting**: All markdown files are automatically linted and formatted using `markdownlint` after edits
- **Configuration**: See `.github/hooks/hooks.json` and `.markdownlint.json`

See [specs/README.md](specs/README.md) for full documentation.

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

## Happy Building! 🚀
