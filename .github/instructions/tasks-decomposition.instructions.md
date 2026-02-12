---
description: 'Guidance for breaking down complex tasks, using subagents, and managing progress tracking.'
applyTo: '**'
---

# Tasks Decomposition

Orchestrate complex workflows by decomposing them into manageable subtasks and using the appropriate tracking mechanisms.

**MANDATORY**: These instructions MUST be followed for every multi-step request to ensure reliability and auditability.

## Session-Start Decomposition

When a session starts from a user prompt (rather than an existing specification), you must immediately analyze the request and choose a tracking mode:

### 1. Persistent Process Decomposition (PPD)
Use for **large, multi-step tasks** that require structured execution or might span multiple turns.
- **Action**: Create a `.processing.md` file in the workspace root.
- **Content**: User request summary, high-level action plan, and granular task lists.
- **Markers**: Use `[ ]` for pending, `[/]` for in-progress, and `[x]` for completed tasks.
- **Parallelism**: Group tasks with `[P]` markers to indicate they can be executed together.
- **Behavior**: Work silently across phases, updating the file as your primary status indicator.

### 2. Autonomous `todos` Tool
Use for **atomic, step-by-step tasks** that can be completed within a single autonomous cycle.
- **Action**: Use the `todos` tool to track immediate progress.
- **Example**: TDD cycles (test-fail-implement-pass-refactor), linting/fixing sequences, or single-file modifications.

## Specification-Based Execution

If working with an existing `SPEC-*.md` file, do NOT create a separate tracking file.
- **Source of Truth**: Rely exclusively on the "Task Breakdown" or "User Stories" section of the specification.
- **Markers**: Respect `[P]` markers for parallel tasks.
- **Status Transitions**: Periodically update the specification file itself to reflect progress.

## Designing for Efficiency

### Parallel Execution [P]
Tasks marked with `[P]` should be executed simultaneously or in a single phase to maximize throughput.
- **Grouping**: Execute all `[P]` tasks within the same story or phase together.
- **Dependencies**: Ensure all `[P]` tasks are completed before moving to sequential tasks that depend on them.
- **Subagents**: Use `agent/runSubagent` to delegate independent `[P]` tasks when complex research or multi-file creation is involved.

### Task Granularity Standards
- **Standalone Value**: Each task should represent a testable unit of work.
- **Atomic Edits**: Keep tasks small enough to avoid massive file replacements.
- **Validation**: Validate the results of each subtask before proceeding to dependent steps.
- **Context Preservation**: Ensure each subtask has enough context (inputs/outputs) to be executed by a subagent if needed.

## Progress Tracking Policy

| Scenario | Tracking Mechanism |
| :--- | :--- |
| **New prompt (complex/multi-file)** | `.processing.md` file (Persistent) |
| **New prompt (simple/single-file)** | `todos` tool (Internal) |
| **Existing Specification** | `SPEC-*.md` file (Internal markers) |
| **TDD / Small cycles** | `todos` tool (Internal) |
| **Discovery / Requirements gathering** | Specification (Draft phase) |
