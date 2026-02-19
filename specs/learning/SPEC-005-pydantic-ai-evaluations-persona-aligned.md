---
spec-id: SPEC-005
title: Evaluation First as AI system Development Driver - Learning Module
spec-type: learning
status: ready
created: 2026-02-15
owner: learning-ops
---

## Specification Progress

- [x] Complete discovery phase
- [x] Determine specification type
- [x] Draft specification from template
- [x] Validate against quality standards
- [x] Finalize specification

## Discovery Notes

- The target audience is primarily Sarah Jenkins (Enterprise AI Architect), with secondary needs from David Chen (Compliance-First AI Engineer) and Marcus Thorne (AI Product Strategist).
- Existing learning materials mention evaluations but do not provide a short, practical, start-to-end path for learning and applying them.
- The highest-value gap is a local, on-demand workflow that produces a scorecard and explains failures with traceable evidence.
- Module boundaries were previously ambiguous; this specification now defines strict topic ownership across core and advanced learning modules.

## Executive Summary

### Problem Statement

The current learning path references evaluations, but the scope became too implementation-heavy and too broad for this module.

This created three issues:

1. **Learning friction**: the start and end points are too far apart for an introductory module.
2. **Delivery ambiguity**: CI/CD, continuous operations, and governance automation obscure core learning outcomes.
3. **Debuggability gap**: learners need clear, traceable failure analysis before advanced operationalization.

### Proposed Solution

Refocus this module to a learning-first progression with short distance between start and finish:

- **Lesson 1 (core concepts):** why evaluations + observability are foundational for reliable AI systems.
- **Lesson 2 (implementation):** run one local, on-demand evaluation pipeline that outputs a scorecard.
- **Lesson 3 (analysis):** troubleshoot failures using audit fields, reason codes, and evidence links.

CI/CD integration and continuous evaluation operations are explicitly deferred to a standalone future module.

### Success Criteria

- The module is scoped to progressive learning stories with clear start and end points.
- A local, on-demand evaluation pipeline is defined and produces a single scorecard output.
- Scorecard and run artifacts are auditable and traceable for troubleshooting.
- Decision output uses a clear recommendation: `proceed`, `hold`, or `escalate`.
- No unresolved `NEEDS CLARIFICATION` markers remain.

## Scope

### In Scope

- Learning content specification for `pydantic-evals` fundamentals and practical usage.
- A local, on-demand evaluation workflow with one scorecard output.
- Auditability and traceability guidance for failure troubleshooting.
- Progressive lesson design: core concepts, then local implementation, then analysis.
- Explicit module-boundary definition so topic ownership is unambiguous.

### Out of Scope

- CI/CD integration, merge gates, and GitHub Actions workflows.
- Continuous/scheduled evaluation operations (pre-merge, nightly, pre-release cadence).
- Incident automation, SIEM integrations, and compliance sign-off workflows.
- Full analytics dashboard implementation.

## Learning Architecture

This specification no longer depends on the previous numbered module drafts. The learning structure is redefined as follows:

1. **Reliable AI Foundations**
   - Core concepts, including evaluations and observability basics.
   - Terminology and minimum reliability mental model.

2. **Evaluation and Observability** (this spec)
   - Local, on-demand evaluation workflow.
   - Scorecard generation, auditability, and failure troubleshooting.

3. **Advanced Reliability Patterns** (future modules)
   - Context management patterns.
   - Retrieval patterns (RAG) and evaluation interactions.
   - Scaling concerns (performance, cost, reliability under load).
   - CI/CD and continuous evaluation operations.

Boundary rule: if a topic requires scheduled automation, production orchestration, or large-scale systems optimization, it belongs to **Advanced Reliability Patterns**, not this module.

## Prioritized User Stories

### Story 1: Foundations Lesson — Why Evaluations Matter (Priority: P1) 🎯 MVP

As Sarah (Enterprise AI Architect), I want a concise conceptual lesson on evaluations and monitoring/observation so that I understand why they are required to build reliable AI systems.

**Why this priority**: This establishes the minimum mental model before any implementation work.

