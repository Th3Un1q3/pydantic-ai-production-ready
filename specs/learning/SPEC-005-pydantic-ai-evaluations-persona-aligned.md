---
spec-id: SPEC-005
title: Persona-Aligned Pydantic AI Evaluations
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
- Existing learning materials mention evaluations but do not provide a full, persona-driven, production evaluation playbook.
- The most valuable gap is operational guidance: governance, failure handling, auditability, and ROI-aware evaluation loops.

## Executive Summary

### Problem Statement

The current learning path references evaluations in concept form but lacks a production-grade, persona-oriented specification for how teams should design, run, and operationalize `pydantic-evals` in real enterprise settings.

This gap causes three practical issues:

1. **Architectural uncertainty**: teams cannot confidently place evaluations in CI/CD and release gates.
2. **Compliance risk**: safety, prompt-injection resilience, and traceability checks are not standardized.
3. **Product ambiguity**: product teams lack a repeatable framework to tie evaluation metrics to UX trust, latency, and cost outcomes.

### Proposed Solution

Create a dedicated learning specification and supporting module content for **Pydantic AI Evaluations in Production**, centered on:

- `Dataset` / `Case` design patterns for enterprise scenarios.
- Focused evaluator design (custom evaluators + LLM-as-a-judge).
- Governance and safety evaluation layers (RBAC, prompt-injection, circuit-breaker readiness).
- Experiment reporting and release gates tied to business metrics.

### Success Criteria

- A complete persona-aligned evaluations module is specified with P1/P2/P3 user stories.
- Each story has independent, testable acceptance criteria.
- The spec includes explicit CI/CD evaluation gates and failure thresholds.
- The spec defines a repeatable experiment workflow with versioned prompts/tools/models.
- No unresolved `NEEDS CLARIFICATION` markers remain.

## Scope

### In Scope

- Learning content specification for evaluations in `pydantic-evals`.
- Design and operation of automated, LLM-judge, and human review evaluation paths.
- Safety/compliance-focused evaluation patterns and reporting expectations.
- Product-facing metrics translation (quality, latency, cost, trust).

### Out of Scope

- Implementing new runtime security infrastructure (e.g., WORM storage backend).
- Replacing existing package-level business logic.
- Building a full analytics dashboard UI.
- Provider-specific benchmark claims not reproducible inside this monorepo.

## Prioritized User Stories

### Story 1: Enterprise Evaluation Baseline (Priority: P1) 🎯 MVP

As Sarah (Enterprise AI Architect), I want a standardized evaluation architecture using `Dataset`, `Case`, and focused evaluators so that release decisions are auditable and repeatable.

**Why this priority**: This is the minimum architecture needed for production readiness.

**Independent Test**: A sample evaluation suite runs against a target agent and yields deterministic pass/fail release output with clear thresholds.

**Acceptance Criteria:**

- [ ] Defines canonical structure for evaluation datasets (happy path, edge case, adversarial case, policy case) and requires dataset artifacts to include a storage URI and a SHA256 checksum.
- [ ] Defines the baseline evaluator stack and measurement windows: deterministic checks (schema/assertions), qualitative checks (LLM‑judge with pinned rubric + config), and operational checks (latency p50/p95, token usage, estimated cost).
- [ ] Specifies release‑gate rules with explicit thresholds and decision logic (example): critical_assertions = 100% pass AND overall_quality_score ≥ 0.90 AND latency.p95_ms ≤ 500 → decision = proceed; otherwise → hold or escalate. Include a decision table in the learning docs.
- [ ] Requires reproducibility metadata for every experiment run: `model_version` (registry URI + digest), `prompt_version` (git SHA/tag), `dataset_version` (storage URI + SHA256), `tool_version`, and `evaluator_version`. A JSON Schema / Pydantic model MUST be provided under `packages/shared` for programmatic validation.

### Story 2: Governance and Hardening Evaluations (Priority: P1) 🎯 MVP

As David (Compliance-First AI Engineer), I want explicit safety and governance evaluation patterns so that unsafe or non-compliant agent behavior is detected before release.

**Why this priority**: Compliance failures are high-impact and must be part of MVP evaluation coverage.

**Independent Test**: A red‑team evaluation set demonstrates blocked unsafe outputs and records reasons in reports.

