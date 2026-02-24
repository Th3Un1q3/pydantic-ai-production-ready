---
description: Guide to setting up the development environment for Pydantic AI, including technical setup, environment variables, and troubleshooting tips.
tags:
  - status:published
  - verified:false
references:
  previous: "./01-introduction.md"
  next: "./03-agent-anatomy.md"
---

# Environment Setup

Set up your development environment for working with Pydantic AI.

## Quick technical and environment setup

Follow the steps in [Getting Started Guide](../../GETTING_STARTED.md) to set up the devcontainer and initialize the project.

## Environment Variables

The primary `.env` and API-key instructions are in `GETTING_STARTED.md`. Add an `OPEN_ROUTER_API_KEY` if you plan to use OpenRouter (recommended for development to avoid vendor lock-in and to access free dev models).

### Docker issues

Ensure Docker Desktop is running before opening the devcontainer.

### Port conflicts

If ports 5432 or 6379 are already in use, modify the port mappings in `.devcontainer/docker-compose.yml`.

## What's next?

After setting up your environment, proceed to the next lesson: [Building Your First Type-Safe Agent](./03-agent-anatomy.md).
