---
description: 'Analyze user sessions to identify frustration markers, investigate root causes, and implement instruction-based improvements.'
name: 'evolve-ai-workflows'
agent: 'agent'
tools:
  - 'read'
  - 'search'
  - 'edit'
  - 'execute'
  - 'agent'
  - 'todo'
  - 'vscode'
argument-hint: 'Optional session IDs or time range to focus the analysis'
---

# Evolve AI Workflows

Analyze recent user-agent interactions to identify areas where the agent's behavior caused friction or frustration, and codify the learnings into permanent repository instructions.

## Orchestration Strategy

This prompt uses an autonomous agentic workflow to discover and fix interaction patterns:

1. **Discovery Phase** → Use `search` (grep) to find frustration markers in session logs and `read` to inspect transcripts.
2. **Analysis Phase** → Use the current agent or `agent/runSubagent` with the `agent` agent to perform deep-dive root cause analysis on a per transcript/session basis.
3. **Implementation Phase** → Use `edit` to update `.github/instructions/` and `execute` to run validators.

## Task Decomposition

### Phase 1: Exploration and Marker Detection

1. **Define Investigation Scope**:
   - Use `/workspace/logs/copilot/session.log` to identify the temporal sequence of sessions (ordered from old to new).
   - Focus on sessions within the user-provided time range if specified.
   - If no range is provided, analyze sessions from the **last 2 weeks**.
   - **Redundancy Check**: Skip sessions that have already been analyzed or those where the corresponding instruction improvements have already been implemented.
2. **Grep Logs**: Search the session files identified in step 1 (located in `/workspace/logs/copilot/sessions/{sessionId}.ndjson`) for frustration markers.
   - Keywords: `wrong`, `not what I asked`, `useless`, `broken`, `again`, `frustrat`, `fail`, `cannot`, `can't`, `unable`, `you`.
3. **Map Transcripts**: Identify the `transcript_path` for each flagged session.
4. **Read Details**: Use `read` to inspect the full transcripts (usually in `.jsonl` format) to understand the interaction context.

### Phase 2: Root Cause Analysis

Analyze each flagged interaction to determine:
- **What happened?**: What was the specific tool call or response that failed the user's expectation?
- **Why did it happen?**: Was it an instruction ambiguity, an over-engineered default, "permission fatigue," or a failure to follow the "Primacy of Current Intent"?
- **How should it have been handled?**: Define the ideal behavioral pattern.

### Phase 3: Instruction Evolution

1. **Codify Learnings**: Update the relevant instruction module in `.github/instructions/` (e.g., `tasks-decomposition.instructions.md`, `python.instructions.md`).
2. **Module Update Ritual**:
   - Follow `instruction-authoring.instructions.md` for proper formatting.
   - Use the **Single Source of Truth** principle to avoid duplication.
   - Add explicit behavioral rules (e.g., "Always proceed by default when...", "Prioritize current intent over...").
3. **Verification**: Run `just check` or relevant validators to ensure instruction updates don't break existing metadata standards.

## Quality Standards

- **Traceability**: Every instruction update must be linked to a specific finding from a session log.
- **Actionability**: Use "must/should" language in instruction updates rather than passive suggestions.
- **Brevity**: Keep instruction updates concise and focused on the corrective behavior.