**Acceptance Criteria:**

- [ ] Defines evaluation cases for indirect prompt injection, privilege‑escalation attempts, policy violations, and validator failure loops; includes red‑team case artifacts and expected blocked/outcome behavior.
- [ ] Defines enforceable circuit‑breaker rules: trip when ≥ 3 consecutive runs fail any `critical` assertion OR failure rate > 5% over the last 10 runs; action = block merge + notify on‑call and create an incident.
- [ ] Requires reasoned failure outputs: each failed assertion MUST include `reason_code`, a human‑readable `explanation`, `evidence_ids` (case IDs + output snippet URIs), and `decision_justification`.
- [ ] Maps evaluator outputs to explicit escalation levels and policy controls; `critical` governance failures MUST fail CI automatically and require manual remediation and compliance sign‑off.

### Story 3: Product and ROI Evaluation Framework (Priority: P2)

As Marcus (AI Product Strategist), I want evaluation outputs mapped to user trust and ROI signals so that roadmap and release decisions reflect business outcomes.

**Why this priority**: Product teams need actionable decision inputs after technical quality is established.

**Independent Test**: Two prompt/tool variants are compared with a single report showing quality delta, latency delta, and estimated cost delta.

**Acceptance Criteria:**

- [ ] Defines minimum KPI set: quality score, latency percentile, token/cost estimate, fallback rate, and user-facing failure rate.
- [ ] Includes variant comparison protocol (A/B or ablation) with decision rubric — requires sample‑size calculation, 95% CI reporting, p‑value threshold (p < 0.05), clear primary vs guardrail metric definitions, and a machine‑readable `release_rubric` for decision automation.
- [ ] Defines “unhappy path UX” evaluation checks (clarity of fallback messaging, safe degradation behavior).
- [ ] Includes release recommendation format: proceed / hold / escalate.

#### Release recommendation — required template (one‑paragraph)

Release recommendation — `verdict` (proceed/hold/escalate): `<1‑line rationale>`; Primary metric `<name>` Δ=`<value>` (95% CI `<low>,<high>`, p=`<pvalue>`); Latency p95 Δ=`<ms>`; Cost Δ=`<% or $>`; Key risks: `<short list>`; Action: `<canary % / hold / rollback criteria>`. Attach experiment link and artifact URIs.

**Required fields**: `experiment_id`, `owner`, `primary_metric`, `delta_with_CI`, `cost_delta`, `latency_delta`, `decision`, `rollout_plan`, `rollback_triggers`.

### Story 4: Continuous Evaluation Operations (Priority: P3)

As a cross-functional AI team, we want recurring evaluation operations so that quality regressions are caught early and improvements are measurable over time.

**Why this priority**: Ongoing operations amplify value but depend on MVP architecture.

**Independent Test**: Scheduled evaluation run compares current results to prior baseline and flags regressions.

**Acceptance Criteria:**

- [ ] Defines run cadence (pre-merge, nightly, pre-release) and ownership.
- [ ] Defines regression policy (which deltas fail CI vs open follow-up issue).
- [ ] Defines experiment changelog format and retention expectations.
- [ ] Defines handoff expectations between engineering, security, and product.

## Functional Requirements

1. The module MUST teach `pydantic-evals` foundations (`Dataset`, `Case`, evaluator composition) with enterprise examples.
2. The module MUST include guidance for custom evaluators that remain single-purpose and composable.
3. The module MUST include LLM-as-a-judge guidance with rubric design and judge model governance.
4. The module MUST include adversarial and policy-focused evaluation suites.
5. The module MUST define explicit release gates and escalation paths.
6. The module MUST include a product-facing reporting schema translating technical metrics to decision-ready KPIs.
7. The module MUST define repeatable experiment metadata/versioning requirements and provide a machine‑readable JSON Schema / `pydantic` model (stored in `packages/shared`) that CI can validate.

## Technical Specification

### Content Targets

- New/updated learning materials under `learning/03-advanced-patterns/` for evaluation operations.
- Cross-links from `learning/02-core-concepts/README.md` and `learning/CONCEPTS.md` to the new evaluation playbook.
- Real code references from:
  - `packages/course-navigator/`
  - `packages/shared/`

### Canonical Evaluation Layers

