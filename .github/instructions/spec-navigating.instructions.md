---
description: Guidance for reading, analyzing, and validating existing specifications before starting implementation.
applyTo: '**/specs/**/*.md'
---

# Specification Navigation

Before beginning implementation, a rigorous analysis of the specification is required to ensure feasibility, clarity, and architectural alignment. This is a mandatory pre-coding step.

## Analysis Workflow

### 1. Structural Validation
Verify that the specification file contains all required sections as defined in [.github/instructions/spec-writing.instructions.md](.github/instructions/spec-writing.instructions.md):
- [ ] **Executive Summary**: Clear problem statement and success criteria.
- [ ] **Prioritized User Stories**: P1 (MVP), P2, P3 ranking.
- [ ] **Acceptance Criteria**: Testable requirements for each story.
- [ ] **Implementation Plan**: Phases with clear checkpoints and Phase 0 (Foundations).
- [ ] **Task Breakdown**: Detailed tasks with parallel markers `[P]`.
- [ ] **Testing Strategy**: How success will be verified.

### 2. Clarity Check
- **Resolve Unknowns**: Scan for `NEEDS CLARIFICATION` markers. These must be resolved with the user before starting work.
- **Identify Ambiguity**: Flags requirements that lack concrete metrics or clear success criteria.
- **Boundaries**: Ensure "Out of Scope" clearly defines what *not* to build.

### 3. Dependency Mapping
- **Sequential Flow**: Analyze the task breakdown to identify blocking tasks and dependencies between user stories.
- **Parallel Opportunities**: Note tasks marked `[P]` for parallel execution.
- **External Dependencies**: Identify new libraries, environment variables, or cross-package imports (refer to [.github/instructions/monorepo.instructions.md](.github/instructions/monorepo.instructions.md)).

### 4. Interface Verification
Confirm that all technical details in the spec are grounded in reality:
- **Existing Code**: Use search tools to verify referenced class names, module paths, and function signatures.
- **Proposed Interfaces**: Check `INTERFACE VALIDATION NEEDED` markers. Verify that proposed names and patterns align with the codebase's existing architecture.
- **Library Check**: Confirm all listed libraries are valid and suitable for the task.

## Verification Checklist

Confirm readiness with this checklist:
- [ ] **Understanding**: All P1 stories are fully understood and testable.
- [ ] **Foundations**: Phase 0 foundational tasks (config, boilerplate, migrations) are identified.
- [ ] **Accuracy**: All referenced code interfaces have been verified against the current codebase.
- [ ] **Consistency**: No contradictory requirements exist within the spec.
- [ ] **Tooling**: Testing strategy is executable using `just test` and `just check`.
- [ ] **Context**: Relevant instruction modules (e.g., `python`, `monorepo`) have been loaded.

## Transition to Implementation

Once analysis is complete:
1. **Confirm MVP**: Summarize the P1 (MVP) scope to the user.
2. **Setup**: Load the [.github/instructions/spec-implementation.instructions.md](.github/instructions/spec-implementation.instructions.md) module.
3. **Status**: Update the specification frontmatter status to `ready`.
4. **Questions**: If ambiguities remain, provide a list of specific, numbered questions.
