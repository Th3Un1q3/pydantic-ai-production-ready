---
agent: 'agent'
description: 'Create a professional specification document through guided discovery'
tools: ['vscode/askQuestions', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'context7/*', 'gh_readonly/*', 'todo']
argument-hint: 'Optionally specify the type: feature, package, learning, or change'
---

# Write Specification

Create a comprehensive specification document using the [.github/instructions/spec-writing.instructions.md](.github/instructions/spec-writing.instructions.md) instruction module.

## Orchestration Strategy

This prompt decomposes spec writing into discrete subtasks:

1. **Discovery** → Track progress in the specification file itself (file-based for human-in-loop persistence)
2. **Research** → Use `agent/runSubagent` to explore codebase for context
3. **Drafting** → Use `agent/runSubagent` to populate template from instruction module
4. **Validation** → Track quality checklist in the specification file

## Agentic Tools Usage

### File-Based Progress Tracking

Create the specification file early to track progress persistently:

```markdown
## Specification Progress
- [ ] Complete discovery phase
- [ ] Determine specification type
- [ ] Draft specification from template
- [ ] Validate against quality standards
- [ ] Finalize specification

## Discovery Notes
(Capture answers here for persistence across sessions)
```

### Subtask Delegation

Use `agent/runSubagent` for parallel/specialized work:

| Subtask | Agent Purpose |
|---------|---------------|
| Codebase exploration | Find existing patterns, similar implementations |
| Template population | Read instruction module template and generate draft |
| Quality validation | Check criteria against standards |

### GitHub Read-only (when to use)

- Use the `gh_readonly/*` toolset during Research and Discovery to locate related GitHub artifacts (issues, PRs, commits, file history, and releases) that affect the spec's scope or reveal existing work.
- Typical calls: `gh_readonly_list_issues`, `gh_readonly_list_pull_requests`, `gh_readonly_get_commit`, `gh_readonly_get_file_contents`, `gh_readonly_get_release_by_tag`.
- Suggested pattern: search for PRs/issues by spec keywords or affected file paths, then fetch commit diffs or file contents for candidates and summarize relevance in the Research notes.


## Workflow

Follow the workflow defined in [.github/instructions/spec-writing.instructions.md](.github/instructions/spec-writing.instructions.md):

1. **Discovery Phase** - Ask clarifying questions (see instruction module for question list)
2. **Type Selection** - Choose template based on work type
3. **Drafting** - Populate template with prioritized stories (P1, P2, P3) and parallel markers [P]
4. **Clarification** - Mark unclear items with `NEEDS CLARIFICATION:` and resolve before finalizing
5. **Validation** - Verify against instruction module's quality checklist
6. **Save** - Store to `specs/{type}/SPEC-{id}-{title}.md`

## Key Concepts from spec-kit

- **Prioritized User Stories**: Order by importance (P1 = MVP, P2, P3)
- **Independent Testing**: Each story testable as standalone MVP
- **Parallel Markers [P]**: Tasks that can run simultaneously
- **NEEDS CLARIFICATION**: Explicit markers for unclear items
- **Checkpoints**: Validation points after each story phase

## Next Steps

After the specification is created, inform the user:

> Specification saved to `specs/{type}/SPEC-{id}-{title}.md`
>
> To implement this specification, use `/implement-spec` or follow the [.github/instructions/spec-navigating.instructions.md](.github/instructions/spec-navigating.instructions.md) and [.github/instructions/spec-implementation.instructions.md](.github/instructions/spec-implementation.instructions.md) modules.
