---
name: spec-implementer
description: Execute specifications to produce high-quality implementations. Use when asked to "implement a spec", "execute specification", "build from spec", or when a SPEC-*.md file is provided. Follows phased implementation with validation, updates documentation, and ensures quality through iterative refinement.
---

# Specification Implementer

Execute specifications with phased delivery, continuous validation, and documentation updates.

## Overview

This skill transforms specifications into working implementations through:

1. Specification analysis and planning
2. Phased implementation with validation gates
3. Documentation updates
4. Quality assurance through iterative refinement

## Workflow

### Phase 1: Specification Analysis

**Load and validate the specification:**

1. Read the specification file (e.g., `specs/features/SPEC-001-*.md`)
2. Verify required sections are present:
   - [ ] Executive Summary with success criteria
   - [ ] User stories with acceptance criteria
   - [ ] Implementation plan with phases
   - [ ] Testing strategy
3. Identify dependencies and constraints
4. Confirm understanding with the user if ambiguities exist

**Output**: Implementation plan with clear phases.

### Phase 2: Phased Implementation

Execute each phase defined in the specification:

```markdown
## Implementation Loop

FOR each phase in specification.implementation_plan:
    1. Review phase deliverables
    2. Implement deliverables following TDD workflow
    3. Run validation checks
    4. IF validation fails:
        - Analyze failure
        - Refine implementation
        - Re-validate (max 3 attempts)
    5. Report phase completion
    6. Commit progress
```

**TDD Integration**: For Python code, follow the [python-development](../python-development/SKILL.md) skill's ZOMBIE TDD methodology.

**Validation Between Phases**:

```bash
# Standard validation gate
just check              # Type checking
just lint {package}     # Linting
just test {package}     # Tests
```

### Phase 3: Documentation Updates

After implementation, update relevant documentation:

1. **Package README**: Usage examples, API documentation
2. **CHANGELOG**: New features, breaking changes
3. **Learning materials**: If specified, update `learning/` modules
4. **Specification status**: Mark as `implemented`

### Phase 4: Quality Assurance

Final validation checklist:

```markdown
## QA Checklist

### Code Quality
- [ ] All tests pass (`just test`)
- [ ] Type checking passes (`just check`)
- [ ] Linting passes (`just lint`)
- [ ] Code coverage meets target

### Specification Compliance
- [ ] All acceptance criteria verified
- [ ] Success criteria measurable and met
- [ ] Non-goals were not implemented

### Documentation
- [ ] README updated
- [ ] API docs accurate
- [ ] Examples executable
```

## Execution Patterns

### Pattern 1: Evaluator-Optimizer Loop

For quality-critical implementations, use iterative refinement:

```python
# Pseudocode for implementation refinement
def implement_with_refinement(deliverable: str, criteria: list[str]) -> str:
    implementation = generate_implementation(deliverable)
    
    for iteration in range(3):  # Max iterations
        evaluation = evaluate_against_criteria(implementation, criteria)
        
        if evaluation.all_pass:
            return implementation
        
        # Refine based on feedback
        implementation = refine(implementation, evaluation.failures)
    
    # Report partial success with remaining issues
    return implementation
```

### Pattern 2: Test-Driven Phases

For each deliverable:

1. **Red**: Write failing test from acceptance criteria
2. **Green**: Implement minimal code to pass
3. **Refactor**: Clean up while maintaining green

### Pattern 3: Incremental Commits

Commit after each successful validation:

```markdown
## Commit Pattern

After each phase:
1. Verify all validation checks pass
2. Commit changes with:
   - Descriptive commit message
   - Updated checklist in PR description
```

## Integration with Other Skills

| Skill | Integration Point |
|-------|-------------------|
| [python-development](../python-development/SKILL.md) | TDD workflow for Python code |
| [learning-ops](../learning-ops/SKILL.md) | Learning module creation |
| [monorepo-maintainer](../monorepo-maintainer/SKILL.md) | Package structure guidance |
| [command-runner](../command-runner/SKILL.md) | Running just commands |

## Error Handling

### Validation Failures

If validation fails after 3 attempts:

1. Document the blocking issue
2. Mark phase as `blocked`
3. Report to user with:
   - What was attempted
   - Why it failed
   - Suggested resolution

### Ambiguous Specifications

If the specification is unclear:

1. Do NOT proceed with assumptions
2. Ask specific clarifying questions
3. Update specification if needed before continuing

## Status Tracking

Update specification frontmatter as work progresses:

```yaml
---
status: in-progress  # draft → in-progress → review → implemented
current-phase: 2
last-updated: {{YYYY-MM-DD}}
---
```

## Completion Criteria

Implementation is complete when:

- [ ] All phases executed successfully
- [ ] All acceptance criteria verified
- [ ] All success criteria measurable and met
- [ ] Documentation updated
- [ ] Code review completed (if applicable)
- [ ] Specification status updated to `implemented`

## Quick Reference

```markdown
## Implementation Checklist

### Preparation
- [ ] Read and understand specification
- [ ] Verify all required sections present
- [ ] Identify dependencies

### Execution
- [ ] Phase 1: Foundation (tests + core)
- [ ] Phase 2: Implementation (features)
- [ ] Phase 3: Documentation (docs + polish)

### Validation
- [ ] All tests pass
- [ ] Type checking passes
- [ ] Linting passes
- [ ] Acceptance criteria verified

### Completion
- [ ] Documentation updated
- [ ] Specification marked as implemented
- [ ] Final commit with summary
```
