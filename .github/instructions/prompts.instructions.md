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
- Use `agent/runSubagent` for specialized or parallel work

## Progress Tracking: `todos` vs File-Based Checklists

### When to Use `todos` Tool

Use `todos` for **autonomous multi-step tasks** where the agent works without user interruption:

**Good use cases for `todos`:**
- TDD cycle steps (write test → validate fails → implement → validate passes → refactor)
- Build/lint/test validation sequences
- Multi-file refactoring operations
- Sequential code generation steps

**Example - TDD Cycle with `todos`:**
```markdown
Use `todos` to track the TDD cycle:
1. Write failing test for the feature
2. Run test, confirm it fails for the expected reason
3. Write minimal implementation to pass
4. Run test, confirm it passes
5. Refactor implementation while keeping tests green
6. Move to next priority
```

### When to Use File-Based Checklists

Use **file-based checklists** for tracking that must persist across sessions or involves human-in-the-loop:

**Good use cases for file-based checklists:**
- Discovery phases requiring user input
- Deliverables tracking across multiple sessions
- Specification progress (stored in the spec file itself)
- Any workflow where user interruption is expected

**Example - Discovery in Specification File:**
```markdown
## Specification Progress
- [x] Complete discovery phase
- [ ] Determine specification type
- [ ] Draft specification from template
- [ ] Validate against quality standards

## Discovery Notes
(Answers captured here persist across sessions)
```

### Key Distinction

| Scenario | Use `todos` | Use File-Based |
|----------|-------------|----------------|
| Agent works autonomously | ✓ | |
| User may interrupt/resume | | ✓ |
| TDD cycle within a session | ✓ | |
| Tracking deliverables over time | | ✓ |
| Build/test sequences | ✓ | |
| Discovery with user Q&A | | ✓ |

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|------------------|
| `mode: 'agent'` | `agent: 'agent'` |
| Monolithic prompts | Decompose into subtasks |
| `todos` for human-in-loop tracking | Use file-based checklists |
| File-based for ephemeral TDD steps | Use `todos` for autonomous cycles |