1. **Deterministic checks**: schema/constraint validation, exact or rule-based assertions.
2. **Qualitative checks**: LLM-judge rubric scoring for helpfulness/relevance.
3. **Operational checks**: latency, token usage, cost, retries/fallback.
4. **Governance checks**: policy mapping, security challenge sets, trace reasons.

### Data and Reporting Model (Conceptual)

Each experiment run MUST persist an `evaluation_record` containing (at minimum):

- `experiment_id`, `run_id`, `dataset_version` (storage URI + SHA256), `dataset_hash`
- `model_version` (registry URI + digest), `model_hash`, `prompt_version` (git SHA/tag), `prompt_hash`, `tool_version`, `evaluator_version`
- `executor_id` (CI job id or user id), `run_timestamp`, `environment` (pre-merge/nightly/release)
- evaluator outcomes: `assertions[]` (id, pass/fail, numeric score), `score` (aggregated), `reason`/`reason_code`, `evidence_ids` (URIs to raw/sanitized outputs)
- operational metrics: `duration_ms`, `tokens`, `estimated_cost_usd`, `latency.p50_ms`, `latency.p95_ms`
- decision output: `decision` (`proceed`/`hold`/`escalate`), `decision_justification`
- integrity fields: `artifact_uris` (raw_output_uri, sanitized_output_uri), `evidence_signatures` (sha256)

A machine‑readable JSON Schema / `pydantic` model for `evaluation_record` MUST be added to `packages/shared` and used to validate CI artifacts.

### Compliance Acceptance Criteria

- Every `evaluation_run` MUST persist an `evaluation_record` containing the fields: `experiment_id`, `run_id`, `dataset_version`, `dataset_hash`, `model_version`, `model_hash`, `prompt_version`, `prompt_hash`, `evaluator_version`, `run_timestamp`, `executor_id`, `environment`, `assertions`, `failure_reasons`, `raw_output_uri`, `sanitized_output_uri`, `decision`, and `decision_justification`. Missing fields fail validation.
- All `critical` governance evaluations MUST fail CI and block merges automatically. A blocked merge requires manual remediation and explicit approval from the compliance owner.
- Evidence retention: raw evaluation outputs and audit records MUST be retained for at least **1 year**; red‑team/prompt‑injection artifacts for **3 years**; policy/security incident artifacts for **7 years**. Retention storage MUST be versioned and tamper‑evident (WORM or equivalent).
- Escalation mapping: every failure reason MUST map to an escalation level (`info`/`investigate`/`block_release`/`security_incident`) with a documented SLA for response and an assigned owner.

## Implementation Plan

### Phase 0: Foundations (Blocking)

- Define canonical evaluation taxonomy and glossary for learning docs.
- Identify reusable examples in `packages/course-navigator` and `packages/shared` for reuse.
- Define and publish the `evaluation_record` JSON Schema / `pydantic` model and a reference implementation in `packages/shared`.
- Specify reproducibility & artifact rules (storage URI + checksum conventions) and default retention windows.
- Provide CI gating example (GitHub Actions workflow + `just eval <package>` recipe) and decision table templates.
- Define owner roles (engineering owner, compliance owner, product owner) and SLAs for escalations.

**CHECKPOINT:** Foundation approved before story execution.

### Phase 1: P1 Stories (MVP)

- Implement Story 1 (baseline architecture).
- Implement Story 2 (governance/hardening coverage).
- Validate both stories as independently testable.

**CHECKPOINT:** P1 MVP can run end-to-end with explicit release gates.

### Phase 2: P2 Story

- Implement Story 3 (ROI and product-facing decision framework).
- Validate metric-to-decision mapping.

**CHECKPOINT:** Product stakeholders can consume evaluation report without code deep dive.

### Phase 3: P3 Story

- Implement Story 4 (recurring operations and regression policy).
- Validate scheduled execution and baseline comparison flow.

**CHECKPOINT:** Continuous evaluation workflow is documented and operable.

### Phase 4: Final QA + Docs Sync

- Run `just learning-validate`.
- Run targeted package checks as needed (`just check navigator`, etc.).
- Update status and linkages in learning indexes.

## Task Breakdown

