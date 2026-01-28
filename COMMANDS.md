# Command System Guide

This repository uses [just](https://github.com/casey/just) as a command runner for consistent, discoverable task execution across all projects.

## Why `just`?

- **Discoverability**: Run `just` or `just --list` to see all available commands
- **Modularity**: Commands delegate to package-specific implementations
- **Consistency**: All commands follow the same predictable structure
- **Ease of Use**: Dependencies are handled automatically

## Installation

This repository is designed to work with **Dev Containers**, where \`just\` and all other dependencies are pre-installed.

If you are running locally (not recommended), please install \`just\` following the [official documentation](https://just.systems/man/en/chapter_4.html).

## Quick Start

*See `just --list` for all commands.*

```bash
# Initialize environment (installs all dependencies)
just init

# Start a project (automatically installs if needed)
just start support
just start corporate

# Run tests
just test          # All
just test shared   # Specific package

# Code quality
just check         # Format, lint, typecheck, test
```

## Command Reference

### Discovery

- `just`: List commands
- `just tree`: Show project structure
- `just info`: Show environment info

### Development

- `just install [package]`: Sync dependencies
- `just start [package]`: Run the agent/package
- `just test [package]`: Run pytest

### Quality

- `just format`: Code formatting (black)
- `just lint`: Linting (ruff)
- `just typecheck`: Static analysis (mypy)
- `just check`: Run all of the above

## Package Aliases

| Full Name | Alias |
|-----------|-------|
| `shared` | `shared` |
| `internal-support-agent` | `support` |
| `corporate-agentic-system` | `corporate` |
