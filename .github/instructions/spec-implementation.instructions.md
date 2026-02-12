---
description: Guidance for executing specifications using phased delivery, checkpoints, and TDD.
applyTo: '**/specs/**/*.md'
---

# Specification Implementation

Transform specifications into working code through phased delivery, continuous validation, and documentation updates.

## Implementation Workflow

### Phase 1: Foundational Implementation
**⚠️ CRITICAL**: Complete all core infrastructure and Phase 0 tasks before any user story work. Foundations provide the necessary scaffolding for features.
1. Execute foundational tasks (prerequisites).
2. Run validation checks (`just check`).
3. **CHECKPOINT**: Confirm foundation is ready before proceeding to P1.

### Phase 2: User Story Implementation (Priority Order)
Execute stories in priority order: **P1 (MVP) → P2 → P3**.

**The Story Loop:**
FOR each user_story in priority_order (P1 first):
1. Identify all `[P]` tasks within the story level.
2. **Parallel Execution Gate**: Group and execute all `[P]` tasks using `agent/runSubagent` or simultaneous tool calls where possible. Follow [.github/instructions/tasks-decomposition.instructions.md](.github/instructions/tasks-decomposition.instructions.md).
3. Execute remaining sequential tasks in dependency order.
4. Follow the [.github/instructions/test-implementation.instructions.md](.github/instructions/test-implementation.instructions.md) workflow (Red-Green-Refactor) for each task.
5. Run story validation checks (tests and linting).
6. **CHECKPOINT**: Ensure the story is independently testable. Mark tasks as `[x]` in the specification file.
7. Commit progress with story status and checkpoint confirmation.

### Phase 3: Documentation Updates
After implementation, update relevant files:
- **README.md**: Add usage examples and API docs.
- **CHANGELOG.md**: Document features and any breaking changes.
- **Learning Materials**: Update files in `learning/` if specified (see [.github/instructions/learning-operations.instructions.md](.github/instructions/learning-operations.instructions.md)).
- **Specification Status**: Mark as `implemented`.

### Phase 4: Final QA Checklist
- [ ] All tests pass (`just test`).
- [ ] Type checking and linting pass (`just check`).
- [ ] All acceptance criteria in the specification are verified.
- [ ] Documentation is accurate and examples are executable.
- [ ] Specification status updated to `implemented`.

## Execution Patterns

### Phased Delivery (MVP Strategy)
Deliver value incrementally by focusing on core functionality first.
1. Complete Phase 0: Foundations.
2. Complete P1 User Story only.
3. **STOP and VALIDATE**: Test P1 independently as an MVP.
4. Continue with P2, P3 as capacity allows.

### Parallel Task Execution
Tasks marked `[P]` within the same story context should be grouped and executed together to improve efficiency.
- **Grouping**: Execute all [P] tasks in a single phase.
- **Waiting**: Ensure all parallel tasks complete before starting dependent sequential tasks.

### Test-Driven Phases
For each deliverable/story:
1. **Red**: Write failing test from acceptance criteria.
2. **Green**: Implement minimal code to pass.
3. **Refactor**: Clean up while maintaining green.

### Incremental Commits with Checkpoints
Commit after each successful validation of a story:
1. Verify all validation checks pass.
2. Commit with a descriptive message (e.g., `feat: implement US1 - core search functionality`).
3. **CHECKPOINT**: Update spec status or post checkpoint message.

## Handling Failures
If validation fails repeatedly:
1. Document the blocking issue.
2. Mark the phase as `blocked`.
3. Report the attempted steps and suggested resolution to the user.
