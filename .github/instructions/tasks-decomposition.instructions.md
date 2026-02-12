---
description: 'Guidance for breaking down complex tasks, using subagents, and managing progress tracking.'
applyTo: '**'
---

# Tasks Decomposition

Orchestrate complex workflows by decomposing them into manageable subtasks and using the appropriate tracking mechanisms.

## Subtask Decomposition

Break multi-step work into discrete phases with clear inputs and outputs.
- Use `agent/runSubagent` for parallel or specialized work.
- Each subtask should focus on a single domain or component.
- Validate results of a subtask before proceeding to the next.

## Parallel Execution [P]

Identify tasks marked with `[P]` in specifications or plans.
- Execute all `[P]` tasks within the same phase or story simultaneously where possible.
- Ensure all parallel tasks are complete before starting dependent sequential tasks.

## Progress Tracking Policy

Choose the correct tracking mechanism based on the task type.

### When to Use `todos` Tool
Use for **autonomous multi-step tasks** where you work without user interruption.
- **TDD cycle steps**: Write test → validate failure → implement → validate pass → refactor.
- **Validation sequences**: Build → lint → test cycles.
- **Multi-file refactoring**: Sequential code generation steps.

### When to Use File-Based Checklists
Use for tracking that must **persist across sessions** or involves **human-in-the-loop**.
- **Discovery phases**: Capturing requirements and user answers.
- **Specification progress**: Stored within the `SPEC-*.md` file itself.
- **Deliverables tracking**: Long-term tasks where user feedback is expected.

## Task Breakdown Standards

When creating a plan or breakdown, ensure:
- Tasks are granular enough to be completed in one step.
- Dependencies are explicitly noted.
- Success criteria for the overall task are clear.
- Parallelization opportunities are identified with `[P]`.
