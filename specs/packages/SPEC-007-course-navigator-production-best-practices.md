---
spec-id: SPEC-007
title: Harden Course Navigator With Production Best Practices
type: package
status: ready
created: 2026-03-08
owner: ai-engineer
related-specs:
  - SPEC-003
  - SPEC-006
---

## Specification Progress

- [x] Complete discovery phase
- [x] Determine specification type
- [x] Draft specification from template
- [x] Validate against quality standards
- [x] Finalize specification for review

## Discovery Notes

- Canonical guidance followed for this draft: `.github/instructions/spec-writing.instructions.md`, `.github/prompts/write-spec.prompt.md`, `specs/README.md`, and `.github/instructions/markdown.instructions.md`.
- Baseline and follow-up context inspected: `specs/packages/SPEC-003-course-navigator-baseline.md` and `specs/features/learning/SPEC-006-align-foundations-with-production-best-practices.md`.
- Course Navigator package discovery was validated against actual package files, including `packages/course-navigator/README.md`, `pyproject.toml`, `justfile`, source files under `src/course_navigator/`, tests under `tests/`, and shared runtime helpers in `packages/shared/src/pydantic_ai_shared/`.
- Current validated strengths:
  - The package already uses explicit output contracts via `CourseAnswer` and `CourseReference`.
  - Request-scoped dependency injection already exists via `NavigatorDeps`.
  - Provider/model resolution is already abstracted in shared code via `resolve_model()`.
  - Lesson access already follows a zero-trust filesystem posture through an index allowlist, path normalization, traversal rejection, and symlink escape protection.
  - Logfire bootstrap already exists in the CLI entrypoint.
  - The package already has substantial unit and integration coverage, and tests disable real model requests by default.
- Current validated gaps that justify this follow-up spec:
  - Runtime configuration is still implicit and partly hard-coded in `main.py`.
  - CLI execution does not currently apply explicit `UsageLimits`, even though the baseline spec expected safety limits.
  - System prompt construction is inline and not governed as a versioned prompt asset.
  - Prompt trust boundaries are not explicitly separated between privileged instructions, indexed context, and user-controlled fields.
  - Observability is initialized, but run metadata and operator-facing diagnostics are still thin.
  - The package has tests, but the hardening gate is not yet defined around production-style startup validation, prompt revisioning, and fail-fast behavior.
  - Dependency footprint has not yet been reviewed for a slimmer installation strategy.
- This specification is package-only follow-up work. It does not modify learning materials and does not expand Course Navigator into a broader product.

## Executive Summary

### Problem Statement

Course Navigator was intentionally implemented as a strong but imperfect baseline. That baseline now sits behind Module 01, which teaches production-oriented practices such as explicit contracts, reproducible workflows, zero-trust prompt handling, configuration isolation, fail-fast validation, and observability.

The package already demonstrates several of those ideas, but not yet in a form that should be treated as the production-ready reference. The remaining gap is not new product scope. It is hardening scope: make the existing single-agent package more explicit, auditable, deterministic, and operationally disciplined without losing its current educational simplicity.

### Proposed Solution

Harden the current Course Navigator package in a staged way that preserves the existing architecture while making production-minded concerns explicit:

- formalize runtime contracts for model/provider selection, startup configuration, usage limits, and dependency boundaries;
- isolate privileged prompt instructions from user-controlled and retrieved context, and version prompt assets for auditability;
- strengthen backend-style testing and deterministic quality gates around startup, validation, and runtime safety behavior;
- enrich observability and operator diagnostics so runs are easier to inspect and debug;
- capture, but defer, advanced hardening items that would add complexity without being necessary for the first hardening pass.

### Success Criteria

- Course Navigator hardening remains scoped to the existing package and does not introduce unrelated product features.
- The specification translates Module 01 best practices into concrete package stories, requirements, and phased work.
- The first hardening pass defines clear must-have changes for runtime contracts, prompt governance, fail-fast validation, deterministic quality gates, and observability.
- Deferred items are explicitly recorded so future work is visible without being prematurely committed.
- The spec is implementation-ready and contains no unresolved `NEEDS CLARIFICATION` markers.

## Scope

### In Scope

