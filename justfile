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
    @echo "  just copilot-install <URL> - Install a Copilot skill or hook"
    @echo "  just start <package>    - Start a project (e.g. just start course-navigator)"
    @echo "  just test [package]     - Run tests"
    @echo ""
    @echo "See COMMANDS.md for detailed documentation"

# ============================================================================
# Installation Commands
# ============================================================================

# Install a skill or hook from a GitHub URL
copilot-install URL:
    ./scripts/copilot-install.sh {{URL}}

# Copilot sessions utility (generic passthrough)
copilot-sessions +ARGS:
    uv run python scripts/copilot_sessions.py {{ARGS}}

# Copilot sessions utility (list convenience wrapper)
copilot-sessions-list +ARGS:
    uv run python scripts/copilot_sessions.py list {{ARGS}}

# Copilot sessions utility (read convenience wrapper)
copilot-sessions-read ID +ARGS:
    uv run python scripts/copilot_sessions.py read --id {{ID}} {{ARGS}}

# Sync workspace dependencies (uv sync)
install:
    @echo "📦 Syncing workspace environment..."
    uv sync
    @echo "✅ Workspace synced"

# ============================================================================
# Generic Package Commands (Delegate to package justfiles)
# ============================================================================

# Start a specific package by directory name
start PACKAGE +ARGS:
    #!/usr/bin/env bash
    set -euo pipefail

    target="{{PACKAGE}}"
    just _require_package "$target" true
    echo "🚀 Delegating to packages/$target..."
    cd "packages/$target" && just start {{ARGS}}

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
        echo "🧪 Testing $target..."
        just _require_package "$target"
        cd "packages/$target" && just test
        echo "✅ $target tests passed"
    fi

# Format code (MODE: fix|check)
format PACKAGE="all" MODE="fix":
    #!/usr/bin/env bash
    set -euo pipefail

    paths="$(just --quiet _scope_paths "{{PACKAGE}}" true)"
    if [ "{{PACKAGE}}" = "all" ]; then
        scope="workspace"
    else
        scope="{{PACKAGE}}"
    fi

    if [ "{{MODE}}" = "check" ]; then
        echo "🎨 Checking $scope formatting..."
        uv run black --check $paths
    elif [ "{{MODE}}" = "fix" ]; then
        echo "🎨 Formatting $scope..."
        uv run ruff check --fix $paths
        uv run black $paths
    else
        echo "❌ Invalid format mode: {{MODE}} (expected: fix|check)"
        exit 1
    fi

# Lint code (MODE: fix|check)
lint PACKAGE="all" MODE="fix":
    #!/usr/bin/env bash
    set -euo pipefail

    paths="$(just --quiet _scope_paths "{{PACKAGE}}" true)"
    if [ "{{PACKAGE}}" = "all" ]; then
        scope="workspace"
    else
        scope="{{PACKAGE}}"
    fi

    if [ "{{MODE}}" = "check" ]; then
        echo "🔍 Checking $scope lint..."
        uv run ruff check $paths
    elif [ "{{MODE}}" = "fix" ]; then
        echo "🔍 Linting $scope..."
        uv run ruff check --fix $paths
    else
        echo "❌ Invalid lint mode: {{MODE}} (expected: fix|check)"
        exit 1
    fi

# ============================================================================
# Learning Operations
# ============================================================================

# Scaffold a new learning module
learning-init NAME TITLE:
    uv run python scripts/learning/init_learning_structure.py --path ./learning --add-module {{NAME}} --title "{{TITLE}}"

# Validate learning directory structure
learning-validate:
    uv run python scripts/learning/init_learning_structure.py --path ./learning --validate

# Lint markdown files (MODE: fix|check)
lint-md MODE="fix":
    @if [ "{{MODE}}" = "check" ]; then \
        echo "📝 Checking markdown files..."; \
        markdownlint "**/*.md"; \
        echo "✅ Markdown checks passed"; \
    else \
        echo "📝 Linting and fixing markdown files..."; \
        markdownlint --fix "**/*.md"; \
        echo "✅ Markdown files linted"; \
    fi

# Type check
typecheck PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🔎 Type checking workspace..."
    else
        echo "🔎 Type checking {{PACKAGE}}..."
    fi
    paths="$(just --quiet _scope_paths "{{PACKAGE}}" true)"
    uv run mypy $paths

# Run all quality checks
check PACKAGE="all":
    @echo "🔍 Running all quality checks for {{PACKAGE}}..."
    just format "{{PACKAGE}}" fix
    just lint "{{PACKAGE}}" fix
    just typecheck "{{PACKAGE}}"
    just test "{{PACKAGE}}"
    @echo "✅ All checks passed"

# Check formatting without modifying files
format-check PACKAGE="all":
    just format {{PACKAGE}} check

# Non-mutating CI quality gate
check-ci:
    @echo "🔍 Running non-mutating CI checks..."
    just format all check
    just lint all check
    just typecheck all
    just test all
    just lint-md check
    @echo "✅ CI checks passed"

# ============================================================================
# Utility Commands
# ============================================================================

# Sync with remote repository (stash, pull, pop)
repo sync:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "🔄 Syncing with remote repository..."
    if git diff --quiet && git diff --staged --quiet; then
        echo "No local changes to stash."
        git pull --tags origin main
    else
        echo "Stashing local changes..."
        git stash push -m "Auto-stash before sync"
        git pull --tags origin main
        echo "Re-applying stashed changes..."
        git stash pop
    fi
    echo "✅ Synced successfully"

# Clean build artifacts
clean:
    @echo "🧹 Cleaning build artifacts..."
    @find . -type d \( -name "__pycache__" -o -name ".pytest_cache" -o -name ".mypy_cache" -o -name ".ruff_cache" -o -name "htmlcov" \) -exec rm -rf {} + 2>/dev/null || true
    @find . -type f \( -name ".coverage" -o -name "*.pyc" \) -delete 2>/dev/null || true
    @echo "✅ Cleaned"

# List available packages
packages:
    @echo "Available packages:"
    @ls -d packages/*/  | xargs -n1 basename

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



[positional-arguments]
agent-parallel +PROMPT:
    #!/usr/bin/env bash
    set -euo pipefail

    # Delegate to extracted script in /scripts (preserve quoted prompts)
    bash scripts/agent-parallel.sh "$@"

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
    fi

_require_package PACKAGE SHOW_AVAILABLE="false":
    #!/usr/bin/env bash
    set -euo pipefail

    target="{{PACKAGE}}"
    show_available="{{SHOW_AVAILABLE}}"

    if [ ! -d "packages/$target" ]; then
        echo "❌ Package '$target' not found in packages/"
        if [ "$show_available" = "true" ]; then
            echo "Available packages:"
            ls packages
        fi
        exit 1
    fi

_scope_paths PACKAGE INCLUDE_SCRIPTS="false":
    #!/usr/bin/env bash
    set -euo pipefail

    if [ "{{PACKAGE}}" = "all" ]; then
        if [ "{{INCLUDE_SCRIPTS}}" = "true" ]; then
            echo "packages/ scripts/"
        else
            echo "packages/"
        fi
    else
        just _require_package "{{PACKAGE}}"
        echo "packages/{{PACKAGE}}/"
    fi