**Independent Test**: A learner can explain evaluation layers, observability purpose, and decision semantics (`proceed`/`hold`/`escalate`) without running code.

**Acceptance Criteria:**

- [ ] Defines core concepts: `Dataset`, `Case`, deterministic checks, qualitative checks, operational metrics, and observability.
- [ ] Explains the reliability principle: without evaluations and observability, AI quality cannot be trusted or improved safely.
- [ ] Introduces a minimal decision model (`proceed`, `hold`, `escalate`) and when each is used.
- [ ] Uses persona-aligned examples (architecture, compliance, product perspectives) without advanced operational automation.
- [ ] Explains how evaluations and observability drive development and product decisions, even in early stages. How they reduce risk and increase confidence. How they can be used in unexpected ways(model and host pivoting, driving prompt decomposition, balancing safety with usability).
- [ ] Explicitly distinguishes this module from advanced topics (context management, RAG, scaling), which are deferred.

### Story 2: Implementation Lesson — Local On-Demand Scorecard (Priority: P1) 🎯 MVP

As David (Compliance-First AI Engineer), I want a local evaluation pipeline that runs on demand and produces an auditable scorecard so that I can evaluate quality and debug failures early.

**Why this priority**: This is the practical core of the module and the bridge from theory to development usage.

**Independent Test**: A learner runs one local evaluation flow and receives a scorecard plus a traceable run record with clear failure reasons.

**Acceptance Criteria:**

- [ ] Defines one local pipeline flow: load dataset cases, execute evaluator stack, compute scorecard, output recommendation.
- [ ] Scorecard MUST use the standard `pydantic_evals.reporting.EvaluationReport`. Use `.render()` or `.print()` for human-readable console output.
- [ ] Every run captures reproducibility metadata: `run_id`, `timestamp`, `dataset_version`, `prompt_version`, `model_version`, `evaluator_version`, `executor_id`.
- [ ] Every failed check includes `reason_code`, human-readable `explanation`, and `evidence_ids` (mapped to `EvaluationResult` metadata or report attributes).
- [ ] Output includes a single recommendation: `proceed`, `hold`, or `escalate`, with a brief `decision_justification`.
- [ ] Uses a minimal 'Core 3' evaluator set for the walkthrough: `Contains` (deterministic), `HasMatchingSpan` (behavioral contract), and `LLMJudge` (qualitative), explaining why this mix covers the basics.
- [ ] Demonstrates a fail-fast execution ordering: deterministic/format checks → span/behavioral checks → LLM/judge evaluations (cheapest → most expensive).
- [ ] Include one serialized dataset example (YAML) and one example `EvaluationReport` JSON artifact (serialized via `TypeAdapter`) for learners to inspect.
- [ ] Introduces prompt injection sample by setting a username that instructs the course navigator agent to swear, demonstrating how a simple adversarial input can cause a deterministic check to fail and how that failure is captured in the scorecard and run metadata.
- [ ] Demonstrates partial handling of [OWASP Top 10 LLM Risks](../learning/00-misc/owasp-llm-top-10.md) in the context of the evaluation flow, such as how to detect and report prompt injection attempts or data poisoning indicators in the scorecard.

### Story 3: Observation Lesson — Failure Analysis and Next Actions (Priority: P2)

As Marcus (AI Product Strategist), I want a guided troubleshooting lesson from scorecard to root-cause clues so that evaluation outcomes can drive product and development decisions.

**Why this priority**: Teams need actionable interpretation of results after baseline evaluation flow is in place.

**Independent Test**: Given one failed run, a learner can identify likely failure source, associated risk, and immediate next action.

**Acceptance Criteria:**

- [ ] Defines a simple failure triage workflow from scorecard → failed assertion → evidence → remediation candidate.
- [ ] Distinguishes content-quality failures vs latency/cost failures vs policy/safety failures.
- [ ] Provides a compact recommendation template with next action and rollback trigger for local experimentation.

