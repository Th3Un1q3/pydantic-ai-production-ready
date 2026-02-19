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

### Persona-based assumption validation (Role-Player subagent) 🧩

Use persona-driven validation to surface missed risks, clarify trade-offs, and confirm assumptions from multiple stakeholder perspectives. Run this as part of discovery for every P1 user story and any high‑risk P2 items.

1. Identify the core assumptions in the draft spec (data, latency, cost, security, integrations, user behavior).
2. Select relevant personas from `learning/00-misc/learner-personas/` (e.g., `ai-engineer.persona.md`, `enterprise-architect.persona.md`, `product-manager.persona.md`).
3. For each selected persona, run the **Role-Player** subagent with the following structured input:
   - Context: short spec excerpt (assumption, acceptance criteria, sample input/output, and any relevant code/design links).
   - Tasks: (a) Validate the assumption, (b) Provide `Stance` (Approve/Reject/Conditional), (c) List `Critical Risks`, (d) Give `Recommendations` and mitigations, (e) Return a 1–2 line `Reflection` on trade-offs and confidence level.
4. Save the agent output as a `Role-Based Feedback Report` and attach it to the spec (append under the relevant user story).
5. If persona feedback disagrees, add `NEEDS CLARIFICATION: {{issue}}` to the spec and prioritize follow-up user stories or mitigation work.
6. After incorporating changes, re-run the same persona(s) and ask them to **validate the result** and **reflect** on whether their stance changed.

Example subagent prompt (copy into the Role-Player agent or use `runSubagent`):

```text
Context: (paste assumption + acceptance criteria + 2–3 supporting artifacts)
Persona: ai-engineer.persona.md
Task: Validate the assumption and produce a Role-Based Feedback Report with fields: Stance, Critical Risks, Recommendations, Confidence (0–100%), Follow-up Questions, Reflection (2–3 sentences).
```

Expected deliverables:
- One `Role-Based Feedback Report` per persona per validated assumption.
- Spec updated with `NEEDS CLARIFICATION` markers or acceptance-criteria changes where required.
- A short reconciliation summary when personas conflict.

Independent test (how to verify):
- Run Role-Player for at least two distinct personas for each P1 story.
- Confirm each P1 story is either `Approved` or marked `Conditional` with concrete mitigation steps; unresolved `Reject` results must produce follow-up tasks.

Tips:
- Parallelize persona checks (use `just agent-parallel` or multiple `runSubagent` calls) to reduce latency.
- Keep persona reports attached to the spec for auditability and traceability.
- Treat persona `Reflection` as input to the risk/acceptance conversation — not as final approval.


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

For **`learning` type specifications**, simplicity and gradual progression are Paramount:
- **Step-by-Step Path**: Define a short, logical path from a clear start point to an end point (e.g., Concept -> Implementation -> Analysis).
- **Avoid Over-Engineering**: Do not include full production-grade complexity (e.g., CI/CD gating, large-scale automation, or multi-role incident workflows) in introductory learning modules unless explicitly requested.
- **Practical Deliverables**: Focus on on-demand/local workflows (like producing a scorecard or a single auditable trace) that provide immediate learning value without heavy infrastructure.

Each story must be testable as a standalone deliverable.

### Independent Testing
Every user story should include an "Independent Test" description explaining how to verify it in isolation.

### Designing for Parallelism
When drafting stories and tasks, identify components that can be built independently.
- **Markers**: Use `[P]` for tasks that have no dependencies within the same phase.
- **Isolation**: Group parallel tasks such that they don't modify the same lines of code simultaneously.
- **Efficiency**: Aim for at least 30% of implementation tasks to be marked as `[P]` for complex features.

### NEEDS CLARIFICATION
Use the marker `NEEDS CLARIFICATION: {{issue}}` for any unknowns or ambiguities discovered during drafting.

## Code Interface Validation

Rigorous validation of code samples and API references is required to prevent hallucinations and ensure consistency with the existing codebase.

### Validation Process
1. **Interface Existence**: Confirm all referenced classes, functions, and APIs exist using search tools(both internal such as code search and external such as official documentation).
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
Break down implementation into granular tasks. Mark parallelizable tasks with `[P]`.
```markdown
## Task Breakdown

- [ ] T001 [P] [US1] Create User model in `src/models/user.py`
- [ ] T002 [P] [US1] Create Auth model in `src/models/auth.py`
- [ ] T003 [US1] Implement UserService in `src/services.py` (depends on T001, T002)
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
