---
agent: 'agent'
description: 'Implement a specification document. Reads a SPEC-*.md file and executes it with phased delivery, validation, and documentation updates.'
tools: ['agent/runSubagent', 'todos']
---

# Implement Specification

Execute a specification document to produce a high-quality implementation.

## Orchestration Strategy

This prompt decomposes implementation into discrete subtasks:

1. **Load & Parse** → Read specification, extract phases
2. **Per-Phase Execution** → Use `agent/runSubagent` for each phase
3. **Progress Tracking** → Use file-based checklist in spec file for deliverables
4. **Validation** → Use `todos` for autonomous TDD cycles
5. **Documentation** → Use `agent/runSubagent` for doc updates

## Input

Provide either:

1. A path to a specification file: `specs/features/SPEC-001-*.md`
2. A specification ID: `SPEC-001`
3. The specification content directly

If no specification is provided, list available specs in `specs/` directory.

## Process

### Step 1: Initialize Deliverables Tracking

Update the specification file with implementation progress (file-based for persistence):

```markdown
## Implementation Progress
- [ ] Phase 1: [deliverables from spec]
- [ ] Phase 2: [deliverables from spec]
- [ ] Phase 3: [deliverables from spec]
- [ ] Documentation updates
- [ ] Final validation
```

This persists across sessions and tracks high-level deliverables.

### Step 2: Load Specification

Read and validate the specification:

- Executive Summary with success criteria exists
- User stories with acceptance criteria exist
- Implementation plan with phases exists
- Testing strategy exists

If sections are missing, ask the user to complete them first.

### Step 3: Confirm Understanding

Summarize:

1. What will be built
2. The phases and their deliverables
3. The validation criteria

Ask for confirmation before proceeding.

### Step 4: Execute Phases

For each phase in the implementation plan, use `agent/runSubagent` to:

1. **Implement deliverables** following TDD workflow.
   
   Use `todos` to track the autonomous TDD cycle:
   - Write failing test for the feature
   - Run test, confirm it fails for the expected reason
   - Write minimal implementation to pass
   - Run test, confirm it passes
   - Refactor while keeping tests green
   - Move to next priority

2. **Validate** using standard gates:
   ```bash
   just check
   just lint {package}
   just test {package}
   ```

3. **Update file-based checklist** after each deliverable:
   ```markdown
   - [x] Phase 1: Core models
   - [ ] Phase 2: Business logic
   ```

4. **Report progress** after each successful phase

### Step 5: Documentation

Use `agent/runSubagent` for documentation subtasks:

- Update package README with usage examples
- Add/update API documentation
- Update CHANGELOG.md
- Update learning materials if specified

### Step 6: Final Validation

Update the specification file with completion status:

```markdown
## Completion Checklist

### Code Quality
- [x] All tests pass
- [x] Type checking passes
- [x] Linting passes

### Specification Compliance
- [x] All acceptance criteria verified
- [x] Success criteria met
- [x] Non-goals were not implemented

### Documentation
- [x] README updated
- [x] Examples executable
- [x] CHANGELOG updated
```

### Step 7: Mark Complete

Update specification status:

```yaml
---
status: implemented
completed: {{YYYY-MM-DD}}
---
```

## Error Handling

**If validation fails after 3 attempts:**

1. Document the blocking issue
2. Mark phase as `blocked` in file-based checklist
3. Report to user with what was attempted and suggested resolution

**If specification is ambiguous:**

1. Do NOT proceed with assumptions
2. Ask specific clarifying questions
3. Update specification before continuing

## Integration

This prompt uses:

- [spec-implementer skill](../skills/spec-implementer/SKILL.md) for implementation patterns
- [python-development skill](../skills/python-development/SKILL.md) for TDD workflow
- [command-runner skill](../skills/command-runner/SKILL.md) for just commands
