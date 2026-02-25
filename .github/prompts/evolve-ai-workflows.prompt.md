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
argument-hint: 'Mode input: none/time range | session ID | current conversation + extra context'
---

# Evolve AI Workflows

Analyze recent user-agent interactions to identify areas where the agent's behavior caused friction or frustration, and codify the learnings into permanent repository instructions.

## Workflow Modes

Select exactly one mode based on user input:

- **Mode A — Recent Sessions Scan (standalone)**:
   - Trigger when the prompt is invoked with no arguments, or only a time range (for example: `last 7 days`, `2026-02-01..2026-02-10`).
   - Analyze sessions in the provided range; if absent, default to the **last 2 weeks**.
- **Mode B — Specific Session Analysis (standalone)**:
   - Trigger when a session ID is provided (for example: UUID-like ID).
   - Analyze only that session and its transcript.
- **Mode C — Current Conversation Evolution (in-chat)**:
   - Trigger when the prompt is invoked during an active conversation and the user asks to learn from this chat (optionally with extra context).
   - Use the current conversation plus user-provided context as primary evidence, and optionally compare with closely related recent sessions.

When input is ambiguous, ask one concise clarifying question using `vscode/askQuestions`; otherwise proceed autonomously.
If no answer is returned, apply the simplest default that preserves progress: Mode C for active in-chat requests, otherwise Mode A with the last 2 weeks.

## Orchestration Strategy

This prompt uses an autonomous agentic workflow to discover and fix interaction patterns:

1. **Mode Resolution Phase** → Determine mode from arguments/context, then define concrete evidence sources.
2. **Discovery Phase** → Use `search` (grep) and `read` to gather only the evidence required by the selected mode.
3. **Analysis Phase** → Use `agent/runSubagent` for deep-dive root cause analysis per session/transcript or for structured analysis of the current conversation.
4. **Implementation Phase** → Use `edit` to update `.github/instructions/` and `execute` to run validators.

## Task Decomposition

### Phase 1: Mode Resolution and Evidence Collection

1. **Resolve Mode**:
   - **Mode A**: derive session set with `just copilot-sessions-list --min-prompts 2` using user time range or default last 2 weeks.
       ```bash
      # Default range: last 2 weeks (skip low-signal one-prompt sessions)
      just copilot-sessions-list --min-prompts 2

      # Explicit range
      just copilot-sessions-list --min-prompts 2 --from 2026-02-01 --to 2026-02-10

      # Include all sessions (including one-prompt sessions) when needed
      just copilot-sessions-list --min-prompts 1
       ```
    - **Mode B**: validate the provided session ID and retrieve only that session with `just copilot-sessions-read <id>`.
       ```bash
       # Base read (lightweight default)
       just copilot-sessions-read 0005e958-d59f-4c10-9c30-2d7d93174744

       # Deeper evidence when needed (assistant + tool calls)
       just copilot-sessions-read 0005e958-d59f-4c10-9c30-2d7d93174744 --include-assistant --include-tool-calls

       # Optional maximum detail
       just copilot-sessions-read 0005e958-d59f-4c10-9c30-2d7d93174744 --include-full-events
       ```
   - **Mode C**: use current chat transcript/context and any extra user input as primary source.
2. **Apply Redundancy Check**:
   - Skip already-analyzed sessions if their learnings are already codified.
   - In Mode C, avoid re-codifying existing rules unless new evidence reveals a broader principle.
3. **Grep/Inspect Evidence**:
   - For Modes A/B, use `just copilot-sessions-list ...` output to triage candidate sessions by user frustration markers.
   - Use `user_message_preview` as a fast signal for confusion/frustration language before deep transcript reads.
   - Prioritize sessions where `transcript_ref_status` is **not** `missing` (likely loadable transcript); defer `missing` unless signals are unusually strong.
   - After triage, inspect prioritized candidates with `just copilot-sessions-read <id> ...`.
   - For Mode C, extract friction markers from the active conversation first, then optionally scan nearby sessions for corroboration.
   - Keywords: `wrong`, `not what I asked`, `useless`, `broken`, `again`, `frustrat`, `fail`, `cannot`, `can't`, `unable`, `you`.
