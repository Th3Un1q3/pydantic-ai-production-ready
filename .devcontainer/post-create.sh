#!/bin/bash

echo "Setting up development environment..."

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Sync Python dependencies using uv
echo "Installing Python dependencies..."
cd /workspace/projects
uv sync

echo "Development environment setup complete!"
