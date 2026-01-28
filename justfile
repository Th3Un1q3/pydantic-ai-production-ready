# Pydantic AI Production Ready - Command System
# Run `just` or `just --list` to see all available commands

set dotenv-load := true

# Default recipe to display help
default:
    @just --list

# Show detailed help with examples
help:
    @echo "Run 'just --list' to see all available commands"
    @echo ""
    @echo "Common usage:"
    @echo "  just install            - Sync workspace dependencies"
    @echo "  just start <package>    - Start a project (e.g. just start internal-support-agent)"
    @echo "  just test [package]     - Run tests"
    @echo ""
    @echo "See COMMANDS.md for detailed documentation"

# ============================================================================
# Installation Commands
# ============================================================================

# Install a skill from a GitHub URL
install-skill URL:
    ./scripts/install_skill.sh {{URL}}

# Sync workspace dependencies (uv sync)
install:
    @echo "📦 Syncing workspace environment..."
    uv sync
    @echo "✅ Workspace synced"

# ============================================================================
# Generic Package Commands (Delegate to package justfiles)
# ============================================================================

# Start a specific package by directory name
start PACKAGE:
    #!/usr/bin/env bash
    set -euo pipefail
    
    # Alias mapping
    target="{{PACKAGE}}"
    if [[ "$target" == "support" ]]; then target="internal-support-agent"; fi
    if [[ "$target" == "corporate" ]]; then target="corporate-agentic-system"; fi
    
    # Check if directory exists
    if [ ! -d "packages/$target" ]; then
        echo "❌ Package '$target' not found in packages/"
        echo "Available packages:"
        ls packages
        exit 1
    fi

    echo "🚀 Delegating to packages/$target..."
    cd packages/$target && just start

# Run tests for all packages or specific package
test PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🧪 Running tests for workspace..."
        uv run pytest
        echo "✅ All tests passed"
    else
        target="{{PACKAGE}}"
        if [[ "$target" == "support" ]]; then target="internal-support-agent"; fi
        if [[ "$target" == "corporate" ]]; then target="corporate-agentic-system"; fi
        
        if [ ! -d "packages/$target" ]; then
            echo "❌ Package '$target' not found in packages/"
            exit 1
        fi
        
        echo "🧪 Testing $target..."
        cd packages/$target && just test
        echo "✅ $target tests passed"
    fi

# Format code
format PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🎨 Formatting workspace..."
        uv run black packages/
    else
        echo "🎨 Formatting {{PACKAGE}}..."
        uv run black packages/{{PACKAGE}}/
    fi

# Lint code
lint PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🔍 Linting workspace..."
        uv run ruff check packages/
    else
        echo "🔍 Linting {{PACKAGE}}..."
        uv run ruff check packages/{{PACKAGE}}/
    fi

# Type check
typecheck PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🔎 Type checking workspace..."
        uv run mypy packages/
    else
        echo "🔎 Type checking {{PACKAGE}}..."
        uv run mypy packages/{{PACKAGE}}/
    fi

# Run all quality checks
check:
    @echo "🔍 Running all quality checks..."
    just format
    just lint
    just typecheck
    just test
    @echo "✅ All checks passed"

# ============================================================================
# Utility Commands
# ============================================================================

# Clean build artifacts
clean:
    @echo "🧹 Cleaning build artifacts..."
    @find . -type d \( -name "__pycache__" -o -name ".pytest_cache" -o -name ".mypy_cache" -o -name ".ruff_cache" -o -name "htmlcov" \) -exec rm -rf {} + 2>/dev/null || true
    @find . -type f \( -name ".coverage" -o -name "*.pyc" \) -delete 2>/dev/null || true
    @echo "✅ Cleaned"

# Show project structure
tree:
    @tree packages -L 3 -I '__pycache__|*.pyc|.pytest_cache|.mypy_cache|.ruff_cache|htmlcov' 2>/dev/null || find packages -type d -maxdepth 3 ! -path "*/\.*" ! -path "*/__pycache__" ! -path "*/.pytest_cache" ! -path "*/.mypy_cache" ! -path "*/.ruff_cache" ! -path "*/htmlcov"

# Show environment info
info:
    @echo "Environment Information:"
    @echo "========================"
    @python3 --version || echo "Python: not found"
    @uv --version || echo "uv: not found"
    @echo ""
    @echo "Workspace status:"
    @uv tree --depth 1 2>/dev/null || echo "Run 'just install' first"

_create_env_file:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -f .env ]; then
        if [ -f .env.example ]; then
            echo "Creating .env file from .env.example..."
            cp .env.example .env
            echo "✅ .env file created"
        else
            echo "⚠️  .env.example not found, skipping .env creation"
        fi
    fi

_open_startup_files:
    #!/usr/bin/env bash
    set -euo pipefail
    FILES=(.env README.md GETTING_STARTED.md)
    for f in "${FILES[@]}"; do
        if [ -f "$f" ]; then
            if command -v code >/dev/null 2>&1; then code "$f" || true; fi
        fi
    done

# Initialize development environment
init:
    just _create_env_file
    just install
    just _open_startup_files
    @echo ""
    @echo "✅ Development environment ready"