## Functional Requirements
1. The module MUST present a short, progressive learning path from core concepts → local implementation → troubleshooting, enabling a single end-to-end learner experience.
2. The module MUST teach `pydantic-evals` foundations (`Dataset`, `Case`, evaluator composition), using enterprise-aligned examples for architecture, compliance, and product perspectives.
3. The module MUST define one local, on-demand evaluation workflow that produces a canonical scorecard using `pydantic_evals.reporting.EvaluationReport` (serialized via `pydantic.TypeAdapter`) and human-readable output via `.render()`/`.print()`.
4. Each local run MUST produce an auditable `evaluation_record` containing at minimum: `run_id`, `timestamp`, `executor_id`, `dataset_version`, `prompt_version`, `model_version`, `evaluator_version`, `report` (the `EvaluationReport`), and `evidence_ids`.
5. Each failed check MUST include structured failure metadata: `reason_code`, a human-readable `explanation`, and `evidence_ids` that map to `EvaluationResult` metadata or persisted artifact URIs/paths.
6. The module MUST capture observability trace fields for worked examples where applicable: `otel_trace_id`, `span_ids` (or map of check→span), optional `trace_url`, and optional `observability_ui_link` to aid interactive troubleshooting.
7. The module MUST prescribe a minimal "Core 3" evaluator set for the walkthrough: `Contains` (deterministic), `HasMatchingSpan` (behavioral/contract), and `LLMJudge` (qualitative), and MUST demonstrate a fail-fast execution ordering: deterministic/format checks → span/behavioral checks → LLMJudge evaluations.
8. The module MUST include at least one serialized example dataset artifact (YAML) with a generated JSON Schema and one example `EvaluationReport` JSON artifact for learners to inspect and reproduce.
9. The module MUST demonstrate detection and reporting of common LLM risks (example: prompt injection) in the scorecard and run metadata, mapping such detections to reason codes and evidence links tied to the worked example.
10. The module MUST produce a single decision output per run: `proceed`, `hold`, or `escalate`, and include a concise `decision_justification` in the `evaluation_record`.
11. CI/CD integration, scheduled/continuous evaluation operations, merge-gates, and other production orchestration concerns MUST be explicitly deferred to a standalone follow-up module; this module focuses on local/on-demand evaluation and observation.
12. The specification MUST define unambiguous ownership boundaries: core topics (evaluations, auditability, observability, failure triage) belong to this module; advanced topics (context management, RAG interactions, scaling, CI/CD, incident automation) belong to the advanced module.

## Technical Specification

### Content Targets

Canonical learning content for this module will be authored under `learning/02-beyond-prototype/`.
Module entry point file: `learning/02-beyond-prototype/README.md`.
Lesson files (minimum):

- `learning/02-beyond-prototype/01-why-evals-and-observability.md`
- `learning/02-beyond-prototype/02-local-scorecard-pipeline.md`
- `learning/02-beyond-prototype/03-failure-triage-and-observation.md`
Top-level learning index updates will link to this module via `learning/README.md` and `learning/CONCEPTS.md`.
- Optional reference snippets from:
  - `packages/course-navigator/`
  - `packages/shared/`

Pydantic Evals overview: this module uses the code-first `pydantic-evals` model as the canonical tooling vocabulary — Dataset (test suite) → Case (test scenario) → Experiment (execution) → EvaluationReport (result). Lessons should reference example artifacts from `packages/shared` and, where helpful, `packages/course-navigator` for runnable snippets. Include one minimal example dataset (YAML + generated JSON Schema) and one example `EvaluationReport` JSON in the lesson materials.

This target structure is authoritative for this specification and supersedes prior draft layout assumptions.

### Canonical Local Evaluation Flow

1. **Prepare input**: choose dataset and case set for a local run.
2. **Run evaluators**: deterministic + qualitative + operational checks.
3. **Produce scorecard**: generate `pydantic_evals.reporting.EvaluationReport` containing test results and summary metrics.
4. **Record trace**: persist run metadata + failure reasons + evidence links. Serialize the report to JSON using `pydantic.TypeAdapter`.
5. **Recommend action**: `proceed`, `hold`, or `escalate` with justification.

### Audit and Trace Record (Conceptual)