4. **Map and Read Transcripts**:
   - Modes A/B: use `just copilot-sessions-read <id> --include-assistant --include-tool-calls` for investigation of agent responses and tool activity.
   - Escalate to `--include-full-events` only when additional event-level detail is required.
   - Mode C: Treat the current conversation as the transcript and normalize it into the same analysis structure used for session files.

### Phase 2: Root Cause Analysis

Analyze each flagged interaction to determine:
- **What happened?**: What was the specific tool call or response that failed the user's expectation?
- **Why did it happen?**: Was it an instruction ambiguity, an over-engineered default, "permission fatigue," or a failure to follow the "Primacy of Current Intent"?
- **How should it have been handled?**: Define the ideal behavioral pattern.

Execution requirements:
- Use `agent/runSubagent` when analyzing more than one evidence source or when Mode C includes substantial extra context.
- Require each analysis result to include: `pattern`, `root cause`, `generalized rule`, and `target instruction module`.

### Phase 3: Instruction Evolution

1. **Discover** the appropriate targets for change.  Based on the patterns and
   root cause defined in Phase 2, search the repository for related
   instruction modules, prompts, or agent specs.  Candidates might live under
   `.github/instructions/`, `.github/prompts/`, or `.github/agents/`.

   - Use `grep`/`semantic_search` with keywords extracted from the generalized
     rule (e.g. "permission fatigue", "task decomposition", "human‑in‑loop").
   - Collect a short list of files that appear to govern the problematic
     behavior.
   - Document reasoning for each candidate (one‑sentence notes are fine).

2. **Choose** which file(s) are the best subject(s) for the update.  Prefer
   modules that already own the relevant principle and have broader scope; if
   a behavior is cross‑cutting, it may warrant a new section or a small new
   instruction file rather than changing an unrelated module.

3. **Codify Learnings**: Once targets are selected, edit the chosen file(s).
   Follow the usual module‑update ritual:
   - Comply with `instruction-authoring.instructions.md` formatting rules.
   - Maintain the **Single Source of Truth**; avoid duplicating rules across
     files.
   - Add explicit behavioral language and, if helpful, a brief comment noting
     the motivation (e.g. "added after evaluating repeated skip requests").

4. **Verification**: Run `just check` or the relevant validators to ensure the
   edits do not violate metadata or formatting standards, and that the new
   guidance integrates smoothly.


Mode-specific completion criteria:
- **Mode A**: At least one generalized, repository-relevant improvement from recent-session patterns.
- **Mode B**: At least one durable instruction improvement mapped directly to the analyzed session.
- **Mode C**: At least one improvement derived from current conversation friction, integrated without duplicating existing rules.

## Quality Standards

- **Wider Application**: Before codifying a fix, ask: what is the general principle this mistake reveals? A naming confusion in a test factory signals a project-wide naming standard gap; fix the principle, not the symptom. Broaden every finding to cover the full class of problems, and update the instruction module that owns that general principle.
- **Narrative Rationale**: Integrate the "why" into the instruction's prose — not as a standalone "Rationale" or "traced to session" block. The rule must read as coherent guidance that stands alone. Use the motivation as the opening of the section or fold it into the rule statement itself.
- **Actionability**: Use "must/should" language in instruction updates rather than passive suggestions.
- **Brevity**: Keep instruction updates concise and focused on the corrective behavior.
- **Schema-First Metadata Changes**: When a learning involves frontmatter or metadata, verify key support for the specific artifact type (`*.prompt.md`, `*.instructions.md`, `*.agent.md`) before editing.
- **Scope Lock**: If the user references a file while asking for system-level improvements, treat that file as context unless they explicitly request it as the edit target.
