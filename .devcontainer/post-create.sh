#!/bin/bash

echo "Setting up development environment..."

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


cd /workspace

just init # Non interactive mode setup

# Pretty success message
# Uses ANSI colors for terminals that support them
echo -e "\n\033[1;32m+----------------------------------------------+\033[0m"
echo -e "\033[1;32m| ✅  Tooling installation complete!            |\033[0m"
echo -e "\033[1;32m+----------------------------------------------+\033[0m"
echo -e "\033[0;36mTip: run \033[1mjust help\033[0m \033[0;36mfor available commands.\033[0m\n"
echo -e "\033[1;32mFirst Run❓ Execute \033[1mjust init\033[0m \033[0;36m for initial setup.\033[0m"
echo -e "\033[1;32m+----------------------------------------------+\033[0m\n"
