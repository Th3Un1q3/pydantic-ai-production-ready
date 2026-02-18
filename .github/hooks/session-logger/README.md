---
name: 'Session Logger'
description: 'Logs all Copilot coding agent session activity for audit and analysis'
tags: ['logging', 'audit', 'analytics']
---

# Session Logger Hook

Comprehensive logging for GitHub Copilot coding agent sessions, tracking session starts, ends, and user prompts for audit trails and usage analytics.

## Overview

This hook provides detailed logging of Copilot coding agent activity:
- Session start/end times with working directory context
- User prompt submission events
- Configurable log levels

## Features

- **Session Tracking**: Log session start and end events
- **Prompt Logging**: Record when user prompts are submitted
- **Structured Logging**: JSON format for easy parsing
- **Privacy Aware**: Configurable to disable logging entirely

## Installation

1. Copy this hook folder to your repository's `.github/hooks/` directory:
   ```bash
   cp -r hooks/session-logger .github/hooks/
   ```

2. Create the logs directory:
   ```bash
   mkdir -p logs/copilot
   ```

3. Ensure scripts are executable:
   ```bash
   chmod +x .github/hooks/session-logger/*.sh
   ```

4. Commit the hook configuration to your repository's default branch

## Log Format

Session events are written to `logs/copilot/session.log` and prompt events to `logs/copilot/prompts.log` in JSON format:

```json
{"timestamp":"2024-01-15T10:30:00Z","event":"sessionStart","cwd":"/workspace/project"}
{"timestamp":"2024-01-15T10:35:00Z","event":"sessionEnd"}
```

Additionally, full conversation content for each session is persisted to per-session NDJSON files under `logs/copilot/sessions/`.
Each file is newline-delimited JSON (NDJSON) with one event per line. Example entries:

```json
{"timestamp":"2024-01-15T10:30:00Z","event":"sessionStart","sessionId":"sess-...","cwd":"/workspace/project"}
{"timestamp":"2024-01-15T10:31:12Z","event":"message","sessionId":"sess-...","message":{"role":"user","content":"Please refactor my function."}}
{"timestamp":"2024-01-15T10:31:15Z","event":"message","sessionId":"sess-...","message":{"role":"assistant","content":"Here's a refactored version..."}}
{"timestamp":"2024-01-15T10:35:00Z","event":"sessionEnd","sessionId":"sess-..."}
```

Use the `sessions` files for audit, analysis, or replaying conversations. Remember to add `logs/` to `.gitignore` to avoid committing sensitive conversation data.

## Privacy & Security

- Add `logs/` to `.gitignore` to avoid committing session data
- Use `LOG_LEVEL=ERROR` to only log errors
- Set `SKIP_LOGGING=true` environment variable to disable
- Logs are stored locally only
