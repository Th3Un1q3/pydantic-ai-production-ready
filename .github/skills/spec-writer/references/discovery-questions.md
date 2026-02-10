# Discovery Questions

Reference guide for gathering complete requirements during the specification discovery phase.

## Core Questions

### Problem & Motivation

| Question | Purpose |
|----------|---------|
| What problem are we solving? | Clarifies the core issue |
| Why is this a priority now? | Understands urgency and context |
| What happens if we don't solve this? | Validates importance |
| Who experiences this problem? | Identifies stakeholders |

### Success Criteria

| Question | Purpose |
|----------|---------|
| How will we know this succeeded? | Defines measurable outcomes |
| What metrics should improve? | Quantifies success |
| What does "done" look like? | Sets completion criteria |
| What's the minimum viable outcome? | Establishes MVP scope |

### Scope & Boundaries

| Question | Purpose |
|----------|---------|
| What's explicitly included? | Clarifies scope |
| What's explicitly excluded? | Prevents scope creep |
| What assumptions are we making? | Surfaces hidden risks |
| What dependencies exist? | Identifies blockers |

### Constraints

| Question | Purpose |
|----------|---------|
| What technology constraints exist? | Limits solution space |
| What timeline are we targeting? | Sets delivery expectations |
| What resources are available? | Scopes effort |
| Are there compliance/security needs? | Identifies requirements |

## Type-Specific Questions

### Feature Specifications

- Which package will this feature belong to?
- What existing functionality will it interact with?
- Are there API contracts to maintain?
- What backward compatibility is required?

### Package Specifications

- What is the package's primary responsibility?
- How does it fit into the monorepo?
- What shared utilities should it use?
- What patterns from existing packages should it follow?

### Learning Module Specifications

- What prerequisites should learners have?
- What concepts will this module teach?
- What hands-on exercises are needed?
- How does it connect to other modules?

### Change Specifications

- What current behavior needs to change?
- What code/files are affected?
- Is this a breaking change?
- What migration path is needed?

## Anti-Patterns

### Questions to Avoid

| Anti-Pattern | Problem | Better Alternative |
|--------------|---------|-------------------|
| "Do you want feature X?" | Leading question | "What problem are you trying to solve?" |
| "Should it be fast?" | Vague | "What response time is acceptable?" |
| "Is this important?" | Yes/no | "How does this compare to other priorities?" |

### Signs of Incomplete Discovery

- No specific success metrics mentioned
- "It should just work" without criteria
- Stakeholders not identified
- Dependencies unknown
- Timeline undefined

## Discovery Checklist

Before proceeding to drafting, verify:

```markdown
## Discovery Complete

- [ ] Problem clearly articulated
- [ ] At least 3 success criteria with metrics
- [ ] Scope boundaries defined
- [ ] Non-goals explicitly stated
- [ ] Technical constraints known
- [ ] Timeline discussed
- [ ] Dependencies identified
- [ ] Stakeholders confirmed
```