- Follow-up hardening work for `packages/course-navigator/`.
- Package runtime concerns: startup configuration, provider/model abstraction boundaries, dependency injection discipline, prompt governance, fail-fast validation, usage limits, observability, and package-level quality gates.
- Updating package documentation and tests as needed to support the hardened behavior.
- Preserving the current single-agent, local-learning-material navigation scope while making it more production-minded.

### Out of Scope

- Implementing this specification in this task.
- Changes to Module 01 learning documents.
- Expanding Course Navigator into vector RAG, a multi-agent system, a web UI, or a generalized knowledge platform.
- Repository-wide CI/CD redesign beyond what is necessary to define package-level hardening gates.
- Advanced operational features that have not been validated as necessary for the first hardening pass.

## Validated Current State

### Existing Foundations Worth Preserving

- `models.py` already defines narrow, explicit contracts for agent output and request-scoped dependencies.
- `agent.py` already uses a dynamic `system_prompt` factory and keeps the package on a single-agent architecture.
- `tools.py` already enforces path allowlisting and filesystem boundary checks suitable for zero-trust local file access.
- `utils.py` already builds a deterministic lesson index from frontmatter-aware parsing of the learning tree.
- `main.py` already centralizes CLI launch mode selection, shared model resolution, and Logfire initialization.
- The test suite already covers models, tools, indexing, CLI behavior, agent construction, and one deterministic integration path.

### Gaps Driving This Specification

- Startup configuration is not yet treated as a typed, validated runtime contract.
- User defaults and runtime controls are still hard-coded in the CLI path.
- Usage limits are not enforced in the interactive runtime path.
- Prompt instructions are not versioned or isolated as governed assets.
- Prompt composition does not yet make trust boundaries explicit between privileged instructions and untrusted content.
- Observability exists, but it does not yet expose enough execution metadata for review and debugging.
- The package workflow does not yet clearly define a production-style minimum gate such as `just check course-navigator`.
- Some hardening ideas introduced in Module 01 remain better treated as deferred options unless implementation discovery proves them necessary.

## Module 01 Best-Practice Translation

- **Model/provider abstraction**
  - Validated current state: Shared `resolve_model()` already chooses provider from environment state.
  - Hardening direction: Keep provider resolution behind an explicit package runtime contract and surface resolved model/provider in tests and diagnostics.
  - Bucket: Must-have.
- **Zero-trust prompt handling**
  - Validated current state: Filesystem access is hardened, but prompt construction is still inline.
  - Hardening direction: Separate privileged instructions from user-controlled and indexed context, and add hostile-input tests.
  - Bucket: Must-have.
- **Dependency injection**
  - Validated current state: `NavigatorDeps` exists and is intentionally narrow.
  - Hardening direction: Preserve narrow request-scoped deps and prevent config sprawl into the deps object.
  - Bucket: Must-have.
- **Backend-style testing**
  - Validated current state: Unit and integration tests already exist.
  - Hardening direction: Extend tests to cover startup validation, usage limits, prompt revisioning, and operator-facing failures under deterministic models.
  - Bucket: Must-have.
- **Prompt/version control**
  - Validated current state: No prompt asset version is surfaced today.
  - Hardening direction: Introduce governed, versioned prompt assets or an equivalent isolated prompt layer under source control.
  - Bucket: Must-have.
- **Deterministic quality gates**
  - Validated current state: The repo supports `just check`, but the package does not yet anchor its hardening around it.
  - Hardening direction: Make `just check course-navigator` the minimum hardening gate and preserve deterministic test defaults.
  - Bucket: Must-have.
- **Reproducible dev workflow**
  - Validated current state: Root and package `justfile`s already support startup and tests.
  - Hardening direction: Align package hardening with the repo's reproducible `just` workflow and document the expected package gate.
  - Bucket: Must-have.
- **Explicit contracts**
  - Validated current state: Output contracts already exist.
  - Hardening direction: Add an explicit runtime configuration contract and make prompt/runtime metadata more auditable.
  - Bucket: Must-have.
- **Observability**
  - Validated current state: Logfire is initialized in the CLI entrypoint.
  - Hardening direction: Add traceable runtime metadata and stronger operator diagnostics without requiring hosted telemetry to run locally.
  - Bucket: Must-have.
