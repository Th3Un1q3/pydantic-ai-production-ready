---
description: 'Guidance for creating comprehensive specifications including discovery, drafting, and validation.'
applyTo: '**/specs/**/*.md'
---

# Specification Writing

Create production-grade specifications that bridge vision and implementation. Specifications are the single source of truth for execution.

## Discovery Phase

Before writing a specification, interrogate the request to fill knowledge gaps. Never skip discovery.

### Discovery Questions
- **Problem**: What problem are we solving? Why now?
- **Success**: How will we measure success? What are the KPIs?
- **Scope**: What is in scope? What is explicitly out of scope?
- **Constraints**: Technology stack, timeline, dependencies?
- **Users**: Who benefits? What are their needs?

## Template Selection

| Type       | Use When                                | Template Location                   |
| ---------- | --------------------------------------- | ----------------------------------- |
| `feature`  | New functionality for existing package | `specs/templates/feature.template.md` |
| `package`  | New package or major component         | `specs/templates/package.template.md` |
| `learning` | New educational module                 | `specs/templates/learning.template.md` |
| `change`   | Refactoring or modification            | `specs/templates/change.template.md` |

## Drafting Principles

### Prioritized User Stories
Order stories by importance:
- **P1**: MVP - Core functionality that delivers immediate value.
- **P2**: High - Important features for full functionality.
- **P3**: Nice-to-have - Enhancements.

Each story must be testable as a standalone deliverable.

### Independent Testing
Every user story should include an "Independent Test" description explaining how to verify it in isolation.

### Parallel Markers
Mark tasks that can run in parallel with `[P]`. Identify these early to enable efficient execution.

### NEEDS CLARIFICATION
Use the marker `NEEDS CLARIFICATION: {{issue}}` for any unknowns or ambiguities discovered during drafting.

## Code Interface Validation

Rigorous validation of code samples and API references is required to prevent hallucinations and ensure consistency with the existing codebase.

### Validation Process
1. **Interface Existence**: Confirm all referenced classes, functions, and APIs exist using search tools (e.g., `grep_search`, `list_code_usages`).
2. **Pattern Alignment**: Ensure new interfaces follow existing code patterns, naming conventions, and architectural principles.
3. **Hallucination Detection**: Flag non-existing interfaces with `INTERFACE VALIDATION NEEDED: {{issue}}`.
4. **Library Validation**: Verify all referenced libraries are real, correctly spelled, and used appropriately according to their documentation.

## Quality Standards

### User Story Format
```markdown
### Story 1: [Title] (Priority: P1) 🎯 MVP

As a user, I want to [action] so that [benefit].

**Why this priority**: Core functionality that delivers immediate value.
**Independent Test**: Can be tested by [specific action] and delivers [specific value].

**Acceptance Criteria:**
- [ ] Testable criterion 1
- [ ] Testable criterion 2
```

### Concrete, Measurable Criteria
Avoid vague language. Use specific metrics and behaviors.
- **Vague**: "The API should be fast."
- **Concrete**: "The API must respond within 200ms at p95 under 100 RPS."

### Parallel Task Breakdown
```markdown
## Task Breakdown

- [ ] T001 [P] [US1] Create User model in src/models/user.py
- [ ] T002 [P] [US1] Create Auth model in src/models/auth.py
- [ ] T003 [US1] Implement UserService (depends on T001, T002)
```

## Validation Checklist

Before finalizing, verify the specification against this checklist:
- [ ] Problem statement is clear and compelling
- [ ] Success criteria are measurable and specific
- [ ] All user stories have testable acceptance criteria
- [ ] Stories are prioritized (P1, P2, P3)
- [ ] Each P1 story is independently testable as MVP
- [ ] Technical constraints and dependencies are documented
- [ ] Out of scope items are explicitly listed
- [ ] Implementation phases have clear checkpoints
- [ ] Tasks have parallel markers [P] where applicable
- [ ] No `NEEDS CLARIFICATION` markers remain
- [ ] All code interfaces and samples are validated against the codebase
- [ ] No `INTERFACE VALIDATION NEEDED` markers remain

## Output Standards

- **Location**: `specs/{type}/SPEC-{id}-{title}.md`
- **Naming**: `SPEC-{sequential-id}-{kebab-case-title}.md` (e.g., `SPEC-001-course-search-api.md`)
- [ ] No `NEEDS CLARIFICATION` markers remain
- [ ] All code interfaces and samples are validated against the codebase
- [ ] No `INTERFACE VALIDATION NEEDED` markers remain

## Output Standards

- **Location**: `specs/{type}/SPEC-{id}-{title}.md`
- **Naming**: `SPEC-{sequential-id}-{kebab-case-title}.md` (e.g., `SPEC-001-course-search-api.md`)
