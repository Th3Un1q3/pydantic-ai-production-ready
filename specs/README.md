# Specifications Directory

This directory contains specifications for features, packages, learning modules, and changes.

## Purpose

Specifications are the **single source of truth** for what to build and how to validate it. They bridge the gap between vision and implementation by providing:

- Clear problem statements and success criteria
- User stories with testable acceptance criteria
- Phased implementation plans with validation gates
- Technical constraints and non-goals

## Directory Structure

```
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

Use the `/write-spec` prompt or invoke the `spec-writer` skill:

```
/write-spec
```

The skill guides you through:

1. **Discovery**: Clarifying questions to understand the scope
2. **Drafting**: Generating a structured specification
3. **Validation**: Ensuring quality standards are met

### 2. Review and Refine

Before implementation, ensure:

- [ ] Problem statement is clear
- [ ] Success criteria are measurable
- [ ] All user stories have acceptance criteria
- [ ] Implementation phases are realistic

### 3. Implement the Specification

Use the `/implement-spec` prompt or invoke the `spec-implementer` skill:

```
/implement-spec specs/features/SPEC-001-course-search.md
```

The skill:

1. Reads and validates the specification
2. Executes phases with validation gates
3. Updates documentation
4. Marks specification as complete

## Naming Convention

```
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

| Status | Description |
|--------|-------------|
| `draft` | Work in progress, not ready for implementation |
| `ready` | Reviewed and approved for implementation |
| `in-progress` | Currently being implemented |
| `review` | Implementation complete, awaiting review |
| `implemented` | Fully implemented and verified |
| `deprecated` | No longer relevant |

## Quick Reference

### Create a Specification

```text
# In GitHub Copilot Chat: create a specification interactively
/write-spec
```

```bash
# Or manually copy a template
cp .github/skills/spec-writer/templates/feature.template.md specs/features/SPEC-XXX-title.md
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
2. **User Stories**: With acceptance criteria
3. **Technical Specification**: API, models, dependencies
4. **Implementation Plan**: Phased deliverables with validation
5. **Testing Strategy**: What to test and how

## Related Resources

- [spec-writer skill](/.github/skills/spec-writer/SKILL.md)
- [spec-implementer skill](/.github/skills/spec-implementer/SKILL.md)
- [write-spec prompt](/.github/prompts/write-spec.prompt.md)
- [implement-spec prompt](/.github/prompts/implement-spec.prompt.md)