- **Config isolation**
  - Validated current state: Shared constants already isolate `LEARNING_ROOT` and model defaults.
  - Hardening direction: Keep configuration separate from request deps and validate runtime config before launching the agent.
  - Bucket: Must-have.
- **Fail-fast validation**
  - Validated current state: Missing provider keys already fail early, but other startup assumptions do not.
  - Hardening direction: Validate startup inputs, prompt inputs, and runtime controls before interactive execution begins.
  - Bucket: Must-have.
- **Modular/slim dependency strategy**
  - Validated current state: Package depends on broad `pydantic-ai` today.
  - Hardening direction: Evaluate `pydantic-ai-slim[...]` or equivalent footprint reduction only if it preserves required behavior and clarity.
  - Bucket: Deferred.

## Must-Have vs Deferred Hardening

### Must-Have First-Pass Hardening

- Explicit runtime configuration and startup validation.
- Enforced usage limits in the CLI execution path.
- Versioned or otherwise governed prompt assets with clear trust boundaries.
- Deterministic prompt assembly for indexed context.
- Production-style quality gate centered on `just check course-navigator`.
- Extended tests for non-happy-path runtime behavior.
- Operator-facing observability metadata and failure diagnostics.

### Deferred or Optional Hardening

- Evaluating a move to `pydantic-ai-slim[...]` or other slimmer install options.
- Multi-provider fallback chains or circuit-breaker behavior beyond current usage limits.
- Immutable replay artifacts, cryptographic evidence trails, or WORM-oriented audit export.
- Dynamic RBAC or end-user-scoped tool permissions.
- Parser-agent or multi-stage content sanitization architectures.
- Expanding the UI placeholder into a real application surface.
- Formal evaluation harnesses beyond the current deterministic test suite.

## Prioritized User Stories

### Story 1: Formalize Runtime Contracts and Startup Boundaries (Priority: P1) 🎯 MVP

As a maintainer, I want runtime configuration, provider selection, startup defaults, and injected dependencies separated into explicit contracts so that Course Navigator starts deterministically, remains model-agnostic, and fails fast when misconfigured.

**Why this priority**: The package already has a shared resolver and request-scoped deps, but startup behavior still depends on implicit defaults and does not fully expose runtime controls.

**Independent Test**: Starting Course Navigator with valid runtime inputs resolves one provider/model path and launches successfully; invalid or incomplete runtime inputs stop before the interactive CLI starts and return actionable diagnostics.

**Acceptance Criteria:**

- [ ] The package defines one explicit runtime configuration contract for provider/model identifier, usage limits, observability behavior, and user-facing defaults.
- [ ] `NavigatorDeps` remains request-scoped personalization data and is not expanded into a catch-all configuration object.
- [ ] CLI startup consumes validated runtime configuration instead of relying on hard-coded user defaults inside the entrypoint.
- [ ] Model/provider resolution remains abstracted behind the shared resolver boundary and is surfaced clearly in package tests and operator diagnostics.
- [ ] Invalid or incomplete runtime configuration fails before interactive execution begins.
- [ ] The interactive runtime path applies validated usage limits rather than leaving request and tool limits implicit.

**Role-Based Feedback Reports:**

**Persona:** Sarah Jenkins (`learning/00-misc/learner-personas/enterprise-architect.persona.md`)

- **Stance:** Approve
- **Critical Risks:** If runtime configuration remains implicit, the package will still read like a teaching demo instead of an enterprise component with defined startup contracts.
- **Recommendations:** Make startup inputs explicit, keep provider abstraction centralized, and prevent request-scoped dependencies from becoming an ungoverned config bag.
- **Confidence:** 93%
- **Follow-Up Questions:** Should usage-limit values live entirely in validated runtime configuration, or may implementation still allow safe defaults with explicit documentation?
- **Reflection:** This story is the right foundation because it improves operational clarity without expanding product scope. The key is to treat startup as a contract boundary, not just a convenience wrapper.

**Persona:** David Chen (`learning/00-misc/learner-personas/ai-engineer.persona.md`)

