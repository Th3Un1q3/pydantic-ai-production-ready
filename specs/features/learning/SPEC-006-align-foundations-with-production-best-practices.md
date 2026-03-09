---
spec-id: SPEC-006
title: Align Foundations With Production Best Practices
spec-type: learning
status: ready
created: 2026-03-08
owner: learning-ops
---

## Specification Progress

- [x] Complete discovery phase
- [x] Determine specification type
- [x] Draft specification from template
- [x] Validate against quality standards
- [x] Finalize specification for review

## Discovery Notes

- Canonical guidance followed for this draft: `.github/instructions/spec-writing.instructions.md` and `.github/prompts/write-spec.prompt.md`.
- `tmp/transcript.md` is supporting context for presenter emphasis and narrative cadence, not the source of truth for module scope or repository guidance.
- Existing Module 01 content partially covers the right themes but still underserves the intended direction in four ways: it does not open from a production-ready-system mindset, underemphasizes disciplined environment and workflow habits, does not keep Course Navigator central as the teaching artifact, and does not clearly separate documentation alignment from later package hardening.
- Existing learning spec precedent lives under `specs/learning/`, but this specification is intentionally created at `specs/features/learning/` to match the requested target path for this task.
- This specification is doc-first only. It defines documentation changes for Module 01 and explicitly defers Course Navigator hardening to a separate follow-up specification.

## Executive Summary

### Problem Statement

Module 01 currently introduces Pydantic AI competently, but it does not yet open with the course's intended promise: we are building a production-ready system from day one, and that starts with a strong development environment, disciplined engineering habits, and explicit architectural boundaries.

The main gaps are:

1. **Framing mismatch**: the current module still reads too much like a framework introduction instead of the start of a production-ready internal system built with deliberate engineering discipline.
2. **Foundations gap**: the module underplays the importance of dev containers, reproducible workflows, quality gates, configuration isolation, fail-fast validation, and other habits that should feel foundational rather than optional.
3. **Teaching-artifact gap**: Course Navigator is not yet explicit enough as the main artifact learners will use to understand how these practices map onto a real package in this repository.
4. **Best-practice sequencing gap**: the current material does not clearly separate what Module 01 should teach and apply now from what should be previewed now and operationalized later in subsequent modules and the follow-up package spec.
5. **Presenter usability gap**: the module does not yet serve the presenter as a strong narration companion. It needs clearer sequencing, stronger talking points, and explicit production framing that is informed by the transcript without being governed by it.

### Proposed Solution

Rewrite Module 01 as a **production-readiness foundations module** that is explicitly doc-first and presenter-aligned.

The rewrite will:

- Reframe the module around building a production-ready internal system from day one, beginning with disciplined setup, repeatable workflows, and ongoing engineering habits.
- Teach Pydantic AI through production engineering principles instead of generic feature enumeration, using Course Navigator as the main teaching artifact for grounding those ideas.
- Update the lesson set so the presenter can narrate from stable, repo-aligned materials that emphasize contracts, flexibility, observability by default, setup discipline, safety boundaries, and reliability patterns.
- Introduce requested best practices in a way appropriate for Module 01: explicitly mark which practices are taught and applied now versus previewed now for later operationalization.
- Record the dependency on a separate follow-up specification, not part of this task, for applying those practices to the intentionally imperfect `course-navigator` implementation.

### Success Criteria

- Module 01 is clearly positioned as the production foundations module for building a production-ready internal AI system from day one.
- The spec defines a doc-first implementation surface limited to Module 01 documentation.
- The transcript is treated as supporting context for presenter alignment, not as the canonical source for module scope or requirements.
- Course Navigator is explicitly named as the primary teaching artifact for Module 01.
- Dev environment, reproducible workflows, and engineering discipline are specified as foundational themes rather than setup footnotes.
- Best practices are clearly separated into apply-now versus preview-later guidance.
- Architecture-as-code and spec-first workflow are defined as teach-now practices with explicit acceptance criteria and implementation tasks for Module 01 docs.
- Each P1 story includes attached Role-Based Feedback Reports with concrete risks and mitigations from at least two learner personas.
- Requested best practices are either assigned to Module 01 content now or explicitly deferred with rationale.
- Course Navigator hardening is named as a follow-up specification and excluded from this implementation scope.
- The spec is reviewable, with assumptions, risks, and open questions clearly called out.

## Scope

### In Scope

