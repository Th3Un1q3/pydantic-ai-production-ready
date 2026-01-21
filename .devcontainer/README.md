# DevContainer Configuration

This document explains the VS Code DevContainer setup for the Pydantic AI Production Ready repository.

## Overview

The devcontainer provides a fully-configured, reproducible development environment with:
- Python 3.12
- PostgreSQL database
- Redis cache
- All development tools pre-installed
- VS Code extensions optimized for this project

## Extensions

### Python Development (Core)

**ms-python.python**
- Official Python extension
- Provides IntelliSense, linting, debugging, and testing support
- Essential for Python development

**ms-python.vscode-pylance**
- Fast, feature-rich language server for Python
- Type checking and IntelliSense
- Works with type hints in our codebase

**ms-python.black-formatter**
- Code formatter (configured to 100 char line length)
- Auto-formats on save
- Matches our `pyproject.toml` configuration

**charliermarsh.ruff**
- Fast Python linter (Rust-based)
- Replaces multiple linters (flake8, isort, etc.)
- Configured in `pyproject.toml`

### Configuration Files

**tamasfe.even-better-toml**
- Syntax highlighting for TOML files
- Validation and auto-completion
- Essential for `pyproject.toml` files in monorepo

**mikestead.dotenv**
- Syntax highlighting for `.env` files
- Helps manage environment variables
- Prevents accidental errors in configuration

### Documentation

**yzhang.markdown-all-in-one**
- Comprehensive Markdown support
- Table of contents generation
- Keyboard shortcuts for formatting
- Essential given extensive documentation

**davidanson.vscode-markdownlint**
- Markdown linting and style checking
- Ensures consistent documentation
- Auto-fixes common issues

### Task Runner

**skellock.just**
- Syntax highlighting for `justfile`
- Command suggestions
- Integrates with our task automation

### Git

**mhutchie.git-graph**
- Visual Git history
- Lightweight alternative to GitLens
- Better for monorepo visualization

### AI/ML Development (Optional)

**ms-toolsai.jupyter**
- Jupyter notebook support
- Useful for experimenting with AI agents
- Interactive Python REPL

**ms-toolsai.vscode-jupyter-cell-tags**
- Enhanced Jupyter functionality
- Cell tagging and organization

## Removed Extensions

These extensions were removed as they don't provide significant value for this project:

❌ **ms-azuretools.vscode-docker**
- Reason: Docker is only used for devcontainer itself, not for active development
- Alternatives: Use `docker-compose` CLI when needed

❌ **redhat.vscode-yaml**
- Reason: Minimal YAML usage (only docker-compose.yml)
- Not worth the overhead

❌ **eamodio.gitlens**
- Reason: Feature-heavy, not project-specific
- Alternative: Using lightweight `git-graph` instead
- Note: Users can still install if they prefer

## Settings Configuration

### Python Settings

```json
{
  "python.defaultInterpreterPath": "/usr/local/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.formatting.provider": "black"
}
```

- Uses container's Python 3.12
- Linting via Ruff (not Pylint)
- Formatting via Black

### Editor Settings

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "editor.rulers": [100],
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true
}
```

- Auto-format on save
- Auto-organize imports
- 100-character ruler (matches Black config)
- Clean whitespace
- Consistent line endings

### File Exclusions

```json
{
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.mypy_cache": true,
    "**/.ruff_cache": true
  }
}
```

- Hides build artifacts from file explorer
- Improves performance
- Reduces clutter

## Usage

### First Time Setup

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Install [VS Code](https://code.visualstudio.com/)
3. Install [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
4. Open repository in VS Code
5. Press `F1` → "Dev Containers: Reopen in Container"
6. Wait for setup to complete (~2-5 minutes first time)

### Post-Setup

The devcontainer automatically:
- Installs all VS Code extensions
- Installs `just` command runner
- Installs `uv` package manager
- Runs `just install-all` to set up Python packages
- Starts PostgreSQL and Redis

### Customizing Extensions

To add personal extensions (not shared with team):

1. Open Command Palette (`F1`)
2. Type "Extensions: Add to devcontainer.json"
3. Select extension
4. Choose "Install in workspace" (not in config)

Or edit `.devcontainer/devcontainer.json` and rebuild:
```bash
# Rebuild container
F1 → "Dev Containers: Rebuild Container"
```

## Extension Benefits for This Project

| Extension | Benefit |
|-----------|---------|
| **Pylance** | Fast IntelliSense for Pydantic models and AI agents |
| **Black Formatter** | Consistent code style across monorepo |
| **Ruff** | Fast linting for all packages |
| **Even Better TOML** | Easier editing of `pyproject.toml` files |
| **dotenv** | Prevents errors in `.env` configuration |
| **Markdown All-in-One** | Improves documentation workflow |
| **Markdown Lint** | Maintains documentation quality |
| **Just** | Syntax highlighting for task automation |
| **Git Graph** | Visualizes monorepo commit history |
| **Jupyter** | Interactive experimentation with AI agents |

## Performance Considerations

### Extension Load Time

- **Fast**: Python, Pylance, Black, Ruff (~2s)
- **Medium**: TOML, Markdown, Just (~1s)
- **Slower**: Jupyter (~3s, lazy-loaded)

Total extension load time: ~6 seconds

### Memory Usage

- Base Python extensions: ~150MB
- Documentation extensions: ~50MB
- Optional Jupyter: ~100MB

Total: ~300MB (acceptable for modern systems)

## Troubleshooting

### Extensions Not Installing

1. Rebuild container: `F1` → "Dev Containers: Rebuild Container"
2. Check Docker logs: `docker logs <container-id>`
3. Verify extension IDs in `devcontainer.json`

### Extension Conflicts

If two extensions provide similar functionality:
1. Check extension settings
2. Disable one extension
3. Restart VS Code

### Slow Performance

If extensions slow down VS Code:
1. Disable optional extensions (Jupyter)
2. Check extension resource usage: `F1` → "Developer: Show Running Extensions"
3. Consider using `.vscode/settings.json` to disable specific features

## Comparing to Other Setups

### vs Local Installation

| Aspect | DevContainer | Local |
|--------|-------------|-------|
| **Setup Time** | 5 min | 30+ min |
| **Consistency** | Identical | Varies |
| **Dependencies** | Isolated | Global |
| **OS Support** | Any | Limited |

### vs Codespaces

| Aspect | DevContainer | Codespaces |
|--------|-------------|------------|
| **Cost** | Free | Paid |
| **Speed** | Local | Network |
| **Privacy** | Local | Cloud |
| **Resources** | Your machine | GitHub servers |

## Best Practices

1. **Don't Over-Install**: Only add extensions you actually use
2. **Test Changes**: Rebuild container after modifying config
3. **Document Additions**: Update this file when adding extensions
4. **Consider Team**: Balance personal preference with team consistency
5. **Performance First**: Remove extensions that slow down VS Code

## Future Enhancements

Potential extensions to consider:

- **Error Lens**: Inline error highlighting (if team prefers)
- **GitHub Copilot**: AI code suggestions (optional, paid)
- **Better Comments**: Enhanced comment highlighting (nice-to-have)
- **Todo Tree**: Task tracking in code (if needed)

## Resources

- [VS Code DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)
- [Extension Marketplace](https://marketplace.visualstudio.com/)
