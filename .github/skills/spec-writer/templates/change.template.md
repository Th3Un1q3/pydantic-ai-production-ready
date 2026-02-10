# Change Specification Template

<!--
Use this template for refactoring, modifications, or improvements.
Replace all placeholders in {{BRACKETS}}.
Delete helper comments before finalizing.
-->

---
spec-id: SPEC-{{ID}}
title: {{Change Title}}
type: change
status: draft
created: {{YYYY-MM-DD}}
affected-areas: {{comma-separated list of affected packages/modules}}
author: {{author}}
---

## Executive Summary

### Problem Statement

{{Describe the issue or limitation being addressed.}}

### Proposed Change

{{Describe the modification and its impact.}}

### Success Criteria

- {{Criterion 1: e.g., All tests continue to pass}}
- {{Criterion 2: e.g., Performance improves by X%}}
- {{Criterion 3: e.g., Code coverage remains above Y%}}

## Current State

### Existing Behavior

{{Describe how the system currently works.}}

### Issues with Current State

| Issue | Impact | Evidence |
|-------|--------|----------|
| {{Issue 1}} | {{Impact}} | {{Data or examples}} |
| {{Issue 2}} | {{Impact}} | {{Data or examples}} |

### Affected Components

| Component | Location | Impact |
|-----------|----------|--------|
| {{Component 1}} | `{{path/to/file}}` | {{How it's affected}} |
| {{Component 2}} | `{{path/to/file}}` | {{How it's affected}} |

## Proposed State

### New Behavior

{{Describe how the system will work after the change.}}

### Changes Overview

| Change | Before | After |
|--------|--------|-------|
| {{Change 1}} | {{Current}} | {{Proposed}} |
| {{Change 2}} | {{Current}} | {{Proposed}} |

### Code Changes

```python
# Before
{{current_code}}

# After
{{proposed_code}}
```

## Migration Strategy

### Backward Compatibility

- [ ] Change is backward compatible
- [ ] Deprecation warnings added (if applicable)
- [ ] Migration guide provided (if breaking)

### Migration Steps

1. {{Step 1}}
2. {{Step 2}}
3. {{Step 3}}

## Implementation Plan

### Phase 1: Preparation

**Deliverables**:

- [ ] Create failing tests for new behavior
- [ ] Identify all affected call sites
- [ ] Document current behavior

**Validation**:

- New tests fail (expected)
- Existing tests pass

### Phase 2: Implementation

**Deliverables**:

- [ ] Implement changes
- [ ] Update affected call sites
- [ ] Add deprecation warnings (if applicable)

**Validation**:

- All tests pass
- `just check` passes
- `just lint` passes

### Phase 3: Cleanup & Documentation

**Deliverables**:

- [ ] Update documentation
- [ ] Update CHANGELOG.md
- [ ] Remove deprecated code (if applicable)

**Validation**:

- Documentation is accurate
- No dead code remains

## Testing Strategy

### Regression Tests

- [ ] All existing tests continue to pass
- [ ] No behavior changes for unaffected code paths

### New Tests

| Test | Purpose |
|------|---------|
| {{Test 1}} | {{Validates new behavior}} |
| {{Test 2}} | {{Validates edge case}} |

### Performance Tests (if applicable)

| Metric | Before | Target |
|--------|--------|--------|
| {{Metric 1}} | {{current}} | {{target}} |

## Risk Assessment

### Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {{Risk 1}} | {{High/Med/Low}} | {{High/Med/Low}} | {{Strategy}} |
| {{Risk 2}} | {{High/Med/Low}} | {{High/Med/Low}} | {{Strategy}} |

### Rollback Plan

If the change causes issues:

1. {{Rollback step 1}}
2. {{Rollback step 2}}

## Constraints

### Technical Constraints

- {{Constraint 1}}
- {{Constraint 2}}

### Non-Goals

- {{Non-goal 1: What this change explicitly does NOT do}}
- {{Non-goal 2}}

## Review Checklist

Before implementation:

- [ ] All affected areas identified
- [ ] Migration path documented
- [ ] Rollback plan defined

After implementation:

- [ ] All tests pass
- [ ] No regressions in coverage
- [ ] Documentation updated
- [ ] CHANGELOG updated

## References

- {{Link to related issue}}
- {{Link to design discussion}}
- {{Link to affected code}}