- **Stance:** Approve
- **Critical Risks:** Hard-coded defaults and implicit startup behavior make it harder to prove what configuration produced a given run and weaken auditability.
- **Recommendations:** Fail fast on invalid runtime inputs, record resolved runtime metadata, and keep configuration separate from user-influenced dependency objects.
- **Confidence:** 95%
- **Follow-Up Questions:** Should the hardening pass require deterministic stop behavior when validation fails repeatedly during startup or prompt preparation?
- **Reflection:** This story aligns with compliance-first expectations because it makes the package easier to reason about before the model is ever invoked. The strongest gain is removing ambiguity from runtime state.

**Reconciliation Summary:** Sarah and David both support explicit startup contracts. Their shared concern is ambiguous runtime state, so the acceptance criteria now require validated configuration, preserved dependency boundaries, and explicit usage-limit handling.

### Story 2: Govern Prompt Assets and Trust Boundaries (Priority: P1) 🎯 MVP

As a maintainer, I want system instructions, indexed lesson context, and user-controlled values separated into explicit trust zones so that prompt behavior is reviewable, versioned, and harder to subvert accidentally.

**Why this priority**: The package already hardens file access, but prompt governance is still weaker than the filesystem posture around it.

**Independent Test**: Reviewers can identify the privileged prompt artifact or isolated prompt layer, verify a surfaced prompt revision, and run tests that reject attempts to smuggle instructions through personalization fields or indexed content.

**Acceptance Criteria:**

- [ ] Privileged system instructions are stored as versioned package assets or an equivalently isolated prompt layer under source control rather than being governed only through inline string concatenation.
- [ ] Prompt assembly keeps privileged instructions separate from user-controlled values and indexed lesson metadata.
- [ ] Indexed context is formatted deterministically with stable ordering and bounded structure before it enters prompt context.
- [ ] The package preserves allowlist-based lesson access and extends tests to cover hostile personalization strings and hostile retrieved-content scenarios.
- [ ] Prompt revision or version metadata is surfaced in documentation, tests, or runtime diagnostics so instruction changes are auditable.
- [ ] This hardening pass does not expand tool access beyond indexed lesson files.

**Role-Based Feedback Reports:**

**Persona:** Sarah Jenkins (`learning/00-misc/learner-personas/enterprise-architect.persona.md`)

- **Stance:** Approve
- **Critical Risks:** Inline prompt assembly makes the most privileged instructions harder to review, evolve, and secure than the rest of the package architecture.
- **Recommendations:** Treat prompts as first-class package assets, make trust boundaries visible in the implementation, and preserve strict tool scoping.
- **Confidence:** 91%
- **Follow-Up Questions:** Should the first pass stop at prompt asset governance and tests, or also include stronger fallback behavior when prompt validation fails?
- **Reflection:** This story brings prompt handling closer to the same engineering discipline already applied to models, tools, and contracts. That is a necessary step for production credibility.

**Persona:** David Chen (`learning/00-misc/learner-personas/ai-engineer.persona.md`)

- **Stance:** Approve
- **Critical Risks:** Without explicit trust zones, user-controlled content or retrieved metadata can influence privileged instructions in ways that are difficult to detect after the fact.
- **Recommendations:** Preserve the filesystem allowlist posture, add adversarial tests for prompt assembly, and surface prompt revision metadata for later audit and replay use cases.
- **Confidence:** 96%
- **Follow-Up Questions:** Should the prompt layer include explicit sanitization or serialization rules for indexed metadata in the first pass, or is deterministic bounded formatting sufficient?
- **Reflection:** The package already shows good zero-trust thinking at the tool layer. This story extends that discipline into the prompt layer, which is where many real failures begin.

**Reconciliation Summary:** Sarah and David agree that prompt governance is the most important missing hardening layer. The story now requires governed prompt assets, deterministic context formatting, and adversarial tests without expanding package scope.

### Story 3: Enforce Backend-Style Validation and Quality Gates (Priority: P1) 🎯 MVP

As a maintainer, I want Course Navigator validated like a backend application so that runtime regressions, contract drift, and non-happy-path failures are caught deterministically before release.

**Why this priority**: The package already has meaningful tests, but the hardening target is not yet defined around startup validation, prompt revisioning, runtime limits, and operator-facing error behavior.

**Independent Test**: `just check course-navigator` passes with deterministic tests covering startup validation failures, prompt governance behavior, usage-limit enforcement, and CLI/operator diagnostics without requiring live provider calls.