Each local run MUST produce an `evaluation_record` concept containing at least:

- `run_id`, `timestamp`, `executor_id`
- `dataset_version`, `prompt_version`, `model_version`, `evaluator_version`
- `report` (the standard `pydantic_evals` EvaluationReport)
- `evidence_ids` (case ID + output snippet URI/path)
- `decision` and `decision_justification`

Additional observability & span fields (required for worked examples and traceability):

- `otel_trace_id`: top-level OpenTelemetry trace id for the run (string)
- `span_ids`: array of span ids (or map of logical check -> span id) used as evidence for behavioral checks
- `trace_url`: optional link to a hosted trace viewer or recorded trace artifact
- `observability_ui_link`: optional link to the Pydantic Logfire or Log/Trace dashboard that visualizes the run
- `behavioral_contract_checks`: structured list of checks that verify internal execution paths (id, pass/fail, span_evidence_id)

Evidence and artifacts guidance:

- Each failed behavior or contract check MUST include `span_ids` and, where possible, a `trace_url` to support interactive investigation.
- Store snippets referenced by `evidence_ids` as small JSON or text artifacts with stable URIs/paths so learners can inspect model outputs used as evidence.

### Learning Boundaries

- This module focuses on local/on-demand evaluation and observation.
- CI/CD policies, merge blocking, scheduled runs, and incident workflows are deferred to a standalone module.
- Context management patterns, RAG concerns, and scaling concerns are deferred to the advanced module.

### Best Practices (Pydantic Evals)

- **Evaluation-Driven Development:** Define evaluation criteria before coding. Ship small, measurable checks early.
- **Fail-Fast Hierarchy:** Run cheap deterministic checks first (format, schema), then span/behavioral checks, and run LLM-judge evaluations last.
- **Case-Specific Evaluators:** Attach tailored evaluators to cases to capture scenario-specific correctness (golden datasets).
- **Verify Behavioral Contracts:** Use span-based checks (HasMatchingSpan) to ensure internal steps (retrievals, tool calls) occurred as expected.
- **LLM Judge Determinism:** When using `LLMJudge`, fix temperature to 0 and supply a clear rubric. Use a fast/cheap model (e.g. `gpt-4o-mini`) for the lesson.
- **Serialization & IDE Support:** Provide datasets as YAML/JSON with generated JSON Schema for IDE autocomplete and validation.
- **Versioning & Separation:** Keep prompts, datasets, and evaluators versioned separately from application code to enable reproducible comparisons.
- **Evaluator Reliability Checks:** Periodically re-run evaluators (or use bootstrap methods) to validate evaluator stability and statistical significance.

## Implementation Plan

### Phase 0: Foundations (Blocking)

- Finalize module boundaries and defer advanced operations scope.
- Define lesson progression and glossary.
- Define scorecard minimum KPI vocabulary and decision semantics.
- Confirm canonical destination path: `learning/02-beyond-prototype/`.

**CHECKPOINT:** Scope and progression approved before drafting lessons.

### Phase 1: P1 Story — Concepts Lesson

- Implement Story 1 (foundational concepts and reliability framing).
- Validate concept clarity and persona alignment.

**CHECKPOINT:** Learner can articulate why evaluations + monitoring are mandatory for reliable AI systems.

### Phase 2: P1 Story — Local On-Demand Implementation Lesson

- Implement Story 2 (single local pipeline and scorecard output).
- Validate auditability and traceability fields in lesson artifacts.

**CHECKPOINT:** Learner can run and interpret one local scorecard end to end.

### Phase 3: P2 Story — Observation and Troubleshooting Lesson

- Implement Story 3 (failure triage and next actions).
- Validate that one failed example can be diagnosed using recorded evidence.

**CHECKPOINT:** Learner can troubleshoot a failed evaluation with traceable artifacts.

### Phase 4: Final QA + Docs Sync

- Run `just learning-validate`.
- Update module linkages in learning indexes.
- Add deferred-scope pointer to the future CI/CD + continuous operations module.

## Task Breakdown

