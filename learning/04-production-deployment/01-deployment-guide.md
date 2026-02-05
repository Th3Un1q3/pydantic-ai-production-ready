---
description: Deployment guide for individual packages in the monorepo
tags:
  - draft
  - non_validated
  - learning
---


# Deployment Guide

One of the key benefits of the monorepo structure is that each package can be deployed independently.

## Docker Deployment

Since the packages share a workspace and potentially some code (like `packages/shared`), you need to build the Docker context from the root, or carefuly copy the necessary parts.

Here is an example `Dockerfile` for deploying `course-navigator`:

```dockerfile
# Example: Deploy course-navigator
FROM python:3.12
WORKDIR /app

# Copy the workspace configuration
COPY pyproject.toml ./
COPY uv.lock ./

# Copy the shared package (if used)
COPY packages/shared ./packages/shared

# Copy the target package
COPY packages/course-navigator ./packages/course-navigator

# Install dependencies
# We use uv to sync only the target package
RUN pip install uv && uv sync --package course-navigator --frozen

# Set the command to run the application
CMD ["uv", "run", "python", "packages/course-navigator/src/course_navigator/main.py"]
```

## Serverless Deployment

Each package is designed to be small and self-contained, making them suitable for deployment as serverless functions (AWS Lambda, Google Cloud Functions, etc.).

When deploying to serverless:

1. Ensure `packages/shared` is included in the build if it's a dependency.
2. Use a tool (like `zip` or a serverless framework plugin) to package the target package and its dependencies.
