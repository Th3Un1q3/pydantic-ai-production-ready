# Specifications Directory

This directory contains specifications for features, packages, learning modules, and changes.

## Purpose

Specifications are the **single source of truth** for what to build and how to validate it. They bridge the gap between vision and implementation by providing:

- Clear problem statements and success criteria
- User stories **prioritized by importance** (P1 = MVP, P2, P3)
- Phased implementation with **checkpoints** after each story
- **Parallel task markers** [P] for concurrent execution
- Technical constraints and non-goals

## Directory Structure

```markdown
specs/
├── README.md           # This file
├── features/           # New functionality for existing packages
│   └── SPEC-{id}-{title}.md
├── packages/           # New packages or major components
│   └── SPEC-{id}-{title}.md
├── learning/           # Educational content and modules
│   └── SPEC-{id}-{title}.md
└── changes/            # Refactoring and modifications
    └── SPEC-{id}-{title}.md
```

## Workflow

### 1. Create a Specification

Use the `/write-spec` prompt or follow the [.github/instructions/spec-writing.instructions.md](.github/instructions/spec-writing.instructions.md) instruction module:

```bash
/write-spec
```

The workflow guides you through:

1. **Discovery**: Clarifying questions to understand the scope
2. **Drafting**: Generating a structured specification with prioritized stories
3. **Clarification**: Mark unclear items with `NEEDS CLARIFICATION:`
4. **Validation**: Ensuring quality standards are met

### 2. Review and Refine

Before implementation, ensure:

- [ ] Problem statement is clear
- [ ] Success criteria are measurable
- [ ] User stories are prioritized (P1, P2, P3)
- [ ] Each story is independently testable as MVP
- [ ] Tasks have parallel markers [P] where applicable
- [ ] No `NEEDS CLARIFICATION` markers remain
- [ ] Implementation phases have checkpoints

### 3. Implement the Specification

Use the `/implement-spec` prompt or follow the [.github/instructions/spec-navigating.instructions.md](.github/instructions/spec-navigating.instructions.md) and [.github/instructions/spec-implementation.instructions.md](.github/instructions/spec-implementation.instructions.md) instruction modules:

```bash
/implement-spec specs/features/SPEC-001-course-search.md
```

The workflow:

1. Validates specification (checks for `NEEDS CLARIFICATION`)
2. Completes **foundational phase** first (blocking prerequisites)
3. Executes **P1 story** → **CHECKPOINT** → validates as MVP
4. Continues with P2, P3 in priority order
5. Runs [P] tasks in parallel within each story
6. Updates documentation
7. Marks specification as `implemented`

## Naming Convention

```text
SPEC-{id}-{kebab-case-title}.md
```

- **id**: Sequential 3-digit number (001, 002, ...)
- **title**: Descriptive kebab-case name

Examples:

- `SPEC-001-course-search-api.md`
- `SPEC-002-authentication-flow.md`
- `SPEC-003-advanced-patterns-module.md`

## Specification Status

Each specification has a status in its frontmatter:

| Status        | Description                                    |
| ------------- | ---------------------------------------------- |
| `draft`       | Work in progress, not ready for implementation |
| `ready`       | Reviewed and approved for implementation       |
| `in-progress` | Currently being implemented                    |
| `review`      | Implementation complete, awaiting review       |
| `implemented` | Fully implemented and verified                 |
| `deprecated`  | No longer relevant                             |

## Quick Reference

### Create a Specification

```text
# In GitHub Copilot Chat: create a specification interactively
/write-spec
```

```bash
# Or manually create from template (see .github/instructions/spec-writing.instructions.md)
```

### Implement a Specification

```text
# In GitHub Copilot Chat: implement a specification
/implement-spec specs/features/SPEC-001-feature-name.md
```

```bash
# Or list available specs
ls specs/*/
```

### Validate Specification Structure

All specifications should include:

1. **Executive Summary**: Problem, solution, success criteria
2. **User Stories**: Prioritized (P1, P2, P3) with acceptance criteria
3. **Requirements**: Functional requirements with `NEEDS CLARIFICATION` for unclear items
4. **Technical Specification**: API, models, dependencies
5. **Implementation Plan**: Phased deliverables with checkpoints
6. **Task Breakdown**: Tasks with [P] parallel markers
7. **Testing Strategy**: What to test and how

## Key Concepts

Inspired by [GitHub's spec-kit](https://github.com/github/spec-kit):

| Concept                              | Description                             |
| ------------------------------------ | --------------------------------------- |
| **Prioritized Stories (P1, P2, P3)** | P1 = MVP, higher priority first         |
| **Independent Testing**              | Each story testable as standalone MVP   |
| **Parallel Markers [P]**             | Tasks that can run simultaneously       |
| **NEEDS CLARIFICATION**              | Explicit markers for unclear items      |
| **Checkpoints**                      | Validation after each story             |
| **Foundational Phase**               | Blocking prerequisites before ANY story |

## Related Resources

- [.github/instructions/spec-writing.instructions.md](.github/instructions/spec-writing.instructions.md)
- [.github/instructions/spec-navigating.instructions.md](.github/instructions/spec-navigating.instructions.md)
- [.github/instructions/spec-implementation.instructions.md](.github/instructions/spec-implementation.instructions.md)
- [write-spec prompt](/.github/prompts/write-spec.prompt.md)
- [implement-spec prompt](/.github/prompts/implement-spec.prompt.md)
