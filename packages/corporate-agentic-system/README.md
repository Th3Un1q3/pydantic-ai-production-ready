# Corporate Agentic System

A sophisticated multi-agent system for corporate operations and workflow automation.

## Overview

This package provides a multi-agent orchestrator that coordinates specialized agents for:
- **Document Processing**: Analysis, summarization, extraction
- **Meeting Management**: Scheduling, agenda creation, note-taking
- **Workflow Automation**: Task planning, assignment, tracking
- **Analytics**: Data insights and reporting

## Architecture

```
Corporate Orchestrator
├── Planning Agent       # Analyzes and breaks down requests
├── Document Agent      # Handles document operations
├── Scheduling Agent    # Manages meetings and calendars
└── Analytics Agent     # Provides data insights
```

## Installation

From the workspace root:

```bash
cd projects
uv sync --package corporate-agentic-system
```

## Usage

```python
from corporate_agentic_system import CorporateOrchestrator, CorporateContext

orchestrator = CorporateOrchestrator()
context = CorporateContext(
    user_role="manager",
    department="engineering"
)

workflow = await orchestrator.plan_workflow(
    "Prepare quarterly business review",
    context
)
```

## Running the Demo

```bash
cd projects
uv run --package corporate-agentic-system python -m src.orchestrator
```

## Features

- **Multi-Agent Coordination**: Specialized agents work together
- **Context-Aware**: Considers user role and department
- **Workflow Planning**: Breaks complex requests into tasks
- **Priority Management**: Handles task prioritization
- **Flexible Models**: Supports multiple LLM providers

## Dependencies

This system uses Anthropic's Claude by default for enhanced reasoning,
but supports other providers through configuration.

## Configuration

Set environment variables in `projects/.env`:

```bash
# Anthropic (recommended for corporate use)
ANTHROPIC_API_KEY=your_key_here

# Or use OpenAI
OPENAI_API_KEY=your_key_here
```

## Use Cases

1. **Quarterly Reviews**: Automate metric collection and presentation prep
2. **Project Planning**: Break down initiatives into actionable tasks
3. **Document Management**: Analyze and organize corporate documents
4. **Meeting Coordination**: Schedule and prepare for team meetings