**Acceptance Criteria:**

- [ ] The package defines `just check course-navigator` as the minimum hardening gate for future implementation work.
- [ ] Tests cover startup validation failures, prompt revision behavior, usage-limit handling, and operator-facing error paths in addition to the current happy-path coverage.
- [ ] Deterministic models or mocks remain the default for package tests, and real provider requests remain explicitly opt-in.
- [ ] Fail-fast validation stops launch when required configuration, prompt inputs, or index assumptions are invalid.
- [ ] Existing path-security and index-building tests are preserved and extended rather than replaced.
- [ ] Package documentation explains the reproducible validation workflow expected for this package.

**Role-Based Feedback Reports:**

**Persona:** Sarah Jenkins (`learning/00-misc/learner-personas/enterprise-architect.persona.md`)

- **Stance:** Approve
- **Critical Risks:** A package can appear well tested while still missing the operational checks that matter most in production, especially startup and degraded-path behavior.
- **Recommendations:** Define one clear package quality gate, keep tests deterministic, and treat startup failures as first-class scenarios rather than incidental edge cases.
- **Confidence:** 92%
- **Follow-Up Questions:** Should the hardening pass require package-level documentation of test categories and expected local commands, or is the root workflow reference sufficient?
- **Reflection:** This story raises the package from "tested enough for a lesson" to "validated enough for disciplined iteration." The emphasis on repeatability is especially important.

**Persona:** David Chen (`learning/00-misc/learner-personas/ai-engineer.persona.md`)

- **Stance:** Approve
- **Critical Risks:** If failure paths and runtime limits are not tested deterministically, teams may rely on provider behavior or manual observation instead of enforceable controls.
- **Recommendations:** Keep real model calls opt-in, assert stop conditions explicitly, and verify that operator-visible failures are distinct and actionable.
- **Confidence:** 94%
- **Follow-Up Questions:** Should the first pass explicitly require tests for repeated validation failure stop conditions, or reserve that for later circuit-breaker work?
- **Reflection:** This story is consistent with compliance and safety expectations because it treats determinism as a control, not just a test convenience. It also avoids overcommitting to advanced resilience features too early.

**Reconciliation Summary:** Sarah and David both prioritize repeatable quality gates and deterministic failure handling. The story therefore centers on `just check course-navigator`, preserved deterministic tests, and explicit fail-fast scenarios instead of advanced fallback mechanisms.

### Story 4: Improve Observability and Operator Diagnostics (Priority: P2)

As an operator, I want each Course Navigator run to expose enough runtime metadata to understand which configuration, prompt revision, and lesson references produced an answer so that debugging and reviews are practical.

**Why this priority**: Logfire is already initialized, so the next step is to make runtime evidence more useful without forcing heavy infrastructure.

**Independent Test**: A maintainer can run the package locally and identify the resolved model/provider, prompt revision, configured limits, and referenced lesson paths from logs, traces, or CLI diagnostics without exposing secrets.

**Acceptance Criteria:**

- [ ] Runtime diagnostics expose resolved provider/model identity, prompt revision, usage-limit settings, and referenced lesson paths or counts without leaking secrets.
- [ ] Startup or index-building diagnostics identify malformed, skipped, or unindexed learning-material conditions clearly enough for local debugging.
- [ ] Operator-facing failures distinguish configuration errors, validation failures, and tool-access violations.
- [ ] Observability remains compatible with the current Logfire bootstrap and local development workflow.

### Story 5: Capture Optional Footprint and Advanced Hardening Work (Priority: P3)

As a maintainer, I want advanced hardening and footprint-reduction ideas recorded explicitly so that future improvements are visible without inflating the first implementation pass.

**Why this priority**: Several worthwhile hardening directions exist, but they should remain deferred until the first pass is complete and validated.

**Independent Test**: Reviewers can identify which advanced ideas were intentionally deferred and why they were not required for the first hardening pass.

**Acceptance Criteria:**

- [ ] The spec records a dependency-footprint review, including whether `pydantic-ai-slim[...]` is a viable later option, without requiring that migration in the first pass.
- [ ] The spec records deferred advanced patterns, including circuit breakers, provider fallback chains, audit-grade replay artifacts, dynamic tool authorization, parser-agent sanitization, UI expansion, and evaluation harnesses.
- [ ] Deferred items are clearly marked as non-blocking for the first implementation pass.

