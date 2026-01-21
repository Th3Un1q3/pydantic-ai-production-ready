# Pydantic AI Production Ready - Command System
# Run `just` or `just --list` to see all available commands

# Default recipe to display help
default:
    @just --list

# Show detailed help with examples
help:
    @echo "Pydantic AI Production Ready - Command System"
    @echo ""
    @echo "Available commands:"
    @echo "  just install [PACKAGE]     - Install dependencies (all or specific package)"
    @echo "  just start [PACKAGE]       - Start project (installs if needed)"
    @echo "  just test [PACKAGE]        - Run tests (all or specific package)"
    @echo "  just format [PACKAGE]      - Format code"
    @echo "  just lint [PACKAGE]        - Lint code"
    @echo "  just clean                 - Clean build artifacts"
    @echo ""
    @echo "Examples:"
    @echo "  just install                           # Install all packages"
    @echo "  just install internal-support-agent    # Install specific package"
    @echo "  just start corporate-agentic-system    # Start corporate system"
    @echo "  just test                              # Test all packages"
    @echo "  just test shared                       # Test shared package"
    @echo ""
    @echo "Package shortcuts:"
    @echo "  just install-shared, just install-support, just install-corporate"
    @echo "  just start-shared, just start-support, just start-corporate"
    @echo "  just test-shared, just test-support, just test-corporate"

# ============================================================================
# Installation Commands
# ============================================================================

# Install all packages
install-all:
    @echo "📦 Installing all packages..."
    cd projects && uv sync
    @echo "✅ All packages installed"

# Install specific package
install PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    cd /home/runner/work/pydantic-ai-production-ready/pydantic-ai-production-ready
    if [ "{{PACKAGE}}" = "all" ]; then
        just install-all
    elif [ "{{PACKAGE}}" = "shared" ]; then
        just install-shared
    elif [ "{{PACKAGE}}" = "internal-support-agent" ] || [ "{{PACKAGE}}" = "support" ]; then
        just install-support
    elif [ "{{PACKAGE}}" = "corporate-agentic-system" ] || [ "{{PACKAGE}}" = "corporate" ]; then
        just install-corporate
    else
        echo "❌ Unknown package: {{PACKAGE}}"
        echo "Available: shared, internal-support-agent (support), corporate-agentic-system (corporate)"
        exit 1
    fi

# Install shared package
install-shared:
    @echo "📦 Installing shared package..."
    cd projects && uv sync --package pydantic-ai-shared
    @echo "✅ Shared package installed"

# Install internal-support-agent
install-support:
    @echo "📦 Installing internal-support-agent..."
    cd projects && uv sync --package internal-support-agent
    @echo "✅ Internal-support-agent installed"

# Install corporate-agentic-system
install-corporate:
    @echo "📦 Installing corporate-agentic-system..."
    cd projects && uv sync --package corporate-agentic-system
    @echo "✅ Corporate-agentic-system installed"

# ============================================================================
# Start Commands (with implicit installation)
# ============================================================================

# Start a project (installs if needed)
start PACKAGE:
    #!/usr/bin/env bash
    set -euo pipefail
    cd /home/runner/work/pydantic-ai-production-ready/pydantic-ai-production-ready
    
    # Ensure dependencies are installed first
    if [ "{{PACKAGE}}" = "shared" ]; then
        just install-shared
        just _start-shared
    elif [ "{{PACKAGE}}" = "internal-support-agent" ] || [ "{{PACKAGE}}" = "support" ]; then
        just install-support
        just _start-support
    elif [ "{{PACKAGE}}" = "corporate-agentic-system" ] || [ "{{PACKAGE}}" = "corporate" ]; then
        just install-corporate
        just _start-corporate
    else
        echo "❌ Unknown package: {{PACKAGE}}"
        echo "Available: shared, internal-support-agent (support), corporate-agentic-system (corporate)"
        exit 1
    fi

# Internal: Start shared examples (chatbot)
_start-shared:
    @echo "🚀 Starting shared chatbot example..."
    cd projects/packages/shared && uv run python src/examples/chatbot.py

