---
spec-id: SPEC-001
title: Refine Module 01 Foundations
type: learning
status: implemented
created: 2026-02-11
---

## Executive Summary

### Problem Statement

The current "Foundations" module (`learning/01-fundamentals/`) is misaligned with the strict "Enterprise/Experienced" persona of the course.

- **Audience Mismatch**: Content explains basic Python concepts and uses overly simplistic "toy" examples inline, rather than referencing production-grade patterns.
- **Redundancy**: `02-setup.md` partially duplicates verification steps from `GETTING_STARTED.md` without being authoritative.
- **Code Disconnect**: The learning material relies on throwaway code block examples instead of analyzing the actual `packages/course-navigator` implementation, creating a drift between theory and the monorepo's practice.

### Proposed Solution

Restructure Module 01 to focus on **Architecture and Patterns** rather than "coding basics".

1. **Refine L02 (Setup)**: Remove verification steps; point to `GETTING_STARTED.md`. Focus the lesson on the *Why* of the stack (Monorepo, `just`, `uv` benefits for teams).
2. **Refactor L03 (Anatomy)**: Rename to "Anatomy of an Enterprise Agent". Instead of writing code from scratch, analyze the `course-navigator` package to explain:
    - Factory Pattern (for testability).
    - Configuration Management (using `pydantic_ai_shared`).
3. **Draft Implementation Spec**: Create a companion specification (`SPEC-003`) to upgrade the current "Hello World" `course-navigator` into a "Structured Output" baseline, ensuring the code matches the lesson's architectural complexity.

### Success Criteria

1. **Single Source of Truth**: All setup/verification instructions delegate to `GETTING_STARTED.md`.
2. **Code-Lesson Parity**: Lesson 03 references files in `packages/course-navigator` instead of using large inline code blocks.
3. **Persona Alignment**: Tone assumes the reader is a Senior/Architect (skips `async/await` basics, focuses on DI/Factories).
4. **Actionable Implementation Plan**: A draft of `SPEC-003` is produced to bring the Python code up to the baseline required by the lesson.
5. **Concept Integration**: The module explicitly introduces and links to core architectural concepts defined in `CONCEPTS.md`.

## Out of Scope

- **Advanced Verification**: We will not add new scripts to `scripts/` or `packages/` for verification; we rely strictly on `just check` / `just start` existing in `GETTING_STARTED.md`.
- **Complex Logic**: The agent in Lesson 03 will handle structured output but will *not* yet implement RAG or Database calls (reserved for L04/Module 03).
- **Deployment**: Production deployment (Docker, K8s) is reserved for Module 04.

## Key Concepts Coverage

The following core concepts from `CONCEPTS.md` must be introduced and demonstrated:

| Concept                     | Introduction Point | Demonstration                                           |
| :-------------------------- | :----------------- | :------------------------------------------------------ |
| **Agents**                  | L03                | The `Agent` class in `course-navigator/agent.py`        |
| **System Prompts**          | L03                | The identity definition in `create_agent`               |
| **Structured Output**       | L03                | The `CourseModule` return type (via SPEC-003)           |
| **Dependencies (`deps`)**   | L03                | Introduction to Runtime State vs Configuration          |
| **Model Selection**         | L03                | Utilization of `resolve_model` for provider comparisons |
| **Observability (Logfire)** | L02                | Mentioned as part of the "Sandbox" stack                |

## Learning Objectives

By the end of this module, learners will be able to:

1. **Articulate** the benefits of the Monorepo/`uv`/`just` stack for enterprise AI teams, including **Observability**.
2. **Navigate** the `course-navigator` package structure to locate **Agent** methodology.
3. **Explain** the "Factory Pattern" for **System Prompts** and agent instantiation.
4. **Identify** how `pydantic_ai_shared` isolates **Model Selection** from agent logic.
5. **Define** the role of **Structures Output** and **Dependencies** in creating reliable agents.

## User Stories

### Story 1: Architecture-First Setup (Priority: P1)

