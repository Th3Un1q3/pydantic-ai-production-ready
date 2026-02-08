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

## Strategic Tool Selection

The `tools` array constrains which tools the agent can use. Select tools strategically to maximize agent capability.

### Built-in Tool Sets

These are the core tool sets available in VS Code and CLI environments:

| Tool Set | Purpose | Example Tools |
|----------|---------|---------------|
| `vscode` | VS Code integration | `vscode/askQuestions`, `vscode/openFile`, `vscode/showDiff` |
| `execute` | Command execution | Terminal commands, script running |
| `read` | File reading | Read file contents, directory listings |
| `agent` | Agent orchestration | `agent/runSubagent` for task delegation |
| `edit` | File editing | Create, modify, delete files |
| `search` | Code search | Find symbols, references, grep patterns |
| `web` | Web access | Fetch URLs, external documentation |
| `todo` | Task tracking | `todos` for ephemeral progress tracking |

### MCP-Based Tools

MCP (Model Context Protocol) servers extend capabilities. Check `.vscode/mcp.json` for available servers.

| Category | Tools | Use For |
|----------|-------|---------|
| **Context** | `context7/*` | Context-aware code understanding |
| **GitHub** | `gh_readonly/*` | Repository exploration, issue reading |
| **Search** | `tavily/*` | Advanced web search and research |
| **Filesystem** | `filesystem/*` | Advanced file operations |

### Combined Tool Strategy

Combine built-in tools with MCP tools for maximum capability:

| Category | Built-in | MCP Extensions |
|----------|----------|----------------|
| **Subtask Delegation** | `agent/runSubagent`, `todos` | - |
| **User Interaction** | `vscode/askQuestions` | - |
| **Code Understanding** | `read`, `search` | `context7/*` |
| **Repository Access** | `read` | `gh_readonly/*` |
| **External Research** | `web` | `tavily/*` |
| **File Operations** | `edit`, `read` | `filesystem/*` |

### Repository MCP Servers

Check `.vscode/mcp.json` for available MCP servers. Currently configured:

- `context7` - Context-aware code understanding

### Tool Selection by Prompt Type

Select a comprehensive combination of built-in and MCP tools based on prompt requirements:

| Prompt Type | Built-in Tools | MCP Tools |
|-------------|----------------|-----------|
| **Discovery/Spec Writing** | `agent/runSubagent`, `todos`, `vscode/askQuestions` | `context7/*`, `gh_readonly/*`, `web` |
| **Implementation** | `agent/runSubagent`, `todos`, `edit`, `read`, `search` | `context7/*`, `gh_readonly/*`, `web` |
| **Research/Exploration** | `agent/runSubagent`, `read`, `search` | `context7/*`, `gh_readonly/*`, `web`, `tavily/*` |
| **Documentation** | `agent/runSubagent`, `edit`, `read` | `web` |

### Missing MCP Suggestions

Consider adding these MCPs if prompts would benefit:

| MCP | Purpose | Add When |
|-----|---------|----------|
| `tavily/*` | Web search and research | Prompts need external research beyond `web` |
| `filesystem/*` | Advanced file operations | Complex file manipulation needed |

### Common Tool Combinations

For most prompts, combine these built-in and MCP tools:

| Tool | Type | Purpose |
|------|------|---------|
| `agent/runSubagent` | Built-in | Delegate subtasks to specialized agents |
| `todos` | Built-in | Track tasks and checklists (ephemeral, for autonomous work) |
| `vscode/askQuestions` | Built-in | Ask user clarifying questions interactively |
| `read` | Built-in | Read file contents for analysis |
| `edit` | Built-in | Create and modify files |
| `search` | Built-in | Find code patterns and symbols |
| `execute` | Built-in | Run commands and scripts |
| `context7/*` | MCP | Context-aware code understanding |
| `gh_readonly/*` | MCP | Read-only GitHub access (issues, PRs, code) |
| `web` | Built-in | Fetch content from URLs |

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
- Include comprehensive `tools` array - limiting tools reduces agent capability
- Decompose complex work into subtasks
- Use `agent/runSubagent` for specialized or parallel work
- Use `vscode/askQuestions` for prompts requiring user clarification
- See [copilot-instructions.md](../copilot-instructions.md) for decision matrix on `todos` vs file-based checklists

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|------------------|
| `mode: 'agent'` | `agent: 'agent'` |
| Minimal tool list | Comprehensive tools for full capability |
| Monolithic prompts | Decompose into subtasks |
| `todos` for human-in-loop tracking | Use file-based checklists |
| File-based for ephemeral TDD steps | Use `todos` for autonomous cycles |
