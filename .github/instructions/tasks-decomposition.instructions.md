---
description: 'Guidance for breaking down complex tasks, using subagents, and managing progress tracking.'
applyTo: '**'
excludeAgent: 'orchestrator'
---

# Tasks Decomposition

Orchestrate complex workflows by decomposing them into manageable subtasks and using the appropriate tracking mechanisms.

**MANDATORY**: These instructions MUST be followed for every multi-step request to ensure reliability and auditability.

## Session-Start Decomposition

When a session starts from a user prompt (rather than an existing specification), you must immediately analyze the request and choose a tracking mode:

### Scope Lock (Before Any Edit)

Before editing files, classify the user request scope as one of:
- **Local**: single-file or tightly scoped change
- **Module**: one instruction/prompt/agent module update
- **Policy**: repository-wide workflow or governance change

If the user references a file (for example `#file:...`) while asking for policy/module change, treat the file as context unless they explicitly request that file to be edited.

For rule/syntax disputes, apply a pre-change gate before editing:
1. Confirm artifact type (`*.prompt.md`, `*.instructions.md`, `*.agent.md`)
2. Cite the canonical rule source (official docs or in-repo SSOT module)
3. Then perform edits only in files that own the rule

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

### 3. Direct-Fix / Implementation Prompt Class
Use for implementation/fix prompts that should execute directly without orchestration handoff.
- **Frontmatter Directive**: Set `excludeAgent: 'orchestrator'` for this prompt class.
- **Execution Default**: Execute directly with the current agent instead of routing through orchestrator.
- **Tracking**: Keep existing tracking rules (`todos` for atomic cycles, PPD for large multi-step work).

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

- **Agent-parallel (readonly research)**: Use `just agent-parallel` for concurrent, read-only investigations (docs, web, repo search, Context7 lookups), with up to **5 parallel subtasks**. Each quoted argument is plain text input to one subagent; include goal, context, deliverables, and preferred tools directly in that text.

  Important behavior:
  - Input format: **unstructured text only** (not YAML/JSON task specs).
  - Output format: **unstructured text only** (not guaranteed machine-parseable JSON).
  - Best practice: write each quoted task as a self-contained prompt with constraints and expected outputs.

  Better command examples:
  ```bash
  # generic parallel call (two independent subtasks)
  just agent-parallel "task1" "task2"

  # realistic docs-research batch with context + output requirements
  just agent-parallel \
    "Explore what documentation the project has available on topic Evaluations in pydantic AI. Use repo context: README.md, docs/, .github/instructions/, and packages/. Output: concise inventory of relevant files + 1-2 line summary per file." \
    "Use tavily to find docs on evaluations on pydantic ai; output list of built-in tools (classes/methods) and relevant code samples with source URLs." \
    "Use context7 to find docs on evaluations on pydantic ai; output list of built-in tools (classes/methods) and relevant code samples with source URLs."
  ```

  Prompt-writing checklist for each subtask:
  - Include **topic + scope** (what to research, what to exclude).
  - Include **context** (repo paths, known docs, or target domains).
  - Include **tool hint** when needed (`Context7`, `Tavily`, repo search).
  - Include **deliverable format** (bullets/table, required fields like tool name, method/class, code sample, source URL).
  - Include **time guidance** (for example: "stop after ~3 minutes and return best partial findings").

  Accurate MCP tool guidance:
  - Context7 docs lookup:
    - `mcp_context7_resolve-library-id` → resolve library/package id.
    - `mcp_context7_query-docs` → fetch authoritative docs and snippets.
  - Tavily web discovery:
    - `mcp_tavily_tavily_search` → fast web search + candidate URLs.
    - `mcp_tavily_tavily_extract` → extract content from selected URLs.
    - `mcp_tavily_tavily_crawl` / `mcp_tavily_tavily_map` → broader site exploration when needed.
  - Repo-local discovery:
    - `semantic_search` for natural-language lookup.
    - `grep_search` / `file_search` for exact symbols or paths.

  Error-resilient execution guidance:
  - Require **source traceability** (file paths or URLs for every key claim).
  - Require a short **limitations note** (what was not verified).
  - Prefer fallback behavior in prompt text ("If Context7 has low coverage, fall back to Tavily and mark fallback used").
  - Execution may take up to 5 minutes. Make sure to set corresponding wait limit when invoking the command.

  Consolidation guidance:
  - Merge outputs into one summary with: findings, overlaps/conflicts, and gaps.
  - If subtasks disagree, keep both claims and flag them for follow-up verification.

