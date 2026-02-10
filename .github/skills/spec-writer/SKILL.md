---
name: spec-writer
description: Create comprehensive, professional specifications for features, packages, learning modules, or changes. Use when asked to "write a spec", "create a specification", "define requirements", "plan a feature", "design a module", or before starting implementation of any significant change. Produces structured, measurable specifications that guide AI agents through implementation.
---

# Specification Writer

Create production-grade specifications that bridge vision and implementation. Specifications become the single source of truth for AI agents executing the work.

## Overview

This skill generates structured specifications following a discovery-first approach. Every specification includes:

- Clear problem statement and success criteria
- User stories with acceptance criteria (prioritized as P1, P2, P3)
- Technical requirements and constraints
- Implementation phases with validation checkpoints
- Task breakdown with parallel execution markers

## Templates

| Type | Use When | Template |
|------|----------|----------|
| `feature` | New functionality for existing package | [feature.template.md](./templates/feature.template.md) |
| `package` | New package or major component | [package.template.md](./templates/package.template.md) |
| `learning` | New educational module | [learning.template.md](./templates/learning.template.md) |
| `change` | Refactoring or modification | [change.template.md](./templates/change.template.md) |

## Workflow

### Phase 1: Discovery (Required)

Before writing a specification, interrogate to fill knowledge gaps. Do not assume context.

**Discovery Questions:**

1. **Problem**: What problem are we solving? Why now?
2. **Success**: How will we measure success? What are the KPIs?
3. **Scope**: What's in scope? What's explicitly out of scope?
4. **Constraints**: Technology stack, timeline, dependencies?
5. **Users**: Who benefits? What are their needs?

**Action**: Ask clarifying questions until the scope is clear. Never skip discovery.

### Phase 2: Specification Type Selection

Choose the appropriate template based on the work type (see Templates table above).

### Phase 3: Drafting

Generate the specification using the selected template.

**Key Principles:**

- **Prioritized User Stories**: Order stories by importance (P1, P2, P3)
- **Independent Testing**: Each story must be testable as a standalone MVP
- **Parallel Markers**: Mark tasks that can run in parallel with `[P]`
- **NEEDS CLARIFICATION**: Use explicit markers for unclear items

### Phase 4: Clarification (Recommended)

Before planning, run a structured clarification to reduce rework:

```markdown
## Clarification Checklist

For each requirement, confirm:
- [ ] Is the requirement specific enough to implement?
- [ ] Are edge cases identified?
- [ ] Are error scenarios defined?
- [ ] Is the scope boundary clear?
```

Mark unclear items with: `NEEDS CLARIFICATION: {{what's unclear}}`

### Phase 5: Validation

Before finalizing, verify the specification against this checklist:

```markdown
## Validation Checklist
- [ ] Problem statement is clear and compelling
- [ ] Success criteria are measurable
- [ ] All user stories have testable acceptance criteria
- [ ] Stories are prioritized (P1, P2, P3)
- [ ] Each story is independently testable as MVP
- [ ] Technical constraints are documented
- [ ] Out of scope items are explicitly listed
- [ ] Implementation phases have checkpoints
- [ ] Tasks have parallel markers [P] where applicable
- [ ] Dependencies are identified
- [ ] No NEEDS CLARIFICATION markers remain
```

## Quality Standards

**Prioritized User Stories:**

```markdown
### Story 1: [Title] (Priority: P1) 🎯 MVP

As a user, I want to [action] so that [benefit].

**Why this priority**: Core functionality that delivers immediate value
**Independent Test**: Can be tested by [specific action] and delivers [specific value]

**Acceptance Criteria:**
- [ ] Testable criterion 1
- [ ] Testable criterion 2
```

**Concrete, Measurable Criteria:**

```diff
# Vague (BAD)
- The API should be fast and reliable.
- The module should be comprehensive.

# Concrete (GOOD)
+ The API must respond within 200ms at p95 under 100 RPS.
+ The module must cover all 5 core concepts with 3+ exercises each.
```

**Parallel Task Markers:**

```markdown
## Task Breakdown

- [ ] T001 [P] [US1] Create User model in src/models/user.py
- [ ] T002 [P] [US1] Create Auth model in src/models/auth.py
- [ ] T003 [US1] Implement UserService (depends on T001, T002)
```

**Testable Acceptance Criteria:**

Each user story must include acceptance criteria that can be verified:

```markdown
## User Story: Search Results
As a user, I want to search courses by topic so that I can find relevant content.

### Acceptance Criteria
- [ ] Search endpoint returns results within 500ms
- [ ] Results are ranked by relevance score
- [ ] Empty query returns validation error with helpful message
- [ ] Results include title, description, and match score
```

## Output Location

Specifications are stored in:

```
specs/
├── features/
│   └── SPEC-{id}-{title}.md
├── packages/
│   └── SPEC-{id}-{title}.md
├── learning/
│   └── SPEC-{id}-{title}.md
└── changes/
    └── SPEC-{id}-{title}.md
```

**Naming Convention**: `SPEC-{sequential-id}-{kebab-case-title}.md`

Example: `SPEC-001-course-search-api.md`

## Best Practices

| Practice | Rationale |
|----------|-----------|
| **Discovery first** | Specifications written without context lead to rework |
| **Prioritize stories (P1, P2, P3)** | Enables MVP delivery and incremental value |
| **Independent story testing** | Each story can be demo'd/deployed on its own |
| **Mark parallel tasks [P]** | Enables efficient parallel execution |
| **NEEDS CLARIFICATION markers** | Explicit about unknowns, prevents assumptions |
| **Measurable criteria** | Vague requirements cannot be validated |
| **Explicit non-goals** | Prevents scope creep during implementation |
| **Phased delivery with checkpoints** | Enables incremental validation and course correction |
| **Acceptance criteria** | Enables automated and manual validation |
| **Complexity tracking** | Documents violations with justifications |

## Integration

Once a specification is complete, it becomes input for the [spec-implementer](../spec-implementer/SKILL.md) skill.