## Functional Requirements

1. Course Navigator hardening MUST preserve the existing single-agent and local lesson-navigation architecture.
2. The package MUST introduce an explicit runtime configuration boundary for provider/model selection, usage limits, observability behavior, and startup defaults.
3. `NavigatorDeps` MUST remain request-scoped dependency data and MUST NOT become the general-purpose package configuration container.
4. Provider/model selection MUST remain abstracted behind shared resolver logic and MUST be surfaced in package-level diagnostics or tests.
5. The interactive runtime path MUST enforce validated usage limits.
6. Privileged system instructions MUST be versioned or isolated under a governed prompt layer that is reviewable in source control.
7. Prompt assembly MUST preserve explicit trust boundaries between privileged instructions, user-controlled values, and indexed lesson metadata.
8. Indexed lesson context MUST be formatted deterministically before entering prompt context.
9. The package MUST preserve allowlist-based lesson access and extend tests to cover prompt/context adversarial scenarios.
10. The package MUST define a reproducible minimum validation gate centered on `just check course-navigator`.
11. The package MUST fail fast on invalid startup configuration, invalid prompt preparation, or invalid index/runtime assumptions.
12. Observability and diagnostics MUST expose enough metadata to support local debugging and review without requiring live hosted telemetry or leaking secrets.
13. Dependency-footprint optimization and advanced resilience patterns MAY be implemented later, but they MUST remain explicitly deferred from the first hardening pass unless later discovery proves them necessary.

## Technical Specification

### Architecture to Preserve

- A single agent factory in `agent.py`.
- Request-scoped dependency injection via `NavigatorDeps`.
- Shared runtime boundaries from `pydantic_ai_shared`, including `LEARNING_ROOT` and `resolve_model()`.
- Lesson indexing in `utils.py` and allowlist-based content access in `tools.py`.
- CLI-driven startup in `main.py` with local-first development ergonomics.

### Hardening Strategy

#### Phase 0: Runtime Contract Foundation

- Introduce a typed startup/runtime configuration boundary for the package.
- Preserve the shared resolver boundary while making resolved runtime state observable.
- Apply validated usage limits in the CLI path.

#### Phase 1: Prompt Governance and Trust Boundaries

- Isolate privileged instructions into a governed prompt layer.
- Keep indexed context and user-controlled fields outside privileged instruction text.
- Make prompt revisioning visible in tests and diagnostics.

#### Phase 2: Deterministic Validation and Operator Visibility

- Expand package tests around startup, validation, usage limits, and operator-facing failures.
- Make `just check course-navigator` the minimum expected package validation path.
- Enrich local diagnostics and Logfire-facing metadata.

#### Phase 3: Deferred Hardening Backlog

- Revisit dependency footprint reduction.
- Revisit advanced resilience and audit patterns only after the first pass is stable.

## Implementation Plan

- [ ] Phase 0: Foundational runtime contract work
- [ ] CHECKPOINT: Startup configuration and usage-limit contract validated independently
- [ ] Phase 1: Story 1 (P1) runtime contracts
- [ ] CHECKPOINT: Runtime startup path independently testable
- [ ] Phase 2: Story 2 (P1) prompt governance
- [ ] CHECKPOINT: Prompt trust boundaries independently testable
- [ ] Phase 3: Story 3 (P1) deterministic quality gate
- [ ] CHECKPOINT: `just check course-navigator` passes with extended deterministic coverage
- [ ] Phase 4: Story 4 (P2) observability and diagnostics
- [ ] CHECKPOINT: Local runtime metadata is reviewable without hosted telemetry
- [ ] Phase 5: Story 5 (P3) deferred backlog review

## Task Breakdown