- Specification for rewriting Module 01 documentation under `learning/01-fundamentals/`.
- Presenter alignment informed by `tmp/transcript.md` as supporting context.
- Updating the conceptual framing, learning objectives, and lesson boundaries for:
  - `learning/01-fundamentals/README.md`
  - `learning/01-fundamentals/01-introduction.md`
  - `learning/01-fundamentals/02-setup.md`
  - `learning/01-fundamentals/03-agent-anatomy.md`
- Reworking Module 01 substantially where needed so it starts from production-ready-system framing instead of preserving existing lesson structure by default.
- Making Course Navigator the main teaching artifact referenced throughout Module 01, while keeping code hardening out of scope.
- Integrating production best practices into Module 01 at the principle and documentation level.
- Clarifying what is taught now versus what is deferred to later modules or follow-up specs.

### Out of Scope

- Editing Module 01 lesson files as part of this task.
- Any package-code, test, or Course Navigator implementation changes.
- Retrofitting `packages/course-navigator/` to match the new guidance.
- Drafting, outlining, or preparing the follow-up Course Navigator hardening specification inside SPEC-006 implementation work.
- Expanding scope beyond Module 01 documentation alignment.
- Turning Module 01 into a full operations, CI/CD, or deployment module.

## Directional Inputs

The rewritten module should be shaped by repository goals first, with presenter materials used to improve delivery quality and narrative flow.

### Canonical Direction for Module 01

- Module 01 must frame the course as building a production-ready internal AI system from day one, not as exploring agents in a demo-first way.
- The module must start with environment quality, reproducible workflows, and engineering discipline as the baseline for everything that follows.
- Course Navigator must be the primary teaching artifact used to make the repository concrete for learners, while preserving its hardening work for later.
- The module must teach architecture-as-code and spec-first habits as part of normal engineering practice.
- The module must introduce safety, quality, contracts, and observability as first-class concerns from the beginning.

### Supporting Emphasis From the Transcript

- The course is for teams moving beyond demos toward reliable, auditable, scalable internal applications.
- The recommended first in-house use case is an internal-facing application because it offers lower risk and faster learning.
- Pydantic AI is presented as a strong fit for contract-first, structured, enterprise-oriented systems.
- Model and provider flexibility are strategic requirements, not implementation details.
- Observability and interpretability are essential for debugging and continuous improvement.
- AI-assisted coding is part of the normal workflow, but it must be captured in reusable, versioned assets and disciplined engineering practices.
- The setup should be as simple and unified as possible, with dev containers and `just`-based workflows reducing friction and drift.
- Deterministic quality must complement non-deterministic agent behavior.

### Presenter Needs This Spec Must Serve

The resulting docs should help the presenter:

- explain why this course starts at internal applications rather than public, customer-facing systems;
- connect enterprise adoption stages to the decision to use Pydantic AI;
- teach production principles before deeper implementation details;
- narrate the agent anatomy using architecture, contracts, dependencies, and reliability patterns rather than a toy coding tutorial;
- point learners toward reusable repository assets, shared prompts, and disciplined workflows.

## Best-Practice Coverage Map

This specification assigns each requested practice to one of three buckets: **apply now in Module 01**, **preview now for later operationalization**, or **defer**.

### Apply Now in Module 01

- **Production-first framing**: Open from the premise that the course is building a production-ready internal system from day one.
- **Reproducible development environment**: Make dev containers, pinned dependencies, and `just` workflows part of the engineering baseline.
- **Deterministic quality gates**: Connect `just check`, linting, tests, and validation to production AI engineering discipline.
- **Architecture as code / spec-first thinking**: State that meaningful course and system changes begin with reviewed specifications, then proceed to doc-first or code implementation.
- **Explicit contracts and structured outputs**: Teach contract-first design as a core reason to use Pydantic AI in production settings.
- **Configuration isolation**: Explain provider/model selection and environment-specific settings as isolated configuration concerns rather than scattered implementation details.
- **Dependency injection via Pydantic AI dependencies**: Present dependencies as the clean, testable way to pass runtime context, services, and data.
- **Zero trust for user-controlled prompt input**: Introduce prompt/context handling as untrusted input and describe safe boundaries for system prompts and dependencies.
- **Fail-fast validation**: Explain why validation should stop bad states early instead of letting unreliable flows continue silently.
- **Versioned prompts and artifacts**: Position prompts, templates, and planning assets as governed artifacts that should be versioned and reviewed.
- **Observability and auditability by default**: Treat tracing and evidence collection as baseline engineering capabilities, not optional add-ons.
- **Continuous improvement of AI-assisted coding**: Explain how reusable prompts, templates, skills, and review loops support systematic improvement.

