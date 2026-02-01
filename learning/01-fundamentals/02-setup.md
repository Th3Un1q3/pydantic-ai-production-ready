# Environment Setup

Set up your development environment for working with Pydantic AI.

## Quick technical setup

Follow the steps in [Getting Started Guide](./GETTING_STARTED.md) to set up the devcontainer and initialize the project.

## Environment Variables

The primary `.env` and API-key instructions are in `GETTING_STARTED.md`. Add an `OPEN_ROUTER_API_KEY` if you plan to use OpenRouter (recommended for development to avoid vendor lock-in and to access free dev models).

## Troubleshooting

### uv command not found
Make sure uv is in your PATH. You may need to restart your terminal or add it manually:
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### Docker issues
Ensure Docker Desktop is running before opening the devcontainer.

### Port conflicts
If ports 5432 or 6379 are already in use, modify the port mappings in `.devcontainer/docker-compose.yml`.
