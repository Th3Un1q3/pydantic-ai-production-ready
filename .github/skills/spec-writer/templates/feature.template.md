# Feature Specification Template

<!--
Use this template for new functionality in existing packages.
Replace all placeholders in {{BRACKETS}}.
Delete helper comments before finalizing.
-->

---
spec-id: SPEC-{{ID}}
title: {{Feature Title}}
type: feature
status: draft
created: {{YYYY-MM-DD}}
package: {{target-package-name}}
author: {{author}}
---

## Executive Summary

### Problem Statement

<!-- 1-2 sentences describing the pain point. Be specific. -->

{{Describe the problem users face without this feature.}}

### Proposed Solution

<!-- 1-2 sentences describing the fix. -->

{{Describe how this feature solves the problem.}}

### Success Criteria

<!-- 3-5 measurable KPIs. Include specific numbers. -->

- {{KPI 1 with target metric}}
- {{KPI 2 with target metric}}
- {{KPI 3 with target metric}}

## User Stories

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance (P1, P2, P3).
  Each story must be INDEPENDENTLY TESTABLE - if you implement just ONE of them,
  you should still have a viable MVP that delivers value.
-->

### Story 1: {{Story Title}} (Priority: P1) 🎯 MVP

As a {{user type}}, I want to {{action}} so that {{benefit}}.

**Why this priority**: {{Explain the value and why it's most critical}}

**Independent Test**: {{How this story can be tested on its own as an MVP}}

**Acceptance Criteria:**

- [ ] {{Testable criterion 1}}
- [ ] {{Testable criterion 2}}
- [ ] {{Testable criterion 3}}

---

### Story 2: {{Story Title}} (Priority: P2)

As a {{user type}}, I want to {{action}} so that {{benefit}}.

**Why this priority**: {{Explain the value and why it has this priority}}

**Independent Test**: {{How this story can be tested independently}}

**Acceptance Criteria:**

- [ ] {{Testable criterion 1}}
- [ ] {{Testable criterion 2}}

### Edge Cases

<!-- What happens when boundary conditions occur? -->

- {{Edge case 1: boundary condition or error scenario}}
- {{Edge case 2: boundary condition or error scenario}}

## Requirements

### Functional Requirements

<!-- Use NEEDS CLARIFICATION for unclear items -->

- **FR-001**: System MUST {{specific capability}}
- **FR-002**: System MUST {{specific capability}}
- **FR-003**: Users MUST be able to {{key interaction}}
- **FR-004**: {{requirement or NEEDS CLARIFICATION: describe what's unclear}}

## Technical Specification

### API Design

<!-- Define interfaces, endpoints, or function signatures. -->

```python
# Example interface
class {{FeatureName}}:
    async def {{method}}(self, {{params}}) -> {{ReturnType}}:
        """{{Description}}."""
        ...
```

### Data Models

<!-- Define any new data structures. -->

```python
from pydantic import BaseModel

class {{ModelName}}(BaseModel):
    """{{Description}}."""
    {{field}}: {{type}}
```

### Dependencies

<!-- List required packages or services. -->

| Dependency | Version | Purpose |
|------------|---------|---------|
| {{package}} | {{version}} | {{why needed}} |

### Integration Points

<!-- How does this feature connect to existing systems? -->

- **Input**: {{What data/events trigger this feature?}}
- **Output**: {{What does this feature produce?}}
- **Side effects**: {{Any external state changes?}}

## Constraints

### Technical Constraints

- {{Constraint 1: e.g., Must use existing database schema}}
- {{Constraint 2: e.g., Response time < 200ms}}

### Non-Goals

<!-- Explicitly state what this feature does NOT do. -->

- {{Non-goal 1}}
- {{Non-goal 2}}

## Implementation Plan

### Phase 0: Foundational (Blocking Prerequisites)

<!--
  ⚠️ CRITICAL: Core infrastructure that MUST be complete before ANY user story.
  No story work can begin until this phase is complete.
-->

**Deliverables:**

- [ ] {{Core dependency or infrastructure}}
- [ ] {{Database/API foundation if applicable}}

**Validation:**

- [ ] Foundation ready for story implementation
- [ ] Type checking passes

**Checkpoint**: Foundation complete - story implementation can begin

---

### Phase 1: User Story 1 (P1) 🎯 MVP

**Goal**: {{Brief description of what this story delivers}}

**Deliverables:**

- [ ] [P] {{Deliverable 1 - can run in parallel}}
- [ ] [P] {{Deliverable 2 - can run in parallel}}
- [ ] {{Deliverable 3 - depends on above}}

**Validation:**

- [ ] Unit tests pass
- [ ] Acceptance criteria verified
- [ ] Story independently testable

**Checkpoint**: Story 1 functional - can demo/deploy as MVP

---

### Phase 2: User Story 2 (P2)

**Goal**: {{Brief description of what this story delivers}}

**Deliverables:**

- [ ] {{Deliverable 1}}
- [ ] {{Deliverable 2}}

**Validation:**

- [ ] Integration tests pass
- [ ] Acceptance criteria verified

**Checkpoint**: Stories 1 AND 2 both work independently

---

### Phase 3: Documentation & Polish

**Deliverables:**

- [ ] API documentation updated
- [ ] Usage examples added
- [ ] CHANGELOG updated

**Validation:**

- [ ] Documentation builds without errors
- [ ] Examples are executable

## Testing Strategy

### Unit Tests

- [ ] {{Test category 1}}
- [ ] {{Test category 2}}

### Integration Tests

- [ ] {{Integration test 1}}
- [ ] {{Integration test 2}}

### Edge Cases

- [ ] {{Edge case test 1}}
- [ ] {{Edge case test 2}}

## Task Breakdown

<!--
  [P] = Can run in parallel (different files, no dependencies)
  [US1/US2] = Which user story this belongs to
  Tasks are organized by user story for independent implementation
-->

### Parallel Markers

| Marker | Meaning |
|--------|---------|
| `[P]` | Can run in parallel with other [P] tasks |
| `[US1]` | Belongs to User Story 1 |
| `[US2]` | Belongs to User Story 2 |

### Task List

- [ ] T001 [P] [US1] {{Task description with file path}}
- [ ] T002 [P] [US1] {{Task description with file path}}
- [ ] T003 [US1] {{Task that depends on T001, T002}}
- [ ] T004 [P] [US2] {{Task description with file path}}
- [ ] T005 [US2] {{Task description with file path}}

## Complexity Tracking

<!-- Fill ONLY if constitution/principles violations must be justified -->

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| {{e.g., Extra abstraction}} | {{Specific need}} | {{Why simpler approach insufficient}} |

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| {{Risk 1}} | {{High/Medium/Low}} | {{How to mitigate}} |
| {{Risk 2}} | {{High/Medium/Low}} | {{How to mitigate}} |

## References

- {{Link to related documentation}}
- {{Link to design decisions}}
- {{Link to prior art}}
