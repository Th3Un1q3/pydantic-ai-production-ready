---
agent: 'agent'
description: 'Create a professional specification document. Guides through discovery phase and produces a comprehensive spec for features, packages, learning modules, or changes.'
tools: ['agent/runSubagent', 'todos']
---

# Write Specification

Create a comprehensive specification document for a feature, package, learning module, or change.

## Orchestration Strategy

This prompt decomposes spec writing into discrete subtasks:

1. **Discovery** → Use `todos` to track discovery questions
2. **Research** → Use `agent/runSubagent` for codebase exploration
3. **Drafting** → Use `agent/runSubagent` for template population
4. **Validation** → Use `todos` to track quality checklist

## Process

### Step 1: Initialize Task Tracking

Create a TODO list to track progress:

```markdown
## Specification TODO
- [ ] Complete discovery phase
- [ ] Determine specification type
- [ ] Draft specification from template
- [ ] Validate against quality standards
- [ ] Save specification to specs/
```

Use the `todos` tool to maintain this checklist throughout the process.

### Step 2: Discovery

Before writing any specification, gather context by asking:

1. **What are we building?** Get a clear description of the feature, package, module, or change.
2. **Why now?** Understand the problem being solved and its urgency.
3. **How will we measure success?** Define 3-5 measurable KPIs.
4. **What's explicitly out of scope?** Prevent scope creep.
5. **Any constraints?** Technology, timeline, dependencies.

Do NOT proceed until you have clear answers. Ask follow-up questions if needed.

**Subtask**: Use `agent/runSubagent` to explore the codebase for relevant context:
- Existing similar implementations
- Related packages and their patterns
- Testing conventions in use

### Step 3: Type Selection

Based on the user's input, determine the specification type:

| Type | Indicators |
|------|------------|
| `feature` | New functionality for existing package |
| `package` | New package or major component |
| `learning` | Educational content, module, or tutorial |
| `change` | Refactoring, modification, improvement |

### Step 4: Draft Specification

**Subtask**: Use `agent/runSubagent` to:
1. Read the appropriate template from the spec-writer skill
2. Populate template sections based on discovery findings
3. Generate concrete acceptance criteria

Templates:
- [feature.template.md](../.github/skills/spec-writer/templates/feature.template.md)
- [package.template.md](../.github/skills/spec-writer/templates/package.template.md)
- [learning.template.md](../.github/skills/spec-writer/templates/learning.template.md)
- [change.template.md](../.github/skills/spec-writer/templates/change.template.md)

### Step 5: Validate

Use `todos` to track validation checklist:

- [ ] Problem statement is clear and compelling
- [ ] Success criteria are measurable (include specific numbers)
- [ ] All user stories have testable acceptance criteria
- [ ] Technical constraints are documented
- [ ] Out of scope items are explicitly listed
- [ ] Implementation phases are realistic

### Step 6: Save

Save the specification to:

```
specs/{type}/SPEC-{id}-{kebab-case-title}.md
```

Create the specs directory if it doesn't exist.

## Output Quality

**Concrete criteria** (not vague):

```diff
# Bad
- The API should be fast and reliable.

# Good
+ The API must respond within 200ms at p95 under 100 RPS.
```

**Testable acceptance criteria**:

```diff
# Bad
- User can search for courses

# Good
+ Search endpoint returns results within 500ms
+ Results are ranked by relevance score
+ Empty query returns validation error with helpful message
```

## Next Steps

After the specification is created, inform the user:

> Specification saved to `specs/{type}/SPEC-{id}-{title}.md`
>
> To implement this specification, use `/implement-spec` or invoke the spec-implementer skill.