### Preview Now for Later Operationalization

- **Model-agnostic design at runtime**: Explain provider flexibility as a production requirement and link it to future fallback strategies.
- **Test as a backend application at increasing depth**: Establish the expectation now, while leaving deeper test suite patterns for later modules and package-focused work.
- **Modular installation via `pydantic-ai-slim[...]`**: Mention slim installs as a footprint-control practice without turning Module 01 into packaging documentation.
- **Fallbacks, retries, and circuit breakers**: Mention them as production reliability patterns learners will operationalize later.
- **Deeper evaluation and hardening loops**: Preview that later modules and follow-up package work will turn these principles into applied workflows.

### Defer

- **Course Navigator hardening**: Handle it in a separate follow-up spec after documentation alignment is complete.

## Prioritized User Stories

### Story 1: Reframe Module 01 Around Production AI Foundations (Priority: P1) 🎯 MVP

As an enterprise-oriented learner, I want Module 01 to explain why this series starts with internal, production-minded agent systems so that I understand the course scope, intended maturity level, and why Pydantic AI is being taught in this context.

**Why this priority**: Without the right framing, the rest of the module reads like a generic framework overview instead of the beginning of a production engineering curriculum.

**Independent Test**: A learner can read the module overview and introduction and accurately explain the target audience, the internal-app starting point, and the production mindset of the course.

**Acceptance Criteria:**

- [ ] `learning/01-fundamentals/README.md` is specified to position Module 01 as the foundation for building production-ready internal AI applications.
- [ ] `learning/01-fundamentals/README.md` is specified to open with the claim that the course is building a production-ready internal system from day one.
- [ ] `learning/01-fundamentals/01-introduction.md` is specified to reflect the transcript's adoption journey and explain why internal apps are the recommended first in-house use case.
- [ ] The rewrite explicitly distinguishes this course from beginner/demo-oriented AI tutorials.
- [ ] The module framing explicitly covers contract-first development, structured outputs, provider flexibility, observability, deterministic quality, and engineering discipline as foundational concerns.
- [ ] The module framing explicitly introduces architecture-as-code and spec-first workflow, making clear that substantial course and system changes begin with a reviewed specification before documentation or package implementation.
- [ ] Course Navigator is specified as the primary teaching artifact used to make the repository concrete in Module 01.
- [ ] The content is written for experienced engineers, architects, and technically fluent product stakeholders rather than beginners.

**Role-Based Feedback Reports:**

**Persona:** Sarah Jenkins (`learning/00-misc/learner-personas/enterprise-architect.persona.md`)

- **Stance:** Approve
- **Critical Risks:** The framing could still read like a library overview if it does not clearly anchor Pydantic AI in enterprise architecture concerns such as contracts, observability, and provider flexibility.
- **Recommendations:** Make the README and introduction explicitly contrast production internal-app architecture with toy demos, and present specifications as the control point for architectural evolution.
- **Confidence:** 92%
- **Follow-Up Questions:** Should the introduction reference repository-level specifications directly, or keep the concept tool-agnostic while still teaching spec-first workflow?
- **Reflection:** The story is directionally strong because it moves the module toward enterprise architecture instead of syntax. The decisive factor is whether the documentation makes the planning artifacts feel like part of the architecture, not process overhead.

**Persona:** Marcus Thorne (`learning/00-misc/learner-personas/product-manager.persona.md`)

- **Stance:** Conditional
- **Critical Risks:** If the framing emphasizes architecture without explaining why internal apps are the recommended first product investment, the course may still underserve roadmap and trust concerns.
- **Recommendations:** Tie the internal-app starting point to lower-risk adoption, faster feedback loops, and clearer ROI. Keep the production framing understandable to technically fluent product stakeholders, not just engineers.
- **Confidence:** 84%
- **Follow-Up Questions:** Should the README include an explicit sentence about trust, time-to-value, and lower operational blast radius for internal apps?
- **Reflection:** The module will land better if business-facing readers can explain why the course starts here. The story is acceptable if the introduction makes that trade-off explicit instead of assuming the reader already agrees.

