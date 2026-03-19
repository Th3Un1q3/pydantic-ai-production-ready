#!/bin/bash

echo "Setting up development environment..."

if [ -f /workspace/.env.example ] && [ ! -f /workspace/.env ]; then
    cp /workspace/.env.example /workspace/.env
    echo "Created /workspace/.env from .env.example"
fi

# Install just command runner
# Note: Using official installer from just.systems (standard practice)
# Alternative: Install from package manager when available
if ! command -v just &> /dev/null; then
    echo "Installing just..."
    mkdir -p ~/.local/bin
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install uv if not already installed
# Note: Using official installer from astral.sh (uv maintainers)
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Install GitHub Copilot CLI if not already installed
if ! command -v copilot &> /dev/null; then
    echo "Installing GitHub Copilot CLI..."
    curl -fsSL https://gh.io/copilot-install | bash
fi

# Install markdownlint-cli for automatic markdown linting
if ! command -v markdownlint &> /dev/null; then
    echo "Installing markdownlint-cli..."
    npm install -g markdownlint-cli
fi

cd /workspace

just init # Non interactive mode setup

# Configure git to use merge strategy for reconciliation
git config --global pull.rebase false

# Configure git user name/email:
# - use GIT_USER_NAME / GIT_USER_EMAIL env vars if present (overrides)
# - otherwise set reasonable defaults only if not already configured (do not overwrite)
if [ -n "$GIT_USER_NAME" ]; then
    git config --global user.name "$GIT_USER_NAME"
    echo "Configured git user.name from GIT_USER_NAME"
fi
if [ -n "$GIT_USER_EMAIL" ]; then
    git config --global user.email "$GIT_USER_EMAIL"
    echo "Configured git user.email from GIT_USER_EMAIL"
fi
if ! git config --global user.name >/dev/null 2>&1; then
    git config --global user.name "devcontainer"
    echo "Set default git user.name to 'devcontainer' (override with GIT_USER_NAME)"
fi
if ! git config --global user.email >/dev/null 2>&1; then
    git config --global user.email "devcontainer@users.noreply.github.com"
    echo "Set default git user.email to 'devcontainer@users.noreply.github.com' (override with GIT_USER_EMAIL)"
fi

# Pretty success message
# Uses ANSI colors for terminals that support them
echo -e "\n\033[1;32m+----------------------------------------------+\033[0m"
echo -e "\033[1;32m| ✅  Tooling installation complete!            |\033[0m"
echo -e "\033[1;32m+----------------------------------------------+\033[0m"
echo -e "\033[0;36mTip: run \033[1mjust help\033[0m \033[0;36mfor available commands.\033[0m\n"
echo -e "\033[1;32mFirst Run❓ Execute \033[1mjust init\033[0m \033[0;36m for initial setup.\033[0m"
echo -e "\033[1;32m+----------------------------------------------+\033[0m\n"
