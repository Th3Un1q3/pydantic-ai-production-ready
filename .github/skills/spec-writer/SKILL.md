---
name: spec-writer
description: Create comprehensive, professional specifications for features, packages, learning modules, or changes. Use when asked to "write a spec", "create a specification", "define requirements", "plan a feature", "design a module", or before starting implementation of any significant change. Produces structured, measurable specifications that guide AI agents through implementation.
---

# Specification Writer

Create production-grade specifications that bridge vision and implementation. Specifications become the single source of truth for AI agents executing the work.

## Overview

This skill generates structured specifications following a discovery-first approach. Every specification includes:

- Clear problem statement and success criteria
- User stories with acceptance criteria
- Technical requirements and constraints
- Implementation phases and validation steps

## Operational Workflow

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

Choose the appropriate template based on the work type:

| Type | Use When | Template |
|------|----------|----------|
| `feature` | New functionality for existing package | [feature.template.md](./templates/feature.template.md) |
| `package` | New package or major component | [package.template.md](./templates/package.template.md) |
| `learning` | New educational module | [learning.template.md](./templates/learning.template.md) |
| `change` | Refactoring or modification | [change.template.md](./templates/change.template.md) |

### Phase 3: Drafting

Generate the specification using the selected template. Apply these quality standards:

#### Quality Standards

**Concrete, Measurable Criteria:**

```diff
# Vague (BAD)
- The API should be fast and reliable.
- The module should be comprehensive.

# Concrete (GOOD)
+ The API must respond within 200ms at p95 under 100 RPS.
+ The module must cover all 5 core concepts with 3+ exercises each.
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

### Phase 4: Validation

Before finalizing, verify the specification against this checklist:

```markdown
## Validation Checklist
- [ ] Problem statement is clear and compelling
- [ ] Success criteria are measurable
- [ ] All user stories have testable acceptance criteria
- [ ] Technical constraints are documented
- [ ] Out of scope items are explicitly listed
- [ ] Implementation phases are realistic
- [ ] Dependencies are identified
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
| **Measurable criteria** | Vague requirements cannot be validated |
| **Explicit non-goals** | Prevents scope creep during implementation |
| **Phased delivery** | Enables incremental validation and course correction |
| **Acceptance criteria** | Enables automated and manual validation |

## Integration with Implementation

Once a specification is complete, it becomes input for the [spec-implementer](../spec-implementer/SKILL.md) skill which:

1. Reads the specification
2. Creates an implementation plan
3. Executes in phases with validation
4. Updates documentation
5. Reports completion status

## Quick Reference

```markdown
## Spec Writing Checklist
1. [ ] Run discovery phase with stakeholder
2. [ ] Select appropriate template type
3. [ ] Fill all required sections
4. [ ] Ensure all criteria are measurable
5. [ ] Validate against checklist
6. [ ] Save to specs/{type}/SPEC-{id}-{title}.md
7. [ ] Hand off to spec-implementer or human reviewer
```
