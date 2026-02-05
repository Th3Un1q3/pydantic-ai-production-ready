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

### Story 1: {{Story Title}}

As a {{user type}}, I want to {{action}} so that {{benefit}}.

**Acceptance Criteria:**

- [ ] {{Testable criterion 1}}
- [ ] {{Testable criterion 2}}
- [ ] {{Testable criterion 3}}

### Story 2: {{Story Title}}

As a {{user type}}, I want to {{action}} so that {{benefit}}.

**Acceptance Criteria:**

- [ ] {{Testable criterion 1}}
- [ ] {{Testable criterion 2}}

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

### Phase 1: Foundation

**Deliverables:**

- [ ] {{Deliverable 1}}
- [ ] {{Deliverable 2}}

**Validation:**

- [ ] Unit tests pass
- [ ] Type checking passes

### Phase 2: Core Implementation

**Deliverables:**

- [ ] {{Deliverable 1}}
- [ ] {{Deliverable 2}}

**Validation:**

- [ ] Integration tests pass
- [ ] Acceptance criteria verified

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

- {{Test category 1}}
- {{Test category 2}}

### Integration Tests

- {{Integration test 1}}
- {{Integration test 2}}

### Edge Cases

- {{Edge case 1}}
- {{Edge case 2}}

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| {{Risk 1}} | {{High/Medium/Low}} | {{How to mitigate}} |
| {{Risk 2}} | {{High/Medium/Low}} | {{How to mitigate}} |

## References

- {{Link to related documentation}}
- {{Link to design decisions}}
- {{Link to prior art}}
