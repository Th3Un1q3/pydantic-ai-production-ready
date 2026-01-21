# Environment Setup

This guide will help you set up your development environment for working with Pydantic AI.

## Prerequisites

- Python 3.12 or higher
- Git
- Docker (for devcontainer setup)

## Option 1: Using DevContainer (Recommended)

The easiest way to get started is using the provided devcontainer configuration.

### Steps

1. **Install Prerequisites**
   - [Visual Studio Code](https://code.visualstudio.com/)
   - [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in DevContainer**
   - Open this repository in VS Code
   - Press `F1` and select "Dev Containers: Reopen in Container"
   - Wait for the container to build and start

3. **Verify Setup**
   ```bash
   # Check Python version
   python --version  # Should be 3.12+
   
   # Check uv installation
   uv --version
   
   # Navigate to projects directory
   cd /workspace/projects
   
   # Install dependencies
   uv sync
   ```

The devcontainer includes:
- Python 3.12
- uv package manager
- PostgreSQL database
- Redis cache
- All necessary development tools

## Option 2: Local Setup

If you prefer to set up your environment locally:

### 1. Install Python 3.12+

**macOS (using Homebrew)**
```bash
brew install python@3.12
```

**Ubuntu/Debian**
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3-pip
```

**Windows**
Download from [python.org](https://www.python.org/downloads/)

### 2. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or using pip:
```bash
pip install uv
```

### 3. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Th3Un1q3/pydantic-ai-production-ready.git
cd pydantic-ai-production-ready

# Navigate to projects directory
cd projects

# Create virtual environment and install dependencies
uv sync
```

### 4. Optional: Install Database Services

**PostgreSQL**
```bash
# macOS
brew install postgresql@16

# Ubuntu/Debian
sudo apt install postgresql-16
```

**Redis**
```bash
# macOS
brew install redis

# Ubuntu/Debian
sudo apt install redis-server
```

## API Keys Setup

You'll need API keys for LLM providers. Create a `.env` file in the `projects` directory:

```bash
cd projects
cat > .env << 'EOF'
# OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic (optional)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Database (for devcontainer)
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/pydantic_ai_db

# Redis (for devcontainer)
REDIS_URL=redis://redis:6379
EOF
```

> **Note:** Never commit the `.env` file to version control!

## Verify Installation

Run the test suite to verify everything is set up correctly:

```bash
cd projects
uv run pytest
```

You should see all tests passing.

## IDE Configuration

### VS Code (Recommended)

The devcontainer automatically configures VS Code. For local setup:

1. Install extensions:
   - Python
   - Pylance
   - Black Formatter
   - Ruff

2. VS Code will automatically detect the project configuration from `pyproject.toml`

### PyCharm

1. Open the `projects` directory
2. PyCharm will automatically detect the project structure
3. Configure the Python interpreter to use the virtual environment created by uv

## Next Steps

Now that your environment is set up, continue to [Your First Agent](03-first-agent.md) to create your first Pydantic AI agent!

## Troubleshooting

### uv command not found
Make sure uv is in your PATH. You may need to restart your terminal or add it manually:
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### Docker issues
Ensure Docker Desktop is running before opening the devcontainer.

### Port conflicts
If ports 5432 or 6379 are already in use, modify the port mappings in `.devcontainer/docker-compose.yml`.
