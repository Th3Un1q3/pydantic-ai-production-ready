#!/bin/bash

echo "Setting up development environment..."

# Install just command runner
# Note: Using official installer from just.systems (standard practice)
# Alternative: Install from package manager when available
if ! command -v just &> /dev/null; then
    echo "Installing just..."
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | sh -s -- --to ~/.local/bin
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install uv if not already installed
# Note: Using official installer from astral.sh (uv maintainers)
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Sync Python dependencies using uv
echo "Installing Python dependencies..."
cd /workspace
just install-all

echo "Development environment setup complete!"
echo ""
echo "Try these commands:"
echo "  just              # List all available commands"
echo "  just start support # Start internal support agent"
echo "  just test          # Run all tests"
