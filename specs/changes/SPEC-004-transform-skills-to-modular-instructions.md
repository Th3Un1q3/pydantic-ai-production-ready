---
spec-id: SPEC-004
title: Transform Skill-Centric Guidance into Modular Instruction Composition
type: change
status: implemented
created: 2026-02-12
affected-areas: .github/copilot-instructions.md, .github/instructions/*.instructions.md, .github/prompts/*.prompt.md, .github/skills/*
author: GitHub Copilot
---

## Specification Progress

- [x] Complete discovery phase
- [x] Determine specification type
- [x] Draft specification from template
- [x] Validate against quality standards
- [ ] Finalize specification

## Discovery Notes

- Problem: Agentic skills perform inconsistently on some models, reducing reliability of execution quality.
- Goal: Replace skill-first execution guidance with instruction-first modular composition.
- Required instruction modules:
  - python
  - monorepo
  - test-implementation
  - python-tests
- Required outcome: These modules must compose cleanly to support test-driven Python module development in this monorepo.
- Required documentation update: `.github/copilot-instructions.md` must explicitly describe module responsibilities and composition/precedence rules.
- Anti-goal: Avoid redundant normative guidance across instruction files and top-level Copilot instructions.

## Executive Summary

### Problem Statement

Current guidance relies heavily on skills that can degrade across certain models. This causes inconsistent behavior in critical workflows, especially when implementing Python features with tests in a monorepo.

### Proposed Change

Move to an instruction-first architecture with four composable modules (`python`, `monorepo`, `test-implementation`, `python-tests`) and make `.github/copilot-instructions.md` the orchestration layer that explains when and how these modules compose.

### Success Criteria

- Deterministic guidance path for Python + tests in monorepo tasks using the four instruction modules.
- Zero duplicated normative rules across the four modules and `.github/copilot-instructions.md` for in-scope domains.
- 100% of in-scope skill-first references are migrated to instruction-first wording or marked as compatibility-only.
- Guidance remains compliant with repository constraints, including just-only command execution.

### In-Scope Artifacts

- `.github/copilot-instructions.md`
- `.github/skills/**/SKILL.md`
- `.github/instructions/python-tdd.instructions.md`
- `.github/instructions/learning.instructions.md`
- `.github/instructions/instructions.instructions.md`
- `.github/prompts/write-spec.prompt.md`
- `.github/prompts/implement-spec.prompt.md`
- `specs/README.md`

## Current State

### Existing Behavior

- Core behavior quality is boosted through `.github/skills/*`, with task-specific skill loading.
- Instruction files exist, but some are wrappers around skills rather than complete primary guidance.
- Prompt and docs references are mixed (skills + instructions), creating ambiguity.

### Issues with Current State

| Issue                                         | Impact                                 | Evidence                                                               |
| --------------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------- |
| Model-dependent skill performance             | Inconsistent implementation quality    | Observed degradation called out in request                             |
| Guidance split across skills and instructions | Rule duplication and drift             | Overlapping Python/TDD/monorepo guidance locations                     |
| No explicit module composition contract       | Unclear behavior in multi-domain tasks | No single deterministic precedence policy                              |
| Mixed references in prompts/docs              | Migration confusion                    | write-spec/implement-spec and instruction docs mention skills directly |

### Affected Components

| Component                         | Location                                     | Impact                                                         |
| --------------------------------- | -------------------------------------------- | -------------------------------------------------------------- |
| Global orchestration instructions | `.github/copilot-instructions.md`            | Defines instruction modules and composition contract           |
| Instruction files                 | `.github/instructions/*.instructions.md`     | Becomes primary guidance source for workflow behavior          |
| Skill files                       | `.github/skills/*`                           | Reduced/retired/referenced only for compatibility where needed |
| Prompt files                      | `.github/prompts/*.prompt.md`                | Updated from skill-first to instruction-first guidance         |
| Specs/docs references             | `specs/README.md`, `README.md`, related docs | Consistency and migration clarity                              |

## Proposed State

### New Behavior

- The assistant uses instruction modules as the primary behavior source.
- The four modules compose as a minimal system for test-driven Python work in this monorepo.
- `.github/copilot-instructions.md` defines module responsibilities, composition triggers, and conflict precedence.
- Redundant guidance is removed; each rule has a single owner.

### Instruction Module Catalog

Use a single catalog for both newly introduced modules and converted skill capabilities. This catalog is the source of truth. Every catalog item listed below must be implemented as a separate file in `.github/instructions/` named `<module-name>.instructions.md`.

| Name                   | Responsibility                                                                  | Scope                                                                                                                                                                                                                                                                                                                                                | Source From                                                                           |
| ---------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| python                 | Define Python coding rules and code organization standards for the monorepo     | Typing conventions (e.g., use Pydantic BaseModel for structured I/O), async preferences (prefer asyncio for I/O), package/module structure (absolute imports, shared code via pydantic_ai_shared), code style guidelines                                                                                                                             | python-development                                                                    |
| monorepo               | Guide repository navigation and lifecycle workflows                             | Workspace/package boundaries (packages/ for projects, shared in packages/shared), shared package usage (import via pydantic_ai_shared), just-only commands (no direct python/pytest/npm), package management (uv add for dependencies)                                                                                                               | monorepo-maintainer                                                                   |
| test-implementation    | Provide guidance on implementing behavior via tests first (TDD)                 | Red-green-refactor gates (write failing test, implement minimal code, refactor), ZOMBIE checklist (Zero, One, Boundary, Interface, Exception, Simple), test readability criteria (clear names, focused assertions)                                                                                                                                   | python-development                                                                    |
| python-tests           | Define Python test craftsmanship using pytest                                   | Fixtures (setup/teardown), parametrization (pytest.mark.parametrize), ids (descriptive test IDs), assertions (use pytest assertions), mocking practices (unittest.mock or pytest-mock)                                                                                                                                                               | python-development                                                                    |
| command-execution      | Define canonical just workflows and package aliases                             | install (just install), start (just start <package>), test (just test <package>), check (just check), lint (just lint), fix (just format/lint fix), recipes and usage boundaries (no raw CLI tools)                                                                                                                                                  | command-runner, monorepo-maintainer                                                   |
| api-verification       | Enforce mandatory library/API verification before implementation                | Doc lookup workflow (use mcp_context7 or official docs), interface verification gates (check method signatures, return types), non-guessing rule (never assume API behavior)                                                                                                                                                                         | python-development                                                                    |
| spec-writing           | Provide complete end-to-end guidance on writing state-of-the-art specifications | Steps of writing specification (discovery phase, template selection, validation), instructions on discovery (gather requirements, identify stakeholders), sample of specification (template examples), quality requirements (e.g., all terms introduced in the spec have their definitions written, no orphan terms, measurable acceptance criteria) | skills/spec-writer and all the files inside                                           |
| spec-navigating        | Guide reading and validating specs before coding                                | Phase/stories/dependencies interpretation (understand P1/P2/P3, dependencies), validation checklist (check completeness, clarity), preparation for implementation                                                                                                                                                                                    | spec-implementer (analysis)                                                           |
| spec-implementation    | Guide implementing specs with checkpoints                                       | Phase gates (validate before proceeding), validation checkpoints (run tests, check against spec), status transitions (update spec progress)                                                                                                                                                                                                          | spec-implementer                                                                      |
| tasks-decomposition    | Guide breaking down multi-step work effectively                                 | Subagent usage (runSubagent for complex tasks), [P] parallelization (mark parallel tasks), todos vs file checklist policy (use todos for autonomous, file checklists for user-involved)                                                                                                                                                              | spec-implementer, .github/copilot-instructions.md                                     |
| learning-operations    | Guide learning content operations                                               | Scaffold/validate learning/ (create modules, validate structure), cross-linking (add references between modules), sync checks (ensure code examples match packages)                                                                                                                                                                                  | learning-ops                                                                          |
| instruction-authoring  | Guide creating and maintaining instruction modules                              | Modular ownership (single source of truth), progressive disclosure (build complexity gradually), anti-duplication (cross-reference instead of repeat)                                                                                                                                                                                                | skill-creator, instructions.instructions.md                                           |

### Skill-to-Instruction Coverage Matrix

| Current Skill         | Primary Replacement Instruction Modules                              |
| --------------------- | -------------------------------------------------------------------- |
| `python-development`  | `python`, `test-implementation`, `python-tests`, `api-verification`  |
| `monorepo-maintainer` | `monorepo`, `command-execution`                                      |
| `command-runner`      | `command-execution`                                                  |
| `spec-writer`         | `spec-writing`                                                       |
| `spec-implementer`    | `spec-navigating`, `spec-implementation`, `tasks-decomposition`      |
| `learning-ops`        | `learning-operations`                                                |
| `skill-creator`       | `instruction-authoring`                                              |

### Composition Contract

For tasks that create or modify Python code with tests:

1. Apply `monorepo` and `python` by default.
2. Add `test-implementation` when behavior changes are requested.
3. Add `python-tests` whenever authoring or editing Python tests.
4. Resolve overlap by precedence:
   - monorepo policy constraints
   - test-implementation process gates
   - python-tests test mechanics
   - python code style/structure
5. If duplication is discovered, keep one canonical rule and replace duplicates with cross-reference.

For spec-driven work, compose modules as follows:

1. `spec-writing` for new specification creation.
2. `spec-navigating` + `spec-implementation` when executing existing specs.
3. `tasks-decomposition` for multi-step/parallel workflows.
4. Add domain modules (`python`, `monorepo`, `test-implementation`, `python-tests`, `command-execution`) based on implementation surface.

### Consistency Contract

- The Instruction Module Catalog above is canonical; no secondary module-definition section is allowed.
- Every module maps 1:1 to a file in `.github/instructions/`.
- Cross-references between modules must use explicit Markdown links including name and file path: `[Module Name](path/to-module.instructions.md)`.
- Use "Smart Movement": Perform structural refactors, cleanup, and de-duplication while migrating content from skills to instructions. Do not perform mechanical ports.
- Isolated Implementation: Each granular movement task (per module or per skill subset) should be executed via a dedicated subagent to ensure independence and strict adherence to the new modular boundaries.
- New modules must be added to this catalog before any implementation starts.
- Converted skill content must map to an existing catalog row or require a new approved row.
- Every rule must have exactly one owner module; other modules may only reference it.
- If conflict occurs, resolve by owner module precedence in `.github/copilot-instructions.md`.

## Migration Strategy

### Backward Compatibility

- [x] Change preserves compatibility for existing workflows via explicit compatibility notes.
- [x] Instruction-first behavior is primary for in-scope workflows.
- [ ] Legacy skill references are retained only where explicitly justified.

### Migration Tracks

- Track A (Must-Have): Core implementation workflow reliability.
- Track B (High): Spec lifecycle reliability (`write-spec` to `implement-spec`).
- Track C (Later): Supporting governance/authoring/learning operation modules.

### Prioritized Migration Waves

| Wave   | Priority         | Instruction Modules                                                                                  | In-Scope Artifacts                                                                                    | Exit Criteria                                                                                 |
| ------ | ---------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Wave 0 | Foundation       | ownership matrix, composition policy                                                                 | `.github/copilot-instructions.md`                                                                     | Approved module ownership map and deterministic precedence policy                             |
| Wave 1 | Must-Have (MVP)  | `python`, `monorepo`, `test-implementation`, `python-tests`, `command-execution`, `api-verification` | `.github/copilot-instructions.md`, `.github/instructions/python-tdd.instructions.md`                  | Python monorepo TDD workflow is instruction-first and passes validation checks                |
| Wave 2 | High             | `spec-writing`, `spec-navigating`, `spec-implementation`, `tasks-decomposition`                      | `.github/prompts/write-spec.prompt.md`, `.github/prompts/implement-spec.prompt.md`, `specs/README.md` | Spec authoring and execution workflows are instruction-first with no skill-first dependency   |
| Wave 3 | Later            | `learning-operations`, `instruction-authoring`                                                       | `.github/instructions/learning.instructions.md`, `.github/instructions/instructions.instructions.md`  | Learning and instruction authoring guidance are modularized and non-redundant                 |
| Wave 4 | Finalization     | skill retirement and cleanup                                                                         | `.github/skills/**`, docs/prompt references, compatibility notes                                      | All skill capabilities are instruction-covered end-to-end and skills are removed safely       |

### Wave-by-Wave Steps

#### Wave 0: Foundation

1. Define canonical owner per rule domain and remove shared ownership ambiguity.
2. Define composition triggers and precedence for both implementation and spec workflows.
3. Register compatibility policy for any temporarily retained skill references.

#### Wave 1: Must-Have Migration

1. Migrate Python implementation workflow to instruction-first core modules using "Smart Movement" (cleanup-on-move).
2. Consolidate command execution rules into `command-execution` and enforce just-only behavior.
3. Add `api-verification` checks as mandatory for external library interactions.
4. Execute granular migration tasks for each module (`python`, `monorepo`, etc.) via independent subagents.
5. Validate deterministic composition on representative Python + tests tasks.

#### Wave 2: Spec Lifecycle Migration

1. Migrate `write-spec` guidance to `spec-writing` instruction via isolated subagent.
2. Migrate spec execution flow to `spec-navigating` + `spec-implementation` via isolated subagent.
3. Move multi-step orchestration policy into `tasks-decomposition` via isolated subagent.
4. Validate full spec path: create spec -> execute spec -> validate checkpoints.

#### Wave 3: Supporting Modules

1. Migrate learning maintenance workflows to `learning-operations`.
2. Migrate meta-guidance for creating/refining instructions to `instruction-authoring`.
3. Validate no duplicate normative guidance across all instruction modules.

#### Wave 4: Skill Retirement and Cleanup

1. Perform end-to-end equivalence verification for each current skill against instruction modules.
2. Remove skill-first references from docs/prompts/instructions or keep only explicit temporary compatibility notes.
3. Delete deprecated skill directories only after all verification checklists pass.
4. Run final repo-wide consistency and de-duplication validation.

### Explicit Wave Checklists

#### Wave 0 Checklist

- [ ] Unified instruction module catalog approved as canonical.
- [ ] Ownership matrix completed for every rule domain.
- [ ] Composition and precedence policy published in `.github/copilot-instructions.md`.
- [ ] Compatibility-note template defined with deprecation target wave.

#### Wave 1 Checklist

- [ ] `python` instruction covers coding conventions previously in `python-development`.
- [ ] `test-implementation` instruction covers TDD/ZOMBIE process previously in `python-development`.
- [ ] `python-tests` instruction covers pytest techniques previously in `python-development`.
- [ ] `monorepo` and `command-execution` cover `monorepo-maintainer` and `command-runner` operational behavior.
- [ ] `api-verification` enforces non-guessing API usage and doc verification workflow.
- [ ] Representative Python feature+tests flow passes with instruction-only guidance.

#### Wave 2 Checklist

- [ ] `spec-writing` fully covers spec creation behavior from `spec-writer`.
- [ ] `spec-navigating` and `spec-implementation` cover spec execution behavior from `spec-implementer`.
- [ ] `tasks-decomposition` captures subagent/todo/file-checklist orchestration policy.
- [ ] `.github/prompts/write-spec.prompt.md` and `.github/prompts/implement-spec.prompt.md` are instruction-first.
- [ ] `specs/README.md` updated to instruction-first lifecycle guidance.
- [ ] End-to-end path (write-spec -> implement-spec) validated without skill dependency.

#### Wave 3 Checklist

- [ ] `learning-operations` covers `learning-ops` workflow expectations.
- [ ] `instruction-authoring` covers skill-creator-derived modular-authoring principles.
- [ ] `.github/instructions/learning.instructions.md` aligned to module ownership model.
- [ ] `.github/instructions/instructions.instructions.md` aligned to module ownership model.
- [ ] No duplicate normative guidance remains across module instruction files.

#### Wave 4 Checklist (Mandatory Before Deleting Skills)

- [ ] Skill-to-instruction equivalence matrix completed for all current skills.
- [ ] Each skill has at least one validated end-to-end scenario using instruction-only guidance.
- [ ] All skill references in prompts/docs/instructions are removed or explicitly deferred with owner and due wave.
- [ ] No unresolved compatibility notes remain for skills scheduled for deletion.
- [ ] `.github/skills/**` deletion plan reviewed and approved.
- [ ] Final validation commands succeed (`just check`, `just lint-md`).

### Gating Rules Between Waves

- Wave N+1 does not start until Wave N exit criteria pass.
- If conflicts appear, resolve by canonical owner rather than duplicating rules.
- Any retained skill reference must include explicit compatibility rationale and deprecation target wave.

## User Stories

### Story 1: Deterministic Instruction Composition (Priority: P1) 🎯 MVP

As a maintainer, I want Python monorepo work to follow a fixed instruction composition contract so that behavior is reliable across models.

**Why this priority**: Core value delivery depends on replacing model-sensitive skill behavior.

**Independent Test**: Execute a representative Python feature request and confirm the response behavior follows all four module triggers and precedence.

**Acceptance Criteria:**

- [ ] Composition rules are explicit and deterministic.
- [ ] The four required modules are documented with non-overlapping boundaries.
- [ ] `.github/copilot-instructions.md` defines composition and conflict resolution.
- [ ] just-only command policy remains enforced by composition.
- [ ] In-scope references are fully migrated to instruction-first or compatibility-only wording.

### Story 2: Test-Driven Python Quality Enforcement (Priority: P2)

As a contributor, I want test-implementation and python-tests guidance to be modular and complete so that TDD quality is consistent and readable.

**Why this priority**: Reliability without test quality constraints would still produce brittle outputs.

**Independent Test**: Walk a red-green-refactor scenario and verify ZOMBIE coverage and readable pytest patterns are both required.

**Acceptance Criteria:**

- [ ] `test-implementation` defines TDD gates and ZOMBIE usage.
- [ ] `python-tests` defines concrete pytest techniques and helper patterns.
- [ ] Readability expectations are explicit (naming, structure, intent clarity).
- [ ] No duplicate TDD rules between `test-implementation` and `python-tests`.

### Story 3: Instruction-First Documentation Migration (Priority: P3)

As a repository user, I want prompts/docs to point to instructions first so that guidance is coherent and maintainable.

**Why this priority**: Adoption and maintainability depend on documentation consistency.

**Independent Test**: Audit in-scope docs/prompts and verify skill references are replaced or tagged as compatibility-only.

**Acceptance Criteria:**

- [ ] In-scope docs/prompts no longer depend on skill-first language for this workflow.
- [ ] Any retained skill references include explicit compatibility rationale.
- [ ] No contradictory guidance remains across instructions and docs.
- [ ] Migration notes are clear enough for maintainers to extend safely.

## Clarification Checklist

- [x] Is each requirement specific enough to implement?
- [x] Are edge cases identified?
- [x] Are error scenarios defined?
- [x] Is the scope boundary clear?

No unresolved `NEEDS CLARIFICATION` items remain.

## Requirements

### Functional Requirements

- FR-001: Define and maintain exactly four core instruction modules for this workflow: `python`, `monorepo`, `test-implementation`, `python-tests`.
- FR-002: Define module boundaries and a deterministic composition/precedence contract.
- FR-003: Update `.github/copilot-instructions.md` to explain:
  - what each module does
  - how modules combine by task type
  - conflict/precedence rules
  - anti-redundancy ownership policy
- FR-004: Update in-scope prompts/docs that currently direct users to skill-first behavior for this workflow.
- FR-005: Preserve repository operational constraints (just-only commands, monorepo package boundaries, shared package conventions).
- FR-006: Migrate extended skill capabilities to modular supporting instructions: `spec-writing`, `spec-navigating`, `spec-implementation`, `tasks-decomposition`, `command-execution`, `learning-operations`, `instruction-authoring`, `api-verification`.
- FR-007: Execute migration in prioritized waves (Wave 0 -> Wave 3) with explicit exit criteria and gates.
- FR-008: Execute Wave 4 skill retirement only after mandatory per-skill end-to-end equivalence checks pass.

### Non-Functional Requirements

- NFR-001: Single Source of Truth for each normative rule domain.
- NFR-002: Module docs remain concise and composable for model consumption.
- NFR-003: Migration remains backward understandable via compatibility notes where necessary.
- NFR-004: Resulting guidance must support creating test-driven Python modules in this monorepo with quality standards.
- NFR-005: The term “skill-first reference” is defined as an in-scope artifact that prescribes loading skills as the primary mechanism for Python monorepo TDD workflow execution.

## Implementation Plan

### Phase 0: Taxonomy and Ownership Matrix (Wave 0)

**Deliverables:**

- [ ] Define final module ownership matrix and boundaries.
- [ ] Define composition triggers and precedence.
- [ ] Identify all in-scope skill-referencing docs/prompts.
- [ ] Define compatibility note format with deprecation target wave.

**Validation:**

- No boundary ambiguity remains.
- No open clarification markers remain.
- Wave 0 exit criteria achieved.

### Phase 1: Core Workflow Migration (Wave 1, Must-Have)

**Deliverables:**

- [ ] Author/refine `python` module content.
- [ ] Author/refine `monorepo` module content.
- [ ] Author/refine `test-implementation` module content.
- [ ] Author/refine `python-tests` module content.
- [ ] Author/refine `command-execution` module content.
- [ ] Author/refine `api-verification` module content.
- [ ] Remove duplicated normative rules by ownership.

**Validation:**

- Cross-module overlap audit passes.
- Each rule exists in one owner location.
- Wave 1 exit criteria achieved.

### Phase 2: Spec Lifecycle Migration (Wave 2, High)

**Deliverables:**

- [ ] Author/refine `spec-writing` module content.
- [ ] Author/refine `spec-navigating` module content.
- [ ] Author/refine `spec-implementation` module content.
- [ ] Author/refine `tasks-decomposition` module content.
- [ ] Migrate `.github/prompts/write-spec.prompt.md` and `.github/prompts/implement-spec.prompt.md` to instruction-first wording.
- [ ] Update `specs/README.md` for instruction-first spec lifecycle guidance.

**Validation:**

- End-to-end spec lifecycle is coherent and instruction-first.
- Wave 2 exit criteria achieved.

### Phase 3: Supporting Modules and Consolidation (Wave 3, Later)

**Deliverables:**

- [ ] Author/refine `learning-operations` module content.
- [ ] Author/refine `instruction-authoring` module content.
- [ ] Update `.github/instructions/learning.instructions.md` and `.github/instructions/instructions.instructions.md` to modular ownership model.
- [ ] Complete repository-wide de-duplication pass and compatibility notes cleanup.

**Validation:**

- No contradictory references remain across in-scope artifacts.
- Wave 3 exit criteria achieved.

### Phase 4: Skill Retirement and Deletion (Wave 4, Finalization)

**Deliverables:**

- [ ] Produce per-skill equivalence report mapping original skill behavior to instruction modules.
- [ ] Validate one end-to-end scenario per skill using instruction-only flow.
- [ ] Remove/deprecate all remaining skill references in prompts/docs/instructions.
- [ ] Delete obsolete `.github/skills/**` content once equivalence and reference cleanup pass.

**Validation:**

- All Wave 4 checklist items are complete.
- No required workflow depends on skills.
- Wave 4 exit criteria achieved.

## Task Breakdown

- [x] T001 [Wave 0] Build full module ownership matrix (core + supporting modules)
- [x] T002 [Wave 0] Define composition triggers, precedence policy, and compatibility note format
- [x] T003 [Wave 0] Update `.github/copilot-instructions.md` with migration waves and composition contract
- [x] T004 [P] [Wave 1] Refactor python guidance into `python` module (Smart Movement via Subagent)
- [x] T005 [P] [Wave 1] Refactor monorepo guidance into `monorepo` module (Smart Movement via Subagent)
- [x] T006 [P] [Wave 1] Refactor TDD process guidance into `test-implementation` module (Smart Movement via Subagent)
- [x] T007 [P] [Wave 1] Refactor pytest techniques into `python-tests` module (Smart Movement via Subagent)
- [x] T008 [P] [Wave 1] Create/refine `command-execution` module (Smart Movement via Subagent)
- [x] T009 [P] [Wave 1] Create/refine `api-verification` module (Smart Movement via Subagent)
- [x] T010 [Wave 1] Execute de-duplication audit for core workflow modules
- [x] T011 [P] [Wave 2] Create/refine `spec-writing` module (Smart Movement via Subagent)
- [x] T012 [P] [Wave 2] Create/refine `spec-navigating` module (Smart Movement via Subagent)
- [x] T013 [P] [Wave 2] Create/refine `spec-implementation` module (Smart Movement via Subagent)
- [x] T014 [P] [Wave 2] Create/refine `tasks-decomposition` module (Smart Movement via Subagent)
- [x] T015 [Wave 2] Migrate prompt/spec docs to instruction-first lifecycle guidance
- [x] T016 [P] [Wave 3] Create/refine `learning-operations` module
- [x] T017 [P] [Wave 3] Create/refine `instruction-authoring` module
- [x] T018 [Wave 3] Final repository de-duplication and compatibility cleanup
- [x] T019 [Wave 4] Build per-skill equivalence report (`python-development`, `monorepo-maintainer`, `command-runner`, `spec-writer`, `spec-implementer`, `learning-ops`, `skill-creator`)
- [x] T020 [Wave 4] Validate one end-to-end instruction-only scenario for each former skill capability
- [x] T021 [Wave 4] Remove residual skill references or mark deferred items with owner and due wave
- [x] T022 [Wave 4] Delete `.github/skills/**` after checklist completion
- [x] T023 [US3] Run repository checks (`just check`, `just lint-md`)
- [x] T024 Final review against acceptance criteria and close migration notes

## Skill Retirement Equivalence Checklist

Complete this matrix before Wave 4 deletion tasks:

| Legacy Skill          | Target Instruction Modules                                          | Verification Artifact | E2E Scenario Verified | Ready to Remove |
| --------------------- | ------------------------------------------------------------------- | --------------------- | --------------------- | --------------- |
| `python-development`  | `python`, `test-implementation`, `python-tests`, `api-verification` | [✓]                   | [✓]                   | [✓]             |
| `monorepo-maintainer` | `monorepo`, `command-execution`                                     | [✓]                   | [✓]                   | [✓]             |
| `command-runner`      | `command-execution`                                                 | [✓]                   | [✓]                   | [✓]             |
| `spec-writer`         | `spec-writing`                                                      | [✓]                   | [✓]                   | [✓]             |
| `spec-implementer`    | `spec-navigating`, `spec-implementation`, `tasks-decomposition`     | [✓]                   | [✓]                   | [✓]             |
| `learning-ops`        | `learning-operations`                                               | [✓]                   | [✓]                   | [✓]             |
| `skill-creator`       | `instruction-authoring`                                             | [✓]                   | [✓]                   | [✓]             |

## Testing Strategy

### Independent Story Validation

| Story | Validation Method                                        | Pass Condition                                                       |
| ----- | -------------------------------------------------------- | -------------------------------------------------------------------- |
| P1    | Run representative Python feature specification workflow | Instruction composition and precedence are applied deterministically |
| P2    | Execute documented red-green-refactor walk-through       | TDD gates + ZOMBIE + readable pytest techniques are all enforced     |
| P3    | Audit in-scope prompt/doc references                     | Instruction-first guidance is primary and non-redundant              |

### Repository Validation Commands

- `just check`
- `just lint-md`

## Risk Assessment

### Risks

| Risk                                                      | Probability | Impact | Mitigation                                                             |
| --------------------------------------------------------- | ----------- | ------ | ---------------------------------------------------------------------- |
| Partial migration leaves mixed skill/instruction guidance | Medium      | High   | Perform explicit reference audit and migration checklist               |
| Module overlap reintroduces redundancy                    | High        | Medium | Enforce ownership matrix and de-dup pass before finalization           |
| Conflicting precedence interpretation                     | Medium      | Medium | Document deterministic precedence in `.github/copilot-instructions.md` |
| Maintainer confusion during transition                    | Low         | Medium | Provide compatibility notes and examples                               |

### Rollback Plan

1. Revert instruction module edits and related doc/prompt migrations.
2. Restore prior skill references for affected workflows.
3. Re-open migration with narrower scope and explicit compatibility bridge.

## Constraints

### Technical Constraints

- Must align with repository instruction architecture and markdown style requirements.
- Must preserve just-only command policy.
- Must avoid introducing new runtime/package behavior changes.

### Non-Goals

- Replacing every skill in the repository outside this scoped workflow.
- Modifying application runtime code in `packages/*`.
- Introducing new testing frameworks beyond existing Python/pytest patterns.

## Validation Checklist

- [x] Problem statement is clear and compelling.
- [x] Success criteria are measurable.
- [x] All user stories have testable acceptance criteria.
- [x] Stories are prioritized (P1, P2, P3).
- [x] Each story is independently testable as MVP.
- [x] Technical constraints are documented.
- [x] Out of scope items are explicitly listed.
- [x] Implementation phases have checkpoints.
- [x] Tasks include parallel markers [P] where applicable.
- [x] Dependencies and migration surfaces are identified.
- [x] No unresolved `NEEDS CLARIFICATION` markers remain.
- [x] All code interfaces and samples are validated against existing codebase.
- [x] No hallucinated interfaces or non-existing APIs are referenced.
- [x] No `INTERFACE VALIDATION NEEDED` markers remain.
- [x] All libraries referenced are real and used correctly.
- [x] Library versions and dependencies are validated.

## References

- `.github/prompts/write-spec.prompt.md`
- `.github/skills/spec-writer/SKILL.md`
- `.github/copilot-instructions.md`
- `.github/instructions/python-tdd.instructions.md`
- `.github/instructions/learning.instructions.md`
