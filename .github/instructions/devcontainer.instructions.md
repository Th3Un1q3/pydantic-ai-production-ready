---
description: 'Guidelines for configuring and maintaining development containers in this monorepo'
applyTo: '**/.devcontainer/**'
---

# Dev Container Configuration Guidelines

This instruction file provides guidance on where to configure different aspects of development containers to ensure maintainability, modularity, and performance. Changes should be routed to the appropriate file based on the type of modification.

## Configuration Routing Guidelines

### 1. Language and Runtime Installation
**Location**: `devcontainer.json` - `features` section

Use Dev Container Features for installing programming languages, runtimes, and their package managers.

**Examples**:
- Python: `"ghcr.io/devcontainers/features/python:1": {"version": "3.13"}`
- Node.js: `"ghcr.io/devcontainers/features/node:1": {"version": "22"}`
- Go: `"ghcr.io/devcontainers/features/go:1": {"version": "1.24"}`

**Why here**: Features are reusable, versioned, and maintain compatibility across different base images.

### 2. Operating System Modifications and System Dependencies
**Location**: `Dockerfile`

Use the Dockerfile for:
- Installing system packages (apt, yum, etc.)
- Modifying OS configuration
- Setting up system-level services
- Custom base image modifications

**Examples**:
```dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.14

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*
```

**Why here**: These changes are permanent and affect the container image build, ensuring consistency across all instances.

### 3. Tooling and CLI Installation
**Location**: `.devcontainer/post-create.sh`

Use post-create scripts for:
- Installing development tools and CLIs
- Setting up user-specific configurations
- Installing tools that may change frequently
- Running initialization commands

**Examples**:
```bash
#!/bin/bash

# Install just command runner
if ! command -v just &> /dev/null; then
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
fi

# Install GitHub Copilot CLI
if ! command -v copilot &> /dev/null; then
    curl -fsSL https://gh.io/copilot-install | bash
fi
```

**Why here**: Post-create runs after container creation, allowing for user-specific installations and frequent updates without rebuilding the image.

### 4. VS Code Extensions and Settings
**Location**: `devcontainer.json` - `customizations.vscode` section

Configure:
- VS Code extensions
- Editor settings
- Workspace settings
- Terminal configuration

**Example**:
```json
{
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "GitHub.copilot-chat"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "editor.formatOnSave": true
      }
    }
  }
}
```

### 5. Environment Variables and Secrets
**Location**: Depends on scope
- System-wide: `Dockerfile` (ENV instructions)
- User-specific: `.devcontainer/post-create.sh` or `devcontainer.json` (containerEnv)
- Secrets: Never in code; use environment files or external services

## Best Practices

### Maintainability
- **Modular Features**: Use official Dev Container Features when available instead of custom installations
- **Version Pinning**: Always specify versions for features and tools to ensure reproducibility
- **Documentation**: Comment configurations explaining why certain tools are needed

### Performance
- **Layer Caching**: Order Dockerfile instructions to maximize Docker layer caching
- **Minimal Images**: Use appropriate base images and clean up package caches
- **Lazy Loading**: Install heavy tools in post-create only if needed

### Security
- **Least Privilege**: Run containers as non-root user when possible
- **Clean Up**: Remove unnecessary packages and clear caches in Dockerfiles
- **Validate Sources**: Only install from trusted sources and verify checksums

## Validation Rules

### Feature Validation
Before adding a feature to `devcontainer.json`:
1. Verify the feature exists in the official Dev Containers Features repository
2. Check compatibility with your base image
3. Ensure the feature version is supported
4. Test the feature in your environment

### Dockerfile Validation
- Use multi-stage builds when appropriate
- Include proper error handling
- Test builds locally before committing

### Post-Create Validation
- Make scripts idempotent (safe to run multiple times)
- Include error checking and logging
- Test scripts in isolation

## Common Patterns

### Adding a New Language
1. Check if a Dev Container Feature exists
2. Add to `features` in `devcontainer.json`
3. Configure VS Code extensions if needed
4. Add any language-specific tools to post-create.sh

### Installing System Tools
1. Determine if it's a build-time or runtime dependency
2. For build-time: Add to `Dockerfile`
3. For runtime/development: Add to post-create.sh
4. Update documentation

### Updating Tool Versions
1. Update version numbers in the appropriate file
2. Test the changes
3. Update any dependent configurations
4. Rebuild and verify functionality</content>
<parameter name="filePath">/workspace/.github/instructions/devcontainer.instructions.md