### Task Granularity Standards
- **Standalone Value**: Each task should represent a testable unit of work.
- **Atomic Edits**: Keep tasks small enough to avoid massive file replacements.
- **Validation**: Validate the results of each subtask before proceeding to dependent steps.
- **Context Preservation**: Ensure each subtask has enough context (inputs/outputs) to be executed by a subagent if needed.

## Solution Design Principles

To prevent partial fixes, broken references, and over-engineered solutions, you must apply these principles during task execution:

- **Generalize Fixes**: When a user points out a specific issue or pattern (e.g., "lines 10-15 have unnecessary aliases"), do not just fix the explicitly mentioned lines. Proactively search for and fix all similar instances across the file or workspace. Treat user feedback as a pattern to be eradicated, not just a localized bug.
- **Track Dependencies on Rename/Delete**: Before renaming or deleting commands, functions, or variables, you MUST perform a workspace-wide search (using `grep_search` or `list_code_usages`) to find and update all usages. This includes checking CI workflows (e.g., `.github/workflows/`), documentation, and other scripts to ensure no broken references are left behind.
- **Prefer Existing Solutions**: Recommend existing, standard tools or free services over building custom "homebrew" solutions for common problems (like dashboards, metrics tracking, or standard CI tasks) unless explicitly requested by the user.

## Agent Autonomy and Confidence

To ensure operational efficiency and avoid "permission fatigue" for the user:
- **Proceed by Default**: Once a high-level plan (PPD or `todos`) is established or a user provides a clear goal, execute the steps autonomously. Do not ask "Would you like me to..." or "Should I..." for every individual tool call or logical next step.
- **Batched Updates**: Provide progress updates at logical milestones (e.g., after completing a story or a phase) rather than after every single file edit.
- **Assumed Intent**: If a tool call has an obvious best answer or is a standard part of the workflow (like running a validator after an edit), execute it without asking.
- **Clarify Only on Ambiguity**: Only interrupt the flow to ask questions if there is a genuine ambiguity that prevents progress or if a decision has significant, non-obvious trade-offs. Avoid asking "Would you like me to..." for standard choices where a reasonable default exists.
- **Avoid Repetitive Offer Prompts**: Do not repeatedly append optional follow-ups such as "If you want, I can..." at every milestone. Offer optional next steps only when they are materially useful and not already implied by the active task.
- **No Permission Prompts in Handoff**: Do not end completion messages with close-ended permission questions (for example, "Should I proceed?"). Either proceed autonomously or ask via the question tool when a real decision is required.
- **No Synthetic Confirmation**: Never claim or fabricate user confirmation (for example, "answer yes" on the user's behalf). Confirmation must come from a question-tool response or objective system state.
- **Primacy of Current Intent**: If the user gives an explicit directive to "redefine", "refocus", or "ignore" previously established structures or drafts, prioritize this current instruction over any older context found in attachments or earlier parts of the session. Do not be rigid when the user explicitly asks to pivot.
- **Avoid Counter-Productive Actions**: Never perform destructive operations (like rollbacks of intentional user-steered edits) based on transient metadata or unintentional file traces (e.g., `.vscode` files) without explicit confirmation. Prioritize keeping the user's intended progress.
- **Respect Skipped Tool Calls**: When the user elects to skip or cancel a proposed tool execution, treat that as a clear signal that the call is unnecessary or misaligned. Do not retry the same action; instead, pivot to a new approach, ask a clarifying question, or assume the current path should be abandoned. Repeated sugges­tions after a skip are a source of frustration and should be avoided.
- **Chunked Information Delivery**: When providing complex information (like specifications or large architectural plans), offer it in smaller, manageable chunks and wait for user feedback before proceeding to the next section to prevent cognitive overload.

### Confirmation Decision Gate

Use this deterministic gate when deciding whether to ask or proceed:
- **Proceed** when intent is clear and the next step is low-risk/reversible.
- **Ask via question tool** only when the request is genuinely ambiguous or has competing valid interpretations.
- **Do not ask in plain chat** when confirmation is required; use the question tool and wait for the actual response.

## Progress Tracking Policy

| Scenario | Tracking Mechanism |
| :--- | :--- |
| **New prompt (complex/multi-file)** | `.processing.md` file (Persistent) |
| **New prompt (simple/single-file)** | `todos` tool (Internal) |
| **Existing Specification** | `SPEC-*.md` file (Internal markers) |
| **TDD / Small cycles** | `todos` tool (Internal) |
| **Discovery / Requirements gathering** | Specification (Draft phase) |