- [ ] T001 [P] [FOUNDATION] Define module scope boundaries and explicit defer list (CI/CD, continuous operations).
- [ ] T002 [P] [FOUNDATION] Define evaluation glossary and lesson progression map.
- [ ] T003 [FOUNDATION] Reference `pydantic_evals.reporting` for scorecard format.
- [ ] T016 [FOUNDATION] Define strict ownership split for core (evaluations/observability) vs advanced (context management, RAG, scaling).

- [ ] T004 [P] [US1] Draft concepts lesson for evaluation layers and monitoring/observation rationale.
- [ ] T005 [P] [US1] Add persona-aligned examples for architecture, compliance, and product concerns.
- [ ] T006 [US1] Add concise concept checkpoint prompts for learner self-validation.

- [ ] T007 [P] [US2] Draft local on-demand pipeline walkthrough.
- [ ] T008 [P] [US2] Define auditable run record fields and `pydantic_evals` report link.
- [ ] T009 [US2] Draft scorecard interpretation guide with `proceed`/`hold`/`escalate` outcomes.

- [ ] T010 [P] [US3] Draft failure triage playbook (scorecard → evidence → remediation).
- [ ] T011 [P] [US3] Add one worked failure example with traceable evidence links.
- [ ] T012 [US3] Add compact release recommendation template for local experimentation decisions.

- [ ] T013 [FINAL] Update `learning/CONCEPTS.md` and module index links.
- [ ] T014 [FINAL] Execute `just learning-validate` and resolve documentation issues.
- [ ] T015 [FINAL] Mark specification handoff notes and deferred-module follow-up pointers.
- [ ] T017 [US2] Create example dataset artifact (YAML) and generated JSON Schema for the lesson.
- [ ] T018 [US2] Produce one example `pydantic_evals.reporting.EvaluationReport` JSON for the lesson.

## Testing Strategy

### Story-Level Validation

- **US1**: Validate conceptual understanding via checklist prompts (evaluation layers, monitoring role, decision semantics).
- **US2**: Validate local run output produces a standard `pydantic_evals.reporting` object + required audit/trace fields.
- **US2**: Validate local run output includes `EvaluationReport` + `behavioral_contract_checks`, `evidence_ids`, and that the walkthrough used the documented evaluator mix (deterministic, span, LLMJudge). Ensure `trace_url`/`otel_trace_id` or `observability_ui_link` are present in worked examples.
- **US3**: Validate a failed run can be triaged to likely cause and a concrete next action.

### Quality Gates

- Documentation structure checks via `just learning-validate`.
- Manual review: persona alignment checklist (Sarah, David, Marcus).

## Risks and Mitigations

- **Risk:** Scope becomes too light to guide real development.
  - **Mitigation:** Keep one complete local pipeline walkthrough with concrete scorecard and failure analysis.
- **Risk:** Learners infer local success equals production readiness.
  - **Mitigation:** Add explicit deferred-scope section listing production controls handled in the next module.
- **Risk:** Monitoring is treated as optional.
  - **Mitigation:** Make observation/audit fields mandatory in acceptance criteria and worked examples.

## Open Questions

- (Resolved) Canonical scorecard format: Use `pydantic_evals.reporting`.
- (Resolved) Minimum evaluator set: Use Core 3 (`Contains`, `HasMatchingSpan`, `LLMJudge`).
- (Resolved) Future module title: `learning/03-operational-reliability/`.
- (Resolved) LLM Judge defaults: Enforce `temperature=0` and fast model.
- (Resolved) Decision Logic: Left abstract/to-author for now.

## References

- `learning/00-misc/learner-personas/enterprise-architect.persona.md`
- `learning/00-misc/learner-personas/ai-engineer.persona.md`
- `learning/00-misc/learner-personas/product-manager.persona.md`
- `learning/01-fundamentals/README.md` - previous module with core concepts and agent anatomy that this module builds on.
- `learning/CONCEPTS.md`
- `specs/README.md`
- Reference: `learning/00-misc/ai-engineering-cheatsheet.md` — quick evaluation playbook and metric definitions.
