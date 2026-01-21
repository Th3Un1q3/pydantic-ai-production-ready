# Internal Support Agent

An AI-powered agent for handling internal company support queries.

## Overview

This package provides an intelligent support agent that can:
- Handle IT support requests
- Answer HR policy questions
- Create structured support tickets
- Prioritize and escalate issues

## Installation

From the workspace root:

```bash
cd projects
uv sync --package internal-support-agent
```

## Usage

```python
from internal_support_agent import InternalSupportAgent

agent = InternalSupportAgent()
ticket = await agent.process_query("I can't access the VPN")
print(ticket.title, ticket.priority)
```

## Running the Demo

```bash
cd projects
uv run --package internal-support-agent python -m src.agent
```

## Features

- **Automatic Categorization**: IT, HR, Finance, General
- **Priority Assignment**: Low, Medium, High, Urgent
- **Smart Escalation**: Identifies issues requiring human intervention
- **Structured Tickets**: Consistent ticket format for tracking

## Dependencies

- OpenAI or compatible LLM API
- pydantic-ai-shared (workspace package)

## Configuration

Set environment variables in `projects/.env`:

```bash
OPENAI_API_KEY=your_key_here
```
