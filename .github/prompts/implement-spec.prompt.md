---
agent: 'agent'
description: 'Implement a specification document. Reads a SPEC-*.md file and executes it with phased delivery, validation, and documentation updates.'
tools: ['agent/runSubagent', 'todos']
---

# Implement Specification

Execute a specification document using the [spec-implementer skill](../skills/spec-implementer/SKILL.md).

## Orchestration Strategy

This prompt decomposes implementation into discrete subtasks:

1. **Load & Parse** → Read specification, extract phases
2. **Per-Phase Execution** → Use `agent/runSubagent` for each phase
3. **Progress Tracking** → File-based checklist for deliverables (human-in-loop persistence)
4. **TDD Cycles** → Use `todos` for autonomous TDD within phases
5. **Documentation** → Use `agent/runSubagent` for doc updates

## Agentic Tools Usage

### File-Based Deliverables Tracking

Update the specification file with implementation progress (persistent across sessions):

```markdown
## Implementation Progress
- [ ] Phase 1: [deliverables from spec]
- [ ] Phase 2: [deliverables from spec]
- [ ] Phase 3: [deliverables from spec]
- [ ] Documentation updates
- [ ] Final validation
```

### `todos` for TDD Cycles

Use `todos` to track autonomous TDD cycle within a phase:

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

1. **Load Specification** - Read and validate structure
2. **Confirm Understanding** - Summarize and confirm with user
3. **Execute Phases** - Implement each phase with validation gates
4. **Update Documentation** - README, CHANGELOG, API docs
5. **Final Validation** - Complete QA checklist
6. **Mark Complete** - Update specification status

## Integration

This prompt uses:

- [spec-implementer skill](../skills/spec-implementer/SKILL.md) for implementation patterns
- [python-development skill](../skills/python-development/SKILL.md) for TDD workflow
- [command-runner skill](../skills/command-runner/SKILL.md) for just commands
