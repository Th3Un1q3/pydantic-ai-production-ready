---
agent: 'agent'
description: 'Implement a specification document. Reads a SPEC-*.md file and executes it with phased delivery, validation, and documentation updates.'
tools: ['agent/runSubagent', 'todos', 'context7/*', 'gh_readonly/*', 'web']
---

# Implement Specification

Execute a specification document using the [spec-implementer skill](../skills/spec-implementer/SKILL.md).

## Orchestration Strategy

This prompt decomposes implementation into discrete subtasks:

1. **Load & Validate** → Check for `NEEDS CLARIFICATION` markers
2. **Foundational Phase** → Complete blocking prerequisites first
3. **Per-Story Execution** → Use `agent/runSubagent` for each user story (P1 first)
4. **Parallel Tasks** → Execute [P] marked tasks simultaneously
5. **Progress Tracking** → File-based checklist for deliverables (human-in-loop persistence)
6. **TDD Cycles** → Use `todos` for autonomous TDD within stories
7. **Checkpoints** → Validate each story independently before next
8. **Documentation** → Use `agent/runSubagent` for doc updates

## Agentic Tools Usage

### File-Based Deliverables Tracking

Update the specification file with implementation progress (persistent across sessions):

```markdown
## Implementation Progress
- [ ] Phase 0: Foundational (blocking prerequisites)
- [ ] CHECKPOINT: Foundation ready
- [ ] Phase 1: User Story 1 (P1) 🎯 MVP
- [ ] CHECKPOINT: Story 1 independently testable
- [ ] Phase 2: User Story 2 (P2)
- [ ] CHECKPOINT: Story 2 independently testable
- [ ] Documentation updates
- [ ] Final validation
```

### Parallel Task Execution

Execute [P] marked tasks simultaneously:

```markdown
## Parallel Execution
Tasks marked [P] within same story run together:
- [ ] T001 [P] [US1] Create User model → Execute
- [ ] T002 [P] [US1] Create Auth model → Execute (parallel)

Then sequential:
- [ ] T003 [US1] Implement UserService → Execute (after T001, T002)
```

### `todos` for TDD Cycles

Use `todos` to track autonomous TDD cycle within a story:

```markdown
Use `todos` to track:
1. Write failing test for the feature
2. Run test, confirm it fails for the expected reason
3. Write minimal implementation to pass
4. Run test, confirm it passes
5. Refactor while keeping tests green
6. Move to next priority
```

### Subtask Delegation

Use `agent/runSubagent` for parallel/specialized work:

| Subtask | Agent Purpose |
|---------|---------------|
| Phase implementation | Execute deliverables with TDD |
| Documentation updates | Update README, CHANGELOG, API docs |
| Quality validation | Run validation gates |

## Input

Provide either:

1. A path to a specification file: `specs/features/SPEC-001-*.md`
2. A specification ID: `SPEC-001`
3. The specification content directly

If no specification is provided, list available specs in `specs/` directory.

## Workflow

Follow the workflow defined in [spec-implementer skill](../skills/spec-implementer/SKILL.md):

1. **Load Specification** - Read and check for `NEEDS CLARIFICATION` markers
2. **Confirm Understanding** - Summarize and confirm with user
3. **Foundational Phase** - Complete Phase 0 blocking prerequisites
4. **CHECKPOINT** - Foundation ready, stories can begin
5. **Execute Stories** - Implement P1 first (MVP), then P2, P3
6. **Per-Story Checkpoints** - Validate story independently before next
7. **Update Documentation** - README, CHANGELOG, API docs
8. **Final Validation** - Complete QA checklist
9. **Mark Complete** - Update specification status to `implemented`

## Key Concepts from spec-kit

- **MVP First**: Complete P1 story, validate, then continue
- **Parallel Execution**: Run [P] tasks simultaneously
- **Checkpoints**: Verify each story independently
- **Foundational Phase**: Complete blocking prerequisites before ANY story

## Integration

This prompt uses:

- [spec-implementer skill](../skills/spec-implementer/SKILL.md) for implementation patterns
- [python-development skill](../skills/python-development/SKILL.md) for TDD workflow
- [command-runner skill](../skills/command-runner/SKILL.md) for just commands