**Reconciliation Summary:** Sarah and Marcus both support the reframing, but Marcus requires clearer product-facing justification. The acceptance criteria now require explicit internal-app rationale and spec-first framing so the story satisfies both architecture and adoption concerns.

### Story 2: Make Setup and Workflow Reflect Real Engineering Discipline (Priority: P1) 🎯 MVP

As a learner preparing to follow the course, I want the setup lesson to explain the unified development environment and quality workflow so that I can adopt the same reproducible practices used throughout the series.

**Why this priority**: The transcript treats setup simplicity and determinism as a core principle, not a housekeeping detail.

**Independent Test**: A learner can explain why the repository uses dev containers, `just`, environment configuration, and quality gates, and can distinguish those choices from ad hoc local setup.

**Acceptance Criteria:**

- [ ] `learning/01-fundamentals/02-setup.md` is specified to focus on the rationale for unified setup: dev containers, dependency sync, environment consistency, and reduced local drift.
- [ ] The lesson explicitly treats `just init` and `just check` as examples of deterministic engineering workflow rather than mere commands to copy.
- [ ] The rewrite explains that AI systems should be developed and tested like backend applications, not like disposable notebooks.
- [ ] The rewrite introduces modular dependency selection, including `pydantic-ai-slim[...]`, as a production-footprint practice without turning the lesson into packaging documentation.
- [ ] The setup narrative explicitly connects spec-first planning, doc-first implementation, and deterministic quality gates so learners understand that disciplined changes start with reviewed specs and proceed through reproducible workflows.
- [ ] The rewrite defines quality gates, repeatability, local reproducibility, and configuration isolation as part of the course's baseline engineering contract.

**Role-Based Feedback Reports:**

**Persona:** Sarah Jenkins (`learning/00-misc/learner-personas/enterprise-architect.persona.md`)

- **Stance:** Approve
- **Critical Risks:** Setup guidance can become operationally shallow if it lists tools without explaining the architectural reason for standardization and reproducibility.
- **Recommendations:** Explain dev containers, `just`, and quality gates as controls that reduce drift and make agent systems behave like maintainable backend services. Include spec-first workflow as part of engineering discipline, not separate governance paperwork.
- **Confidence:** 90%
- **Follow-Up Questions:** Should the setup lesson mention how standardized workflows support later observability, testing, and provider swaps?
- **Reflection:** The story works when the environment choices are explained as architecture-enabling constraints. Without that, setup will still feel like onboarding boilerplate.

**Persona:** David Chen (`learning/00-misc/learner-personas/ai-engineer.persona.md`)

- **Stance:** Conditional
- **Critical Risks:** A workflow lesson that celebrates reproducibility but does not emphasize auditability, untrusted inputs, and deterministic checks will not meet compliance-first needs.
- **Recommendations:** Explicitly frame `just check`, versioned prompts, and controlled environments as audit and verification tools. Preserve the backend-style testing language so the module does not imply notebook-style experimentation is acceptable for production work.
- **Confidence:** 87%
- **Follow-Up Questions:** Should the setup lesson name prompt versioning and dependency pinning as part of the reproducibility baseline, or keep that detail for the anatomy lesson?
- **Reflection:** The core setup direction is correct, but compliance-focused readers need to see why deterministic workflow matters operationally. The lesson should connect environment control to evidence, not just convenience.

**Reconciliation Summary:** Sarah and David agree that setup must teach disciplined, reproducible engineering rather than a quick install checklist. The acceptance criteria now require spec-first workflow linkage, backend-style testing language, and deterministic quality gates so the lesson satisfies both architecture and compliance expectations.

### Story 3: Teach Agent Anatomy Through Contracts, Dependencies, and Trust Boundaries (Priority: P1) 🎯 MVP

As a senior engineer, I want the agent anatomy lesson to emphasize contracts, dependency injection, trust boundaries, and runtime reliability so that I learn patterns suitable for production systems rather than only the syntax of the `Agent` API.

**Why this priority**: This is the point where the course either establishes serious engineering habits or falls back into framework-tour territory.

**Independent Test**: A learner can explain the roles of model/provider configuration, structured outputs, dependencies, system prompts, tools, and trust boundaries in a production-oriented agent architecture.

**Acceptance Criteria:**

