# Pydantic AI Production Ready - Command System
# Run `just` or `just --list` to see all available commands

# Default recipe to display help
default:
    @just --list

# Show detailed help with examples
help:
    @echo "Run 'just --list' to see all available commands"
    @echo ""
    @echo "Common usage:"
    @echo "  just install [package]  - Install dependencies"
    @echo "  just start <package>    - Start a project"
    @echo "  just test [package]     - Run tests"
    @echo ""
    @echo "See COMMANDS.md for detailed documentation"

# ============================================================================
# Installation Commands
# ============================================================================

# Install a skill from a GitHub URL. just install-skill https://github.com/anthropics/skills/tree/main/skills/skill-creator
install-skill URL:
    ./scripts/install_skill.sh {{URL}}

# Install all packages or specific package
install PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "📦 Installing all packages..."
        uv sync
        echo "✅ All packages installed"
    elif [ "{{PACKAGE}}" = "shared" ]; then
        echo "📦 Installing shared package..."
        uv sync --package pydantic-ai-shared
        echo "✅ Shared package installed"
    else
        # Use directory name as package name
        PKG_DIR="{{PACKAGE}}"
        if [ ! -d "packages/$PKG_DIR" ]; then
            echo "❌ Package directory not found: packages/$PKG_DIR"
            exit 1
        fi

        echo "📦 Installing {{PACKAGE}}..."
        uv sync --package {{PACKAGE}}
        echo "✅ {{PACKAGE}} installed"
    fi

# ============================================================================
# Start Commands (with implicit installation)
# ============================================================================

# Start a project (installs if needed)
start PACKAGE:
    #!/usr/bin/env bash
    set -euo pipefail

    # Ensure dependencies are installed first
    just install {{PACKAGE}}

    # Use directory name as package name
    PKG_DIR="{{PACKAGE}}"

    if [ ! -d "packages/$PKG_DIR" ]; then
        echo "❌ Package directory not found: packages/$PKG_DIR"
        exit 1
    fi

    # Delegate to package-specific justfile
    cd packages/$PKG_DIR && just start

# ============================================================================
# Testing Commands
# ============================================================================

# Run tests for all packages or specific package
test PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🧪 Running tests for all packages..."
        uv run pytest
        echo "✅ All tests passed"
    else
        # Use directory name as package name
        PKG_DIR="{{PACKAGE}}"

        if [ ! -d "packages/$PKG_DIR" ]; then
            echo "❌ Package directory not found: packages/$PKG_DIR"
            exit 1
        fi

        # Delegate to package-specific justfile
        cd packages/$PKG_DIR && just test
    fi

# ============================================================================
# Code Quality Commands
# ============================================================================

# Format code for all or specific package
format PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🎨 Formatting all packages..."
        uv run black packages/
        echo "✅ All code formatted"
    else
        echo "🎨 Formatting {{PACKAGE}}..."
        uv run black packages/{{PACKAGE}}/
        echo "✅ {{PACKAGE}} formatted"
    fi

# Lint code for all or specific package
lint PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🔍 Linting all packages..."
        uv run ruff check packages/
        echo "✅ All code linted"
    else
        echo "🔍 Linting {{PACKAGE}}..."
        uv run ruff check packages/{{PACKAGE}}/
        echo "✅ {{PACKAGE}} linted"
    fi

# Type check code for all or specific package
typecheck PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🔎 Type checking all packages..."
        uv run mypy packages/*/src
        echo "✅ All code type checked"
    else
        echo "🔎 Type checking {{PACKAGE}}..."
        uv run mypy packages/{{PACKAGE}}/src
        echo "✅ {{PACKAGE}} type checked"
    fi

# Run all quality checks
check PACKAGE="all":
    @echo "🔍 Running all quality checks..."
    just format {{PACKAGE}}
    just lint {{PACKAGE}}
    just typecheck {{PACKAGE}}
    just test {{PACKAGE}}
    @echo "✅ All checks passed"

# ============================================================================
# Utility Commands
# ============================================================================

# Clean build artifacts and cache
clean:
    @echo "🧹 Cleaning build artifacts..."
    @find packages -type d \( -name "__pycache__" -o -name ".pytest_cache" -o -name ".mypy_cache" -o -name ".ruff_cache" -o -name "htmlcov" \) -exec rm -rf {} + 2>/dev/null || true
    @find packages -type f \( -name ".coverage" -o -name "*.pyc" \) -delete 2>/dev/null || true
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
    @echo "Workspace packages:"
    @uv tree 2>/dev/null || echo "Run 'just install' first"


# Opens files needed first
_open_startup_files:
    #!/usr/bin/env bash
    set -euo pipefail

    FILES_TO_CHECK=(.env README.md GETTING_STARTED.md)
    FILES_TO_OPEN=()

    # Build a single list of existing files in the desired order (so .env is last)
    for f in "${FILES_TO_CHECK[@]}"; do
        if [ -f "$f" ]; then
            FILES_TO_OPEN+=("$f")
        fi
    done

    # Open files in editor (prefers VS Code). Maintain order from FILES_TO_CHECK.
    if [ ${#FILES_TO_OPEN[@]} -gt 0 ]; then
        if command -v code >/dev/null 2>&1; then
            code "${FILES_TO_OPEN[@]}" || true
        elif command -v editor >/dev/null 2>&1; then
            editor "${FILES_TO_OPEN[@]}" || true
        else
            echo "💡 Tip: open the following files in your editor:"
            for file in "${FILES_TO_OPEN[@]}"; do
                echo "  - $file"
            done
        fi
    fi


_create_env_file:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ ! -f .env ]; then
        echo "Creating .env file from .env.example..."
        cp .env.example .env
        echo "✅ .env file created"
    else
        echo ".env file already exists. Skipping creation."
    fi

# Initialize development environment
init:
    #!/usr/bin/env bash
    set -euo pipefail
    just _create_env_file
    just _open_startup_files

    echo "✅ Development environment ready"
    echo ""
    echo "Try these commands:"
    echo "  just start support     # Start internal support agent"
    echo "  just test              # Run all tests"
    echo "  just help              # Show detailed help"

