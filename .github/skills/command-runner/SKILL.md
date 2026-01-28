---
name: command-runner
description: Guide for using the `just` command runner to manage and execute tasks, start agents, and run tests. Use this skill when the user asks about running commands, starting agents/services, testing packages, checking code quality, or managing dependencies in the monorepo.
---

# Command Runner Skill

This project uses [just](https://github.com/casey/just) as a command runner for consistent, discoverable task execution. It leverages **uv workspaces** for efficient dependency management.

## Essential Commands

### 1. Setup & Installation

Initialize the environment and install dependencies:

```bash
just init        # Initialize environment (first time setup)
just install     # Sync all workspace dependencies
```

### 2. Discovery

Find available commands and project info:

```bash
just             # List all commands
just tree        # Show project structure
just info        # Show environment info
```

### 3. Running Agents & Packages

Start a specific package or agent. Dependencies are checked automatically.

```bash
just start <package>
```

Examples:

- `just start support` (starts `internal-support-agent`)
- `just start corporate` (starts `corporate-agentic-system`)

### 4. Testing

Run tests with `pytest`.

```bash
just test              # Test all packages
just test <package>    # Test specific package
```

Examples:

- `just test shared`
- `just test support`

### 5. Quality Assurance

Format, lint, and type check code.

```bash
just format      # Format code (black)
just lint        # Lint code (ruff)
just check       # Run all checks (format + lint + typecheck + test)
```

You can also run these for specific packages: `just check support`

## Package Management

### Aliases

Common packages have short aliases for convenience:

- `support` → `internal-support-agent`
- `corporate` → `corporate-agentic-system`
- `shared` → `shared`

## Extension

### Adding Custom Commands

Edit the `justfile` to add new commands:

```just
# Custom command example
my-command:
    @echo "Running my custom command..."
    # Your command here
```

Keep commands discoverable and modular.

## Troubleshooting

- **`just: command not found`**: Install `just` (see `COMMANDS.md` or https://just.systems).
- **`uv: command not found`**: Install `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`.
- **Dependencies not installed**: Run `just init`.
- **Tests failing**: Ensure env is synced (`just install`) and `.env` exists.

## Integration

The justfile works seamlessly in DevContainer. The `postCreateCommand` usually handles `just init` to prepare the environment.

## Architecture Note

- The root `justfile` manages the workspace.
- `uv` handles dependency resolution and virtual environments centrally.
- Running `just start <package>` automatically ensures the environment is up-to-date.