**As an** Enterprise Architect,
**I want** to understand the "Development Sandbox" (Monorepo, Tools),
**So that** I can justify this standard infrastructure to my team.

*Acceptance Criteria:*

- `02-setup.md` focuses on the *architecture* of the dev environment.
- Explicit links to `GETTING_STARTED.md` for the actual "do this" steps.
- Explains the role of `packages/shared` vs `packages/course-navigator`.

### Story 2: Anatomy of a Production Agent (Priority: P1)

**As a** Senior Python Engineer,
**I want** to dissect the `course-navigator` agent,
**So that** I can understand the required boilerplate (Factories, Config) for a production app.

*Acceptance Criteria:*

- `03-first-agent.md` renamed to `03-agent-anatomy.md`.
- Content analyzes `packages/course-navigator/src/course_navigator/agent.py`.
- Explains:
  - `create_agent()` factory function.
  - Model resolution via `resolve_model` (referencing `shared`).
  - *Note*: Relies on `course-navigator` being updated via SPEC-003.
- **Concept Integration**: Explicitly defines and links to `CONCEPTS.md` for:
  - **Agents** (The orchestration container)
  - **System Prompts** (Static vs Dynamic instructions)
  - **Dependencies** (Introduction to Type-Safe DI)

### Story 3: Defined Baseline Implementation (Priority: P1)

**As a** Course Author,
**I want** a specification to update the `course-navigator` code,
**So that** the code properly demonstrates the patterns (Structured Output, Factories) taught in Lesson 03.

*Acceptance Criteria:*

- `specs/packages/SPEC-003-course-navigator-baseline.md` is created.
- Requirements:
  - Update `course-navigator` to return a Pydantic Model (**Structured Output**) instead of string.
  - Ensure Factory Pattern is robust.
  - Ensure `pydantic_ai_shared` is used for **Model Selection**.

## Advice for Spec Implementation

- **Minimize Inline Code**: Use links like `[agent.py](../../packages/course-navigator/src/course_navigator/agent.py)` instead of pasting 50 lines of code.
- **Respect the Reader**: Do not explain what a Virtual Environment is. Explain why `uv` is faster/better for locking.
- **Linearity**: Ensure L02 context (Monorepo structure) helps L03 (Where is `agent.py`?).

## Implementation Progress

- [x] Phase 0: Foundational (blocking prerequisites)
- [x] CHECKPOINT: Foundation ready
- [x] Phase 1: User Story 1 (P1) 🎯 MVP
- [x] CHECKPOINT: Story 1 independently testable
- [x] Phase 2: User Story 2 (P2)
- [x] CHECKPOINT: Story 2 independently testable
- [x] Documentation updates
- [x] Final validation

## Implementation Plan

### Phase 1: Clean Up & Link (Content)

- [ ] **Task 1.1** [P]: Rewrite `02-setup.md` to be "Architecture of the Sandbox". Link to `GETTING_STARTED.md`.
- [ ] **Task 1.2** [P]: Rename `03-first-agent.md` -> `03-agent-anatomy.md`.

### Phase 2: Define Practice (Code Spec)

- [ ] **Task 2.1**: Create `specs/packages/SPEC-003-course-navigator-baseline.md`. Use the `spec-writer` skill.
  - Focus: Upgrade `course-navigator` to use Structured Output (e.g., return a `CourseModule` object).

### Phase 3: Content Refinement

- [ ] **Task 3.1**: Write `03-agent-anatomy.md`.
  - It should describe the code *as if SPEC-003 is implemented*.
  - Focus on the *Pattern*: "Notice how we define the return type as `CourseModule` to guarantee structure."

## Specification Progress

- [x] Complete discovery phase
- [x] Determine specification type (Learning)
- [x] Draft specification `SPEC-001`
- [x] Validate against quality standards
- [x] Finalize specification

## Discovery Notes

- **Audience**: Experienced/Senior.
- **Verification**: `GETTING_STARTED.md` is the SSoT.
- **Code State**: `course-navigator` is currently too simple ("Hello World"). Needs an update (SPEC-003) to match the "Production Patterns" promise of the course.