- [ ] `learning/01-fundamentals/03-agent-anatomy.md` is specified to present the agent as a production application component with explicit contracts and runtime context boundaries.
- [ ] The lesson explains dependency injection via Pydantic AI dependencies as the preferred mechanism for sharing context, services, and data cleanly across prompts, tools, and validators.
- [ ] The lesson introduces zero-trust prompt handling, making clear that user-controlled or retrieved input must not be promoted into the system prompt unchecked.
- [ ] The lesson explains why prompts, prompt templates, and agent instructions should be versioned and reviewed as engineering assets.
- [ ] The lesson introduces observability, fail-fast validation, retries, and fallback patterns as part of the anatomy discussion, while reserving deeper implementation for later modules.
- [ ] The lesson maintains model/provider agnosticism and explicitly avoids implying that the architecture is tied to a single vendor.

**Role-Based Feedback Reports:**

**Persona:** Sarah Jenkins (`learning/00-misc/learner-personas/enterprise-architect.persona.md`)

- **Stance:** Approve
- **Critical Risks:** Agent anatomy often collapses into API syntax and misses failure engineering, trust boundaries, and architectural separation of concerns.
- **Recommendations:** Keep contracts, dependencies, provider flexibility, and forward-looking reliability patterns in the lesson structure itself. Make clear that dependencies and validators are architecture tools, not optional niceties.
- **Confidence:** 91%
- **Follow-Up Questions:** Should observability be introduced as part of every component explanation, or as a closing section on cross-cutting concerns?
- **Reflection:** This story is aligned with enterprise needs because it treats the agent as a system component rather than a prompt wrapper. The main risk is slipping back into a feature tour during implementation.

**Persona:** David Chen (`learning/00-misc/learner-personas/ai-engineer.persona.md`)

- **Stance:** Conditional
- **Critical Risks:** Trust-boundary language can stay too abstract unless the lesson explicitly says untrusted inputs must be isolated from system prompts and runtime privileges.
- **Recommendations:** Preserve zero-trust wording, call out user-controlled and retrieved content as untrusted by default, and treat prompt/version review as part of the security posture. Keep retries and fallbacks framed as controlled reliability mechanisms rather than silent self-healing.
- **Confidence:** 89%
- **Follow-Up Questions:** Should the lesson mention deterministic stop conditions when validation fails repeatedly, or reserve that for later reliability modules?
- **Reflection:** The story is acceptable if it teaches security boundaries concretely. Compliance-first readers need to see the difference between using LLM features and governing them.

**Reconciliation Summary:** Sarah and David both approve the production-oriented anatomy direction, with David requiring sharper security language. The acceptance criteria already make zero-trust handling, versioned prompt assets, and architecture-grade dependencies explicit, which addresses the conditional concerns.

### Story 4: Establish a Presenter-Friendly Documentation Spine for Module 01 (Priority: P2)

As the presenter and course maintainer, I want Module 01 docs to align with the intended talk track and repository teaching goals so that the written materials support narration, live explanation, and future course maintenance.

**Why this priority**: Presenter-friendly structure improves teaching quality and reduces drift between spoken and written guidance.

**Independent Test**: The presenter can map major transcript beats to Module 01 pages without inventing new framing during delivery.

**Acceptance Criteria:**

- [ ] The specification defines a recommended narrative flow across README, introduction, setup, and agent anatomy.
- [ ] The docs are specified to foreground reusable repository assets such as prompts, templates, skills, and shared engineering patterns.
- [ ] The docs are specified to use concise, presentation-friendly sections that can anchor narration without requiring large code walkthroughs.
- [ ] The spec identifies where transcript language should inform emphasis rather than dictate wording or scope.

## Functional Requirements

