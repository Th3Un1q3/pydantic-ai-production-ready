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
   - [ ] User stories with acceptance criteria (prioritized P1, P2, P3)
   - [ ] Implementation plan with phases and checkpoints
   - [ ] Task breakdown with parallel markers [P]
   - [ ] Testing strategy
3. Check for `NEEDS CLARIFICATION` markers - resolve before proceeding
4. Identify dependencies and constraints
5. Confirm understanding with the user if ambiguities exist

**Output**: Validated specification ready for implementation.

### Phase 2: Foundational Implementation

**⚠️ CRITICAL**: Complete foundational/blocking prerequisites before ANY user story.

```markdown
## Foundational Phase

1. Execute Phase 0 tasks (core infrastructure)
2. Run validation checks
3. Confirm foundation ready
4. **CHECKPOINT**: Foundation complete - story work can begin
```

### Phase 3: User Story Implementation (Priority Order)

Execute user stories in priority order (P1 → P2 → P3):

```markdown
## Story Implementation Loop

FOR each user_story in priority_order (P1 first):
    1. Identify [P] parallel tasks - execute together
    2. Execute sequential tasks in dependency order
    3. Implement following TDD workflow
    4. Run story validation checks
    5. **CHECKPOINT**: Story independently testable
    6. Commit progress with story status
```

**Parallel Execution**:

```markdown
## Parallel Task Execution

Tasks marked [P] can run simultaneously:
- [ ] T001 [P] [US1] Create User model
- [ ] T002 [P] [US1] Create Auth model
→ Execute T001 and T002 in parallel

Then execute dependent tasks:
- [ ] T003 [US1] Implement UserService (depends on T001, T002)
```

**TDD Integration**: For Python code, follow the [python-development](../python-development/SKILL.md) skill's ZOMBIE TDD methodology.

**Validation Between Stories**:

```bash
just check
just lint {package}
just test {package}
```

### Phase 4: Documentation Updates

After implementation, update relevant documentation:

1. **Package README**: Usage examples, API documentation
2. **CHANGELOG**: New features, breaking changes
3. **Learning materials**: If specified, update `learning/` modules
4. **Specification status**: Mark as `implemented`

### Phase 5: Quality Assurance

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

### Pattern 1: MVP First (P1 Only)

Deliver value incrementally:

```markdown
## MVP Strategy

1. Complete Phase 0: Foundational
2. Complete P1 User Story only
3. **STOP and VALIDATE**: Test P1 independently
4. Deploy/demo if ready (this is your MVP!)
5. Continue with P2, P3 as capacity allows
```

### Pattern 2: Parallel Task Execution

Execute [P] marked tasks simultaneously:

```markdown
## Parallel Execution

# All [P] tasks within same story can run together:
T001 [P] [US1] → Execute
T002 [P] [US1] → Execute (in parallel with T001)

# Wait for parallel tasks, then sequential:
T003 [US1] → Execute (after T001, T002 complete)
```

### Pattern 3: Evaluator-Optimizer Loop

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

### Pattern 4: Test-Driven Phases

For each deliverable:

1. **Red**: Write failing test from acceptance criteria
2. **Green**: Implement minimal code to pass
3. **Refactor**: Clean up while maintaining green

### Pattern 5: Incremental Commits with Checkpoints

Commit after each successful validation:

```markdown
## Commit Pattern

After each story checkpoint:
1. Verify all validation checks pass
2. Commit changes with descriptive message
3. Update specification status
4. **CHECKPOINT**: Story X complete and independently testable
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
3. Report with:
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
status: in-progress  # draft → ready → in-progress → review → implemented → deprecated
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