- [ ] T001 [P] [FOUNDATION] Define evaluation taxonomy and glossary in learning docs.
- [ ] T002 [P] [FOUNDATION] Inventory existing examples in `course-navigator` and `shared` for reuse.
- [ ] T003 [FOUNDATION] Define canonical KPI/metric names and report schema.

- [ ] T004 [P] [US1] Draft baseline `Dataset`/`Case` architecture section.
- [ ] T005 [P] [US1] Draft focused evaluator composition guidance.
- [ ] T006 [US1] Define release gate thresholds and decision table.

- [ ] T007 [P] [US2] Draft adversarial evaluation suite design (prompt-injection/policy).
- [ ] T008 [P] [US2] Draft circuit-breaker and repeated-failure handling guidance.
- [ ] T009 [US2] Map evaluator outputs to compliance controls and escalation actions.

- [ ] T010 [P] [US3] Draft KPI-to-ROI interpretation guide for product stakeholders.
- [ ] T011 [P] [US3] Draft ablation/A-B comparison workflow.
- [ ] T012 [US3] Define release recommendation template (proceed/hold/escalate).

- [ ] T013 [P] [US4] Define recurring run cadence and ownership model.
- [ ] T014 [P] [US4] Define regression threshold policy and alerting behavior.
- [ ] T015 [US4] Define changelog and evidence retention checklist.
- [ ] T019 [P] [FOUNDATION] Add `evaluation_record` JSON Schema / `pydantic` model to `packages/shared` and unit tests.
- [ ] T020 [P] [FOUNDATION] Add example evaluation suite for `course-navigator` (dataset fixtures + evaluators + tests).
- [ ] T021 [P] [US1] Add CI gating example: `.github/workflows/evals.yml` and `just eval <package>` recipe.
- [ ] T022 [P] [US3] Add Release Recommendation template + ROI calculator example in `learning/03-advanced-patterns/`.
- [ ] T023 [P] [FOUNDATION] Define evidence retention policy and assign compliance/owner roles.

- [ ] T016 [FINAL] Update `learning/CONCEPTS.md` and module index links.
- [ ] T017 [FINAL] Execute validation commands and resolve doc structure issues.
- [ ] T018 [FINAL] Mark specification status and publish handoff notes.

## Testing Strategy

### Story-Level Validation

- **US1**: Run a baseline evaluation suite and verify deterministic release‑gate output and `evaluation_record` schema validation.
- **US2**: Run adversarial/policy cases and verify blocked outcomes, explicit reasons, and that `critical` failures fail CI and create an incident per escalation SLA.
- **US3**: Run variant comparison and verify KPI deltas produce a recommendation; A/B reports must include sample‑size, 95% CI and p‑value.
- **US4**: Run baseline‑vs‑current comparison and verify regression handling behavior and evidence retention (artifact URIs + checksums present).

### Quality Gates

- Documentation structure checks via `just learning-validate`.
- Workspace quality checks relevant to changed packages via `just check <package>`.
- Manual review: persona alignment checklist (Sarah, David, Marcus).

## Risks and Mitigations

- **Risk:** Overly complex evaluation framework for early teams.
  - **Mitigation:** Keep P1 minimal and publish a simple baseline first.
- **Risk:** LLM-judge variability creating unstable scores.
  - **Mitigation:** Use fixed rubrics, low-temperature settings, and trend-based interpretation.
- **Risk:** Metric overload for non-technical stakeholders.
  - **Mitigation:** Provide compact executive summary with decision-oriented KPIs.

## Open Questions

- Which artifact/versioning scheme is required for `dataset_version` and `model_version`? (recommended: registry digest + SHA256 + storage URI)
- Should governance (`critical`) failures automatically block merges, or produce a blocking warning requiring manual approval?
- Confirm retention windows for standard vs red‑team vs incident artifacts (recommendation: 1y / 3y / 7y).
- Which judge models, temperature and seed constraints are approved for LLM‑judge usage?
- Who is the canonical owner for recurring runs, alerts, and compliance sign‑offs (engineering / security / product)?
- What SIEM / alerting integration is required (e.g., Datadog, Splunk)?

## References

- `learning/00-misc/learner-personas/enterprise-architect.persona.md`
- `learning/00-misc/learner-personas/ai-engineer.persona.md`
- `learning/00-misc/learner-personas/product-manager.persona.md`
- `learning/CONCEPTS.md`
- `specs/README.md`
