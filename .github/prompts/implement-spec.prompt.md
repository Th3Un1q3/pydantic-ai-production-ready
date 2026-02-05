---
mode: 'agent'
description: 'Implement a specification document. Reads a SPEC-*.md file and executes it with phased delivery, validation, and documentation updates.'
---

# Implement Specification

Execute a specification document to produce a high-quality implementation.

## Input

Provide either:

1. A path to a specification file: `specs/features/SPEC-001-*.md`
2. A specification ID: `SPEC-001`
3. The specification content directly

If no specification is provided, list available specs in `specs/` directory.

## Process

### Step 1: Load Specification

Read and validate the specification:

- [ ] Executive Summary with success criteria exists
- [ ] User stories with acceptance criteria exist
- [ ] Implementation plan with phases exists
- [ ] Testing strategy exists

If sections are missing, ask the user to complete them first.

### Step 2: Confirm Understanding

Summarize:

1. What will be built
2. The phases and their deliverables
3. The validation criteria

Ask for confirmation before proceeding.

### Step 3: Execute Phases

For each phase in the implementation plan:

1. **Review deliverables** for this phase
2. **Implement** following TDD workflow (see python-development skill)
3. **Validate** using standard gates:
   ```bash
   just check              # Type checking
   just lint {package}     # Linting
   just test {package}     # Tests
   ```
4. **Report progress** after each successful phase

### Step 4: Documentation

After implementation:

- [ ] Update package README with usage examples
- [ ] Add/update API documentation
- [ ] Update CHANGELOG.md
- [ ] Update learning materials if specified

### Step 5: Final Validation

Run complete validation:

```markdown
## Completion Checklist

### Code Quality
- [ ] All tests pass
- [ ] Type checking passes
- [ ] Linting passes

### Specification Compliance
- [ ] All acceptance criteria verified
- [ ] Success criteria met
- [ ] Non-goals were not implemented

### Documentation
- [ ] README updated
- [ ] Examples executable
- [ ] CHANGELOG updated
```

### Step 6: Mark Complete

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
2. Mark phase as `blocked`
3. Report to user with what was attempted and suggested resolution

**If specification is ambiguous:**

1. Do NOT proceed with assumptions
2. Ask specific clarifying questions
3. Update specification before continuing

## Integration

This prompt uses:

- [spec-implementer skill](../.github/skills/spec-implementer/SKILL.md) for implementation patterns
- [python-development skill](../.github/skills/python-development/SKILL.md) for TDD workflow
- [command-runner skill](../.github/skills/command-runner/SKILL.md) for just commands
