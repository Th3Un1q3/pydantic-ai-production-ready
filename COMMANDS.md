# Command System Guide

This repository uses [just](https://github.com/casey/just) as a command runner for consistent, discoverable task execution across all projects.

## Why `just`?

- **Discoverability**: Run `just` or `just --list` to see all available commands
- **Modularity**: Commands delegate to package-specific implementations
- **Consistency**: All commands follow the same predictable structure
- **Ease of Use**: Dependencies are handled automatically
- **Focus**: Only essential commands are included

## Installation

### Install `just`

**macOS/Linux**:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
```

**macOS (Homebrew)**:
```bash
brew install just
```

**Ubuntu/Debian**:
```bash
wget -qO - 'https://proget.makedeb.org/debian-feeds/prebuilt-mpr.pub' | gpg --dearmor | sudo tee /usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg 1> /dev/null
echo "deb [arch=all,$(dpkg --print-architecture) signed-by=/usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg] https://proget.makedeb.org prebuilt-mpr $(lsb_release -cs)" | sudo tee /etc/apt/sources.list.d/prebuilt-mpr.list
sudo apt update
sudo apt install just
```

**Cargo** (any platform with Rust):
```bash
cargo install just
```

## Quick Start

```bash
# See all available commands
just

# Initialize environment (installs all dependencies)
just init

# Install specific package
just install shared
just install support
just install corporate

# Start a project (automatically installs if needed)
just start support
just start corporate

# Run tests
just test
just test shared
just test support

# Code quality
just format
just lint
just check
```

## Command Reference

### Discovery Commands

```bash
# List all commands
just

# Show detailed help
just help

# Show project structure
just tree

# Show environment information
just info
```

### Installation Commands

All installation commands use `uv sync` under the hood.

```bash
# Install all packages
just install
just install-all

# Install specific package
just install shared
just install internal-support-agent
just install corporate-agentic-system

# Package aliases (shorter names)
just install-shared
just install-support
just install-corporate
```

**How it works:**
- Reads workspace configuration from `projects/pyproject.toml`
- Installs package and its dependencies
- Creates virtual environment if needed
- Resolves cross-package dependencies

### Start Commands

Start commands automatically install dependencies if not already installed.

```bash
# Start specific project
just start shared              # Runs chatbot example
just start support             # Runs internal support agent
just start corporate           # Runs corporate agentic system

# Convenient aliases
just start-shared
just start-support
just start-corporate
```

**How it works:**
1. Checks if dependencies are installed
2. Installs if needed (calls `just install-{package}`)
3. Runs the main entry point for the package

**What each command runs:**
- `shared`: Chatbot example (`src/examples/chatbot.py`)
- `support`: Internal support agent demo (`src/agent.py`)
- `corporate`: Corporate system orchestrator (`src/orchestrator.py`)

### Testing Commands

```bash
# Test all packages
just test
just test-all

# Test specific package
just test shared
just test support
just test corporate

# Individual package test shortcuts
just test-shared
just test-support
just test-corporate
```

**How it works:**
- Uses pytest with workspace configuration
- Runs tests in package's `tests/` directory
- Shows coverage reports
- Respects pytest configuration in `pyproject.toml`

### Code Quality Commands

```bash
# Format code
just format              # Format all packages
just format shared       # Format specific package

# Lint code
just lint               # Lint all packages
just lint support       # Lint specific package

# Type check
just typecheck          # Type check all packages
just typecheck corporate # Type check specific package

# Run all checks (format + lint + typecheck + test)
just check              # Check all packages
just check shared       # Check specific package
```

**Tools used:**
- **black**: Code formatting (line length: 100)
- **ruff**: Fast Python linter
- **mypy**: Static type checker
- **pytest**: Testing framework

### Utility Commands

```bash
# Clean build artifacts
just clean

# Show project structure
just tree

# Show environment info
just info

# Initialize development environment
just init
```

## Command Structure

All commands follow a consistent pattern:

### Pattern 1: Action on All or Specific Package

```bash
just <action> [PACKAGE]
```

Examples:
- `just install` → Install all
- `just install shared` → Install shared
- `just test` → Test all
- `just test support` → Test support only

### Pattern 2: Action-Package Shortcuts

```bash
just <action>-<package>
```

Examples:
- `just install-shared` → Install shared package
- `just test-support` → Test support package
- `just start-corporate` → Start corporate system

### Pattern 3: Utility Commands

```bash
just <utility>
```

Examples:
- `just clean` → Clean artifacts
- `just info` → Show environment
- `just help` → Show help

## Package Aliases

For convenience, packages have short aliases:

| Full Name | Alias | Usage |
|-----------|-------|-------|
| `shared` | `shared` | `just install shared` |
| `internal-support-agent` | `support` | `just start support` |
| `corporate-agentic-system` | `corporate` | `just test corporate` |

Both full names and aliases work with all commands.

## Dependency Management

Commands that require other commands to run first will automatically run them:

### Implicit Dependencies

- **`just start <package>`**:
  1. Runs `just install-<package>` (if needed)
  2. Runs the package

- **`just check <package>`**:
  1. Runs `just format <package>`
  2. Runs `just lint <package>`
  3. Runs `just typecheck <package>`
  4. Runs `just test <package>`

This means you can run `just start support` even on a fresh clone, and it will install everything needed automatically.

## Working with Multiple Packages

### Install and test everything

```bash
just init    # Install all packages
just test    # Test all packages
```

### Work on specific package

```bash
# Install only what you need
just install-support

# Make changes, then test
just test-support

# Format and lint
just format support
just lint support

# Run all checks
just check support
```

### Parallel development

Work on multiple packages simultaneously:

```bash
# Terminal 1: Work on support agent
just start support

# Terminal 2: Work on corporate system
just start corporate

# Terminal 3: Run tests continuously
just test
```

## Integration with DevContainer

The justfile works seamlessly in DevContainer:

```jsonc
// .devcontainer/devcontainer.json
{
  "postCreateCommand": "curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin && just init"
}
```

This automatically:
1. Installs `just`
2. Initializes the entire workspace
3. Prepares the development environment

## Best Practices

### 1. Use `just init` on first setup

```bash
# After cloning
git clone <repo>
cd <repo>
just init
```

### 2. Use `just start` instead of manual commands

Instead of:
```bash
cd projects/packages/internal-support-agent
uv sync --package internal-support-agent
uv run python src/agent.py
```

Do:
```bash
just start support
```

### 3. Run `just check` before committing

```bash
# Make changes
just check support

# Or check everything
just check
```

### 4. Use package aliases for speed

```bash
just test-support    # Instead of: just test internal-support-agent
just start-corporate # Instead of: just start corporate-agentic-system
```

### 5. Clean regularly

```bash
# Clean build artifacts
just clean
```

## Troubleshooting

### `just: command not found`

Install just (see Installation section above).

### `uv: command not found`

Install uv first:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Package not found

Make sure you're in the repository root:
```bash
cd /path/to/pydantic-ai-production-ready
just --list
```

### Dependencies not installed

Run:
```bash
just init
```

### Tests failing

1. Ensure dependencies are installed: `just install`
2. Check environment variables: `.env` file configured
3. Run tests with verbose output: `cd projects && uv run pytest -v`

## Extending the Command System

### Adding a New Package

1. Create package directory:
   ```bash
   mkdir -p projects/packages/new-package/{src,tests}
   ```

2. Add to workspace (`projects/pyproject.toml`):
   ```toml
   [tool.uv.workspace]
   members = [
       "packages/shared",
       "packages/internal-support-agent",
       "packages/corporate-agentic-system",
       "packages/new-package",  # Add this
   ]
   ```

3. Update `justfile` with new commands (optional).

The existing `just install`, `just test` commands will work with the new package automatically if you use the full package name.

### Adding Custom Commands

Edit the `justfile` and add your command:

```just
# Custom command example
my-command:
    @echo "Running my custom command..."
    # Your command here
```

Keep it:
- **Discoverable**: Will show up in `just --list`
- **Modular**: Delegate to package-specific scripts
- **Consistent**: Follow existing command patterns
- **Necessary**: Only add if it's genuinely useful

## Examples

### Daily Development Workflow

```bash
# Morning: Update and check
just install
just test

# Work on feature
# ... make changes ...
just test-support

# Before committing
just check support
git add .
git commit -m "feat: add new feature"
```

### Testing Workflow

```bash
# Run specific test file
cd projects/packages/internal-support-agent
uv run pytest tests/test_agent.py -v

# Run all tests with coverage
just test

# Run tests for one package
just test-shared
```

### CI/CD Integration

```yaml
# .github/workflows/test.yml
- name: Install just
  run: curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin

- name: Run tests
  run: just test

- name: Run checks
  run: just check
```

## Comparison with Other Tools

| Tool | Pros | Cons | Why We Use Just |
|------|------|------|-----------------|
| **Make** | Universal, standard | Complex syntax, platform-specific | Just has better syntax |
| **npm scripts** | Node.js ecosystem | Python-specific | Just is language-agnostic |
| **Invoke** | Python-native | Another Python dependency | Just is standalone |
| **just** | Simple, fast, discoverable | Requires installation | Best fit for our needs |

## Resources

- [just Documentation](https://just.systems/)
- [just GitHub Repository](https://github.com/casey/just)
- [justfile Syntax](https://just.systems/man/en/chapter_1.html)

## Summary

The `just` command system provides:

✅ **Discoverability**: Run `just` to see all commands  
✅ **Modularity**: Package-specific implementations  
✅ **Consistency**: Predictable command structure  
✅ **Ease of Use**: Automatic dependency handling  
✅ **Focus**: Only essential commands included  

Start with `just init` and explore with `just --list`!