1. The specification MUST remain doc-first and limit implementation scope to Module 01 documentation alignment.
2. The specification MUST define the implementation surface as the Module 01 overview and three lesson documents: `README.md`, `01-introduction.md`, `02-setup.md`, and `03-agent-anatomy.md`.
3. The rewritten module MUST present the series as focused on production-ready internal AI applications, not beginner experiments or generic chatbot demos.
4. The rewritten module MUST explicitly state that the course is building a production-ready internal system from day one and that disciplined setup and workflow habits are part of that promise.
5. The rewritten module MUST explain the AI adoption journey sufficiently to justify why internal-facing apps are a practical first in-house build.
6. The rewritten module MUST treat Course Navigator as the primary teaching artifact for Module 01 while keeping code hardening out of scope.
7. The rewritten module MUST teach contract-first engineering, structured outputs, provider flexibility, observability, and deterministic quality as foundational principles.
8. The rewritten module MUST describe AI systems as backend-style applications that require testing, fail-fast validation, repeatability, and explicit quality gates.
9. The rewritten module MUST teach architecture-as-code and spec-first workflow as foundational practice, explicitly stating that meaningful course and system changes begin with a reviewed specification before doc or package implementation.
10. The rewritten module MUST introduce dependency injection with Pydantic AI dependencies as a clean and testable mechanism for runtime context sharing.
11. The rewritten module MUST define zero-trust prompt handling as a foundational safety practice and explicitly warn against promoting untrusted user-controlled input into the system prompt.
12. The rewritten module MUST position prompts, prompt templates, AI-assistance assets, and planning artifacts as version-controlled engineering artifacts.
13. The rewritten module MUST explain unified development setup through dev containers and repository-standard workflows as part of production readiness.
14. The rewritten module MUST explain configuration isolation and provider/model selection boundaries as part of maintainable production design.
15. The rewritten module MUST mention modular installation choices such as `pydantic-ai-slim[...]` as a dependency-footprint best practice, without expanding into package-management implementation details.
16. The rewritten module MUST reinforce continuous improvement of AI-assisted coding through reusable prompts, templates, skills, review practices, and deterministic checks.
17. The specification MUST clearly separate which practices are applied now in Module 01, previewed for later modules, or deferred to follow-up specifications.
18. Each P1 story MUST include at least two attached Role-Based Feedback Reports and a reconciliation summary, with any conditional concerns reflected in acceptance criteria or mitigations.
19. The specification MUST explicitly defer Course Navigator code hardening, advanced retry/fallback implementation, and broader operationalization work to later modules or follow-up specifications.
20. The specification MUST identify assumptions, risks, and open questions for user review before implementation begins.

## Technical Specification

### Target Documentation Surface

This specification defines future edits only for the following files:

- `learning/01-fundamentals/README.md`
- `learning/01-fundamentals/01-introduction.md`
- `learning/01-fundamentals/02-setup.md`
- `learning/01-fundamentals/03-agent-anatomy.md`

Optional supporting references during implementation may include:

- `tmp/transcript.md`
- `GETTING_STARTED.md`
- `learning/CONCEPTS.md`
- `learning/00-misc/ai-engineering-cheatsheet.md`
- `packages/course-navigator/README.md`

`tmp/transcript.md` is a supporting reference for presenter emphasis and flow. The canonical implementation target remains this specification plus repository conventions and the Module 01 documentation surface.

This specification does not authorize edits to package code, tests, or Course Navigator implementation files.

### Narrative Structure

The future doc rewrite should follow this narrative spine:

1. **Module README**: define the module as the production foundations entry point; explain audience, learning objectives, and why this module matters.
2. **Introduction**: explain the AI adoption journey, why internal apps are the right starting point, why Course Navigator is the repository teaching artifact, and why Pydantic AI is a strong fit for contract-first systems.
3. **Setup**: explain the unified dev environment, dev containers, `just` workflows, spec-first/doc-first working rhythm, configuration isolation, environment setup, and deterministic quality gates as part of the engineering baseline.
4. **Agent Anatomy**: explain providers, contracts, dependencies, prompts, tools, observability, trust boundaries, fail-fast validation, and reliability patterns through a production lens.

### Content Rules for the Rewrite

- Keep the tone aligned with experienced engineers and architects.
- Prefer principles, architecture reasoning, and repository-aligned references over lengthy toy examples.
- Use the transcript as supporting presenter context, but derive scope and requirements from this spec and repository guidance rather than transcribing it.
- Keep examples vendor-flexible and avoid coupling the teaching narrative to a single model provider.
- Treat prompts, setup, and quality workflows as first-class engineering assets.
- Treat specifications and architecture notes as first-class repository assets that govern later doc and code changes.
- Treat Course Navigator as the through-line artifact for explanation, without turning Module 01 into a code-hardening effort.
- Explicitly distinguish foundational concepts from advanced follow-on topics.

### Explicit Deferrals

The rewritten docs may mention the following topics briefly, but they are not to be implemented or expanded fully in Module 01:

- production fallback orchestration;
- circuit breakers and advanced retry strategies;
- detailed evaluation pipelines;
- deployment and runtime operations;
- Course Navigator hardening work;
- deeper packaging and dependency-management guidance beyond the slim-install mention.

## Implementation Plan

### Phase 0: Scope Lock and Narrative Baseline