- [ ] T001 [P] [US1] Refine startup and runtime configuration boundaries in `packages/course-navigator/src/course_navigator/main.py` and related package runtime surfaces.
- [ ] T002 [P] [US1] Extend package tests to validate provider/model resolution visibility, startup failure behavior, and usage-limit enforcement.
- [ ] T003 [US2] Introduce a governed prompt layer within `packages/course-navigator/src/course_navigator/` and remove exclusive reliance on inline prompt concatenation.
- [ ] T004 [P] [US2] Extend `packages/course-navigator/tests/test_agent.py` and related tests with adversarial prompt/context cases and prompt-revision assertions.
- [ ] T005 [P] [US3] Update package documentation in `packages/course-navigator/README.md` to define the reproducible validation workflow and hardening expectations.
- [ ] T006 [US3] Extend deterministic integration and CLI tests for fail-fast validation, operator-facing errors, and preserved no-real-model defaults.
- [ ] T007 [P] [US4] Enrich runtime diagnostics and observability metadata in the CLI and agent path without exposing secrets.
- [ ] T008 [US4] Add tests for diagnostic behavior around malformed index entries, configuration failures, and tool-access violations.
- [ ] T009 [P] [US5] Review package dependency footprint in `packages/course-navigator/pyproject.toml` and document whether slimmer install options are viable.
- [ ] T010 [US5] Record deferred advanced hardening items in implementation notes so they remain visible but non-blocking.

## Testing Strategy

### Story-Level Validation

- **US1**: Add deterministic unit and CLI-path tests for the runtime configuration contract, including provider/model resolution visibility, validated usage-limit application, fail-fast startup behavior on invalid configuration, and preservation of `NavigatorDeps` as request-scoped dependency data rather than general package config.
- **US2**: Add deterministic prompt-governance tests that verify privileged instructions remain isolated from user-controlled values and indexed lesson context, prompt revision metadata is surfaced for auditability, and hostile personalization or retrieved-content fixtures cannot silently reshape the governed instruction layer.
- **US3**: Extend deterministic validation coverage so `just check course-navigator` exercises startup validation failures, prompt preparation failures, usage-limit handling, preserved path-security/index behavior, and operator-facing CLI/runtime error paths without requiring live provider calls.
- **US4**: Add observability assertions where practical to verify that runtime diagnostics distinguish configuration errors, validation failures, and tool-access violations while exposing resolved provider/model identity, prompt revision, usage-limit settings, and referenced lesson paths or counts without leaking secrets.
- **US5**: Validate deferred work at the specification and documentation level only, confirming footprint-review and advanced-hardening items remain explicitly recorded, package-scoped, and non-blocking for the first implementation pass.

### Deterministic Test Patterns

- Package tests must keep deterministic fakes, mocks, or fixed fixtures as the default execution mode, with real provider requests remaining explicitly opt-in.
- Prompt-boundary tests should use stable hostile-input fixtures and bounded indexed-context fixtures so regressions are attributable to package behavior rather than provider variability.
- CLI and runtime validation tests should assert stop conditions before interactive execution begins when configuration, prompt inputs, or index assumptions are invalid.
- Existing filesystem allowlist and lesson-index tests should be preserved and extended rather than replaced so current hardening guarantees remain intact.

### Quality-Gate Expectations

- `just check course-navigator` is the minimum package hardening gate and must cover formatting, linting, type checking, and the deterministic test suite.
- Package documentation must describe the reproducible validation workflow expected for the hardened package, including the default no-live-provider test posture.
- Observability assertions should remain local-first and testable without requiring hosted telemetry, while still confirming that operator-facing diagnostics are actionable.

## Risks and Guardrails

- Hardening must not turn Course Navigator into a different product. The package should remain a narrow, local, single-agent reference package.
- Prompt governance should improve auditability and safety without making the package harder to understand than necessary.
- Observability work should remain useful in local development and must not require a paid or hosted service to preserve basic developer ergonomics.
- Dependency-footprint optimization should only proceed if it is validated to preserve required features and clarity.

## Validation Checklist

- [x] Problem statement is clear and compelling
- [x] Success criteria are measurable and specific
- [x] All user stories have testable acceptance criteria
- [x] Stories are prioritized (P1, P2, P3)
- [x] Each P1 story is independently testable as MVP
- [x] Technical constraints and dependencies are documented
- [x] Out of scope items are explicitly listed
- [x] Implementation phases have clear checkpoints
- [x] Tasks have parallel markers [P] where applicable
- [x] No `NEEDS CLARIFICATION` markers remain
- [x] The spec is grounded in validated package state rather than assumed future architecture
- [x] Immediate hardening items are separated from deferred work