# Internal: Start internal-support-agent
_start-support:
    @echo "🚀 Starting internal-support-agent..."
    cd projects/packages/internal-support-agent && uv run python src/agent.py

# Internal: Start corporate-agentic-system
_start-corporate:
    @echo "🚀 Starting corporate-agentic-system..."
    cd projects/packages/corporate-agentic-system && uv run python src/orchestrator.py

# Convenient aliases for starting projects
start-shared: (start "shared")
start-support: (start "support")
start-corporate: (start "corporate")

# ============================================================================
# Testing Commands
# ============================================================================

# Run tests for all packages
test-all:
    @echo "🧪 Running tests for all packages..."
    cd projects && uv run pytest
    @echo "✅ All tests passed"

# Run tests for specific package or all
test PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    cd /home/runner/work/pydantic-ai-production-ready/pydantic-ai-production-ready
    if [ "{{PACKAGE}}" = "all" ]; then
        just test-all
    elif [ "{{PACKAGE}}" = "shared" ]; then
        just test-shared
    elif [ "{{PACKAGE}}" = "internal-support-agent" ] || [ "{{PACKAGE}}" = "support" ]; then
        just test-support
    elif [ "{{PACKAGE}}" = "corporate-agentic-system" ] || [ "{{PACKAGE}}" = "corporate" ]; then
        just test-corporate
    else
        echo "❌ Unknown package: {{PACKAGE}}"
        echo "Available: shared, internal-support-agent (support), corporate-agentic-system (corporate)"
        exit 1
    fi

# Test shared package
test-shared:
    @echo "🧪 Testing shared package..."
    cd projects/packages/shared && uv run pytest
    @echo "✅ Shared tests passed"

# Test internal-support-agent
test-support:
    @echo "🧪 Testing internal-support-agent..."
    cd projects/packages/internal-support-agent && uv run pytest
    @echo "✅ Internal-support-agent tests passed"

# Test corporate-agentic-system
test-corporate:
    @echo "🧪 Testing corporate-agentic-system..."
    cd projects/packages/corporate-agentic-system && uv run pytest
    @echo "✅ Corporate-agentic-system tests passed"

# ============================================================================
# Code Quality Commands
# ============================================================================

# Format code for all or specific package
format PACKAGE="all":
    #!/usr/bin/env bash
    set -euo pipefail
    cd /home/runner/work/pydantic-ai-production-ready/pydantic-ai-production-ready/projects
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
    cd /home/runner/work/pydantic-ai-production-ready/pydantic-ai-production-ready/projects
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
    cd /home/runner/work/pydantic-ai-production-ready/pydantic-ai-production-ready/projects
    if [ "{{PACKAGE}}" = "all" ]; then
        echo "🔎 Type checking all packages..."
        uv run mypy packages/shared/src packages/internal-support-agent/src packages/corporate-agentic-system/src
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
    find projects -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find projects -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    find projects -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
    find projects -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
    find projects -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
    find projects -type f -name ".coverage" -delete 2>/dev/null || true
    find projects -type f -name "*.pyc" -delete 2>/dev/null || true
    @echo "✅ Cleaned"

# Show project structure
tree:
    @tree projects -L 3 -I '__pycache__|*.pyc|.pytest_cache|.mypy_cache|.ruff_cache' || find projects -type d -maxdepth 3

# Show environment info
info:
    @echo "Environment Information:"
    @echo "========================"
    @python3 --version || echo "Python: not found"
    @uv --version || echo "uv: not found"
    @echo ""
    @echo "Workspace packages:"
    @cd projects && uv tree 2>/dev/null || echo "Run 'just install' first"

# Initialize development environment
init:
    @echo "🚀 Initializing development environment..."
    just install-all
    @echo "✅ Development environment ready"
    @echo ""
    @echo "Try these commands:"
    @echo "  just start support     # Start internal support agent"
    @echo "  just test              # Run all tests"
    @echo "  just help              # Show detailed help"