- Confirm that Module 01 remains documentation-only for this effort.
- Extract useful presenter beats from `tmp/transcript.md` into a reusable outline for doc implementation without treating the transcript as normative.
- Confirm which requested best practices belong in Module 01 now versus later modules.
- Lock Course Navigator as the primary teaching artifact for Module 01 without pulling its implementation hardening into scope.
- Lock in architecture-as-code/spec-first framing as part of the module baseline rather than a deferred process note.

**CHECKPOINT:** Scope is locked to docs, presenter alignment is agreed, and deferred topics are explicit.

### Phase 1: Story 1 — Production Foundations Reframe

- Rewrite the module overview and introduction around production-ready internal-system framing, using the transcript only as supporting context.
- Align learning objectives with contract-first engineering, provider flexibility, observability, deterministic quality, and disciplined engineering habits.
- Make Course Navigator explicit as the main teaching artifact used to anchor Module 01.
- Add explicit spec-first language showing that architecture decisions and major course changes begin as reviewed specifications before implementation.

**CHECKPOINT:** A reader can understand the course positioning and intended audience from README + introduction alone.

### Phase 2: Story 2 — Unified Setup and Quality Workflow

- Rewrite setup guidance to emphasize dev containers, consistent environment setup, and deterministic quality gates.
- Connect setup choices to backend-style engineering discipline rather than onboarding convenience only.
- Add configuration isolation and reproducible workflow expectations as part of the baseline working contract.
- Tie setup workflow to spec-first planning and doc-first execution so the process feels like an engineering system, not a collection of commands.

**CHECKPOINT:** A reader can explain why the repo uses unified setup and quality gates for AI development.

### Phase 3: Story 3 — Production Agent Anatomy

- Rewrite the agent anatomy lesson around contracts, dependencies, trust boundaries, observability, fail-fast validation, and versioned prompt assets.
- Keep deeper reliability implementations as forward references rather than scope creep.

**CHECKPOINT:** A reader can describe a production-oriented agent architecture and its trust boundaries without needing package-code changes.

### Phase 4: Story 4 — Presenter Alignment Pass

- Ensure the four documents form a presentation-friendly sequence.
- Reduce drift between intended presenter narrative and written module flow.
- Add explicit references to reusable repository assets where helpful.

**CHECKPOINT:** The presenter can use the docs as a narration companion with minimal improvisation.

### Phase 5: Review and Scope-Safe Handoff

- Review assumptions, risks, and unresolved questions with the user.
- Record that Course Navigator hardening depends on a separate future specification and is not drafted as part of SPEC-006 implementation.

**CHECKPOINT:** Module 01 doc spec is approved and the future hardening dependency remains clearly separated from this implementation.

## Task Breakdown

- [ ] T001 [P] [FOUNDATION] Extract supporting presenter beats from `tmp/transcript.md` for Module 01 without treating them as normative requirements.
- [ ] T002 [P] [FOUNDATION] Confirm Module 01 scope boundaries and explicit deferrals.
- [ ] T003 [FOUNDATION] Define the doc-first implementation surface for README, introduction, setup, and agent anatomy.
- [ ] T004 [FOUNDATION] Lock Course Navigator as the primary teaching artifact for Module 01.

- [ ] T005 [P] [US1] Reframe `learning/01-fundamentals/README.md` around production foundations, internal-app positioning, and day-one engineering discipline.
- [ ] T006 [P] [US1] Reframe `learning/01-fundamentals/01-introduction.md` around adoption journey, Course Navigator, Pydantic AI fit, and contract-first thinking.
- [ ] T007 [US1] Add explicit architecture-as-code and spec-first workflow framing across README and introduction.
- [ ] T008 [US1] Align learning objectives and audience assumptions across README and introduction.

- [ ] T009 [P] [US2] Rewrite `learning/01-fundamentals/02-setup.md` around dev containers, reproducibility, and quality gates.
- [ ] T010 [P] [US2] Add backend-style testing, spec-first/doc-first workflow, configuration isolation, and deterministic engineering framing to the setup lesson.
- [ ] T011 [US2] Introduce modular installation guidance and its placement within the setup narrative.

- [ ] T012 [P] [US3] Rewrite `learning/01-fundamentals/03-agent-anatomy.md` around contracts, dependencies, and provider flexibility.
- [ ] T013 [P] [US3] Add zero-trust prompt handling, prompt versioning, observability, and fail-fast validation as explicit anatomy topics.
- [ ] T014 [US3] Add forward references for retries, fallbacks, and later reliability topics without expanding scope.

