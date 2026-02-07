---
agent: 'agent'
description: 'Create a professional specification document. Guides through discovery phase and produces a comprehensive spec for features, packages, learning modules, or changes.'
tools: ['agent/runSubagent', 'todos']
---

# Write Specification

Create a comprehensive specification document using the [spec-writer skill](../skills/spec-writer/SKILL.md).

## Orchestration Strategy

This prompt decomposes spec writing into discrete subtasks:

1. **Discovery** → Track progress in the specification file itself (file-based for human-in-loop persistence)
2. **Research** → Use `agent/runSubagent` to explore codebase for context
3. **Drafting** → Use `agent/runSubagent` to populate template from skill
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
| Template population | Read skill template and generate draft |
| Quality validation | Check criteria against standards |

## Workflow

Follow the workflow defined in [spec-writer skill](../skills/spec-writer/SKILL.md):

1. **Discovery Phase** - Ask clarifying questions (see skill for question list)
2. **Type Selection** - Choose template based on work type
3. **Drafting** - Populate template from skill's templates directory
4. **Validation** - Verify against skill's quality checklist
5. **Save** - Store to `specs/{type}/SPEC-{id}-{title}.md`

## Next Steps

After the specification is created, inform the user:

> Specification saved to `specs/{type}/SPEC-{id}-{title}.md`
>
> To implement this specification, use `/implement-spec` or invoke the spec-implementer skill.
