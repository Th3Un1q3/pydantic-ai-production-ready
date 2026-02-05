# Getting Started Guide

> The primary technical steps to get the development environment running.

## Prerequisites

- Docker (desktop or engine) — used for the Dev Container
- Visual Studio Code
- Dev Containers extension for VS Code
- `just` command runner (installed inside the devcontainer)
- `uv` (Python package manager)

## DevContainer (recommended)

1. Open the repository in VS Code.
2. Press `F1` → "Dev Containers: Reopen in Container".
3. Wait for the container to build and start. The devcontainer will install system packages and dev tooling.
4. Open a terminal inside the container and run:

```bash
just init # Should automatically open .env file to edit
# Edit .env to add API keys (see below)
```

1. Verify quick checks:

```bash
# inside the devcontainer
just test    # run tests for the monorepo
just start course-navigator   # run the course navigator agent demo
```

## OpenRouter (recommended for development)

We recommend using **OpenRouter** as the primary routing layer for LLM access during development. OpenRouter helps avoid vendor lock-in by providing one API endpoint that can route requests to multiple model providers, and it offers free development models that are ideal for experimenting without incurring immediate costs. It also transparently passes through provider pricing for production use when you switch to paid models.

### Quick OpenRouter setup

1. Sign up or log in at OpenRouter (see: <https://openrouter.ai/docs/quickstart>).
2. Create an API token and copy it.
3. Add your OpenRouter token to the `.env` file as `OPEN_ROUTER_API_KEY` (see API keys example below).

Example `.env` snippet:

```bash
# OpenRouter (recommended for development)
OPEN_ROUTER_API_KEY=your_openrouter_api_key_here
```

If you prefer a direct provider integration (OpenAI, Anthropic, etc.), you can keep provider-specific keys as well (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`). Using OpenRouter makes it easy to swap endpoints and test multiple models without changing your code.

---

## Local setup (Not recommended)

If you haven't tried using devcontainers yet, we recommend starting with that approach as it's not only easier but ensures consistency across environments. And that's how most of great productions are built nowadays.

1. **Install Prerequisites**

   Ensure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) and [just](https://just.systems/man/en/chapter_4.html) installed.

2. **Clone and Setup**

   ```bash
   git clone https://github.com/Th3Un1q3/pydantic-ai-production-ready.git
   cd pydantic-ai-production-ready

   # Initialize environment (installs all dependencies)
   just init
   ```

3. **Explore Commands**

   ```bash
   just              # List all available commands
   just help         # Show detailed help
   just start course-navigator # Start course navigator agent
   just test         # Run all tests
   ```

## Where to go next

- For high-level learning path and staged workflow, see `learning/01-fundamentals/`.
- For optional deep-dive and background, `learning/01-fundamentals/02-setup.md` contains context and additional notes.
