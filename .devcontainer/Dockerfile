FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# Set working directory
WORKDIR /workspace

# Create non-root user (idempotent)
RUN if ! id -u vscode >/dev/null 2>&1; then \
    useradd -m -s /bin/bash vscode && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
  fi

USER vscode