- [ ] T015 [P] [US4] Align section flow and headings to support presenter narration.
- [ ] T016 [P] [US4] Identify reusable repository assets to reference in the module, including relevant specifications as planning artifacts.
- [ ] T017 [US4] Perform final editorial pass for presenter alignment and concise teaching flow.

- [ ] T018 [FINAL] Review the module rewrite against spec-defined requirements and requested best-practice coverage.
- [ ] T019 [FINAL] Validate markdown formatting and documentation consistency.
- [ ] T020 [FINAL] Confirm the implementation notes preserve the dependency on a separate future Course Navigator hardening spec without drafting it here.

## Testing Strategy

### Story-Level Validation

- **US1**: Review README and introduction to confirm they explain the internal-app starting point, target audience, and production framing without slipping into beginner tutorial language.
- **US1**: Confirm the framing explicitly teaches architecture-as-code/spec-first workflow as part of production practice rather than a side-process.
- **US2**: Review setup content to confirm it treats environment setup, testing, spec-first/doc-first workflow, and quality gates as engineering-system concerns rather than incidental setup steps.
- **US3**: Review agent anatomy content to confirm contracts, DI, observability, trust boundaries, and provider flexibility are taught explicitly.
- **US4**: Compare the final doc flow to the intended presenter narrative and confirm major beats are present and ordered coherently, with `tmp/transcript.md` used only as supporting context.

### Quality Gates

- Markdown linting must pass for modified docs.
- Each P1 story must retain two attached Role-Based Feedback Reports plus a reconciliation summary.
- Reviewer checklist must confirm each requested best practice is either covered or explicitly deferred.
- Final review must confirm no package-code changes are implied as part of this implementation.
- Final review must confirm no follow-up Course Navigator specification drafting is included in the implementation plan or task breakdown.

## Risks and Mitigations

- **Risk:** The rewrite becomes too broad and starts absorbing later-module topics.
  - **Mitigation:** Keep a strict defer list and limit content to foundational framing and principles.
- **Risk:** The docs overfit the transcript and become too presentation-specific.
  - **Mitigation:** Use the transcript for structure and emphasis, but write durable documentation that is governed by this spec and stands alone.
- **Risk:** The spec implies Course Navigator code must change immediately to match the docs.
  - **Mitigation:** State repeatedly that Course Navigator hardening is a separate follow-up spec.
- **Risk:** Best-practice coverage becomes a checklist dump instead of a coherent module.
  - **Mitigation:** Assign each practice to the lesson where it best supports the narrative and defer deep dives where needed.

## Assumptions

- Module 01 should stay focused on architectural and engineering foundations, not implementation-heavy walkthroughs.
- The audience remains experienced enough to handle backend and architecture terminology without introductory Python teaching.
- The transcript is useful supporting context for presenter intent, but this spec remains the canonical implementation target.
- Existing Course Navigator imperfections are intentional and should remain untouched until a later hardening spec is approved.

## Open Questions for Review

1. Should Module 01 explicitly mention OpenRouter as the recommended development-time aggregator, or should that remain in setup references only to keep provider-neutrality stronger?
2. How explicitly should Module 01 discuss prompt version control mechanics at this stage: principle only, or concrete repository pattern references?
3. Should `learning/01-fundamentals/spec.md` remain untouched as historical context, or should a later implementation pass reconcile it with the rewritten docs?
4. How much of observability should be introduced in Module 01 versus reserved for later reliability/evaluation modules?

## Follow-Up Specification Note

A separate follow-up specification will be required to apply these production best practices to the intentionally imperfect `packages/course-navigator/` implementation. That future spec remains a dependency note only in SPEC-006, is explicitly out of scope for this implementation, and must be drafted only after this Module 01 documentation direction is reviewed and approved.

## References

- `tmp/transcript.md`
- `learning/01-fundamentals/README.md`
- `learning/01-fundamentals/01-introduction.md`
- `learning/01-fundamentals/02-setup.md`
- `learning/01-fundamentals/03-agent-anatomy.md`
- `learning/01-fundamentals/spec.md`
- `specs/README.md`
- `.github/instructions/spec-writing.instructions.md`
- `.github/prompts/write-spec.prompt.md`
- `specs/learning/SPEC-001-refine-foundations-module.md`
- `specs/learning/SPEC-005-pydantic-ai-evaluations-persona-aligned.md`
