---
description: 'Guidelines for creating reusable prompts for GitHub Copilot'
applyTo: '**/.github/prompts/*.prompt.md'
---

# Prompt File Guidelines

Instructions for creating effective and reusable prompt files for GitHub Copilot.

## Required Frontmatter

Every prompt file must include YAML frontmatter with the following fields:

```yaml
---
agent: 'agent'
description: 'Brief description of what the prompt does'
tools: ['tool1', 'tool2']  # Optional: specific tools to enable
---
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `agent` | Yes | Set to `'agent'` for agentic prompts (standard for all prompts in this repo) |
| `description` | Yes | Clear description of the prompt's purpose (1-200 chars) |
| `tools` | No | Array of tools to enable for this prompt |

### Common Tools

| Tool | Purpose |
|------|---------|
| `agent/runSubagent` | Delegate subtasks to specialized agents |
| `todos` | Track tasks and checklists |
| `edit/editFiles` | Edit files in the workspace |
| `web/fetch` | Fetch content from URLs |

## Prompt Structure

### Orchestration Strategy

For complex prompts, include an orchestration strategy section:

```markdown
## Orchestration Strategy

This prompt decomposes work into discrete subtasks:

1. **Subtask 1** → Use `agent/runSubagent` for exploration
2. **Subtask 2** → Use `todos` for tracking
3. **Subtask 3** → Use `agent/runSubagent` for implementation
```

### Task Decomposition

- Break complex workflows into discrete phases
- Use `todos` to track progress through phases
- Use `agent/runSubagent` for parallel or specialized work

### Process Steps

Number steps clearly and indicate which tools to use:

```markdown
### Step 1: Initialize

Use `todos` to create a tracking checklist.

### Step 2: Execute

Use `agent/runSubagent` to perform specialized work.
```

## Best Practices

- Use `agent: 'agent'` (NOT `mode: 'agent'`)
- Include `tools` array when specific tools are needed
- Decompose complex work into subtasks
- Use `todos` for progress tracking
- Use `agent/runSubagent` for specialized or parallel work

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|------------------|
| `mode: 'agent'` | `agent: 'agent'` |
| Monolithic prompts | Decompose into subtasks |
| No progress tracking | Use `todos` for checklists |
| Manual sequential work | Use `agent/runSubagent` for parallelization |
