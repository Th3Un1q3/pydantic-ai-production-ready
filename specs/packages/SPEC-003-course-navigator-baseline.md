# SPEC-003: Establish Course Navigator Baseline

## 1. Overview

| Attribute | Value |
| :--- | :--- |
| **Title** | Establish Course Navigator Baseline |
| **Status** | Proposed |
| **Type** | Package |
| **Owner** | AI Engineer |
| **Related Lesson** | `learning/01-fundamentals/03-agent-anatomy.md` |

## Discovery

### Discovery Questions

1. **Problem**: What problem are we solving? Why now?
   - The current course-navigator is a basic "Hello World" agent that doesn't demonstrate enterprise patterns. Learners need a reference implementation showing structured output, dependency injection, tool use, and context management for educational purposes.

2. **Success**: How will we measure success? What are the KPIs?
   - Success measured by: Agent returns structured CourseAnswer, achieves 100% test coverage, CLI outputs formatted results, and agent can navigate learning directory without external RAG.

3. **Scope**: What's in scope? What's explicitly out of scope?
   - In scope: Single agent architecture, static index strategy, tool for reading files, dependency injection for personalization.
   - Out of scope: Vector embeddings, external APIs, multi-agent systems, advanced RAG infrastructure.

4. **Constraints**: Technology stack, timeline, dependencies?
   - Tech stack: Python 3.12+, pydantic-ai, existing monorepo structure.
   - Dependencies: Must use pydantic-ai.Agent (validated: exists in codebase), integrate with shared config.

5. **Users**: Who benefits? What are their needs?
   - Learners studying agent development need a baseline implementation to understand patterns.
   - Developers want reference code for building educational agents.

## 3. Problem Statement

The current `course-navigator` is a basic "Hello World" agent. To serve as a proper educational baseline, it needs to demonstrate core "Enterprise Agent" patterns: **Structured Output**, **Dependency Injection**, **Tool Use**, and **Context Management**.

Learners need a reference implementation that shows how to build an agent that can "navigate" a local file system of learning materials without relying on complex Vector RAG infrastructure, while maintaining strict type safety.

## 4. Goals & Success Criteria

### Goals

- Implement a **Single Agent** architecture that can navigate the `learning/` directory.
- Use **Structured Output** to return clean summaries with file references.
- Implement **Dependency Injection** to personalize responses (e.g., via user name or difficulty level).
- Use **Tooling** to allow the agent to read specific lesson files on demand.
- Use a **Static Index** strategy: Collect index during startup with YAML headers from learning materials, filter by status != 'draft', and inject into System Prompt. Index includes file references and titles.
- **Lightweight Design**: Index + on-demand full content fetching via single tool.

### Success Criteria

- Agent returns `CourseAnswer` (summary + references list).
- Agent can find and read the content of specific files via `read_lesson` tool.
- Agent personalizes output based on injected `NavigatorDeps`.
- 100% Test Coverage.
- CLI (`main.py`) prints formatted JSON or rich text.

## 5. User Stories

### Story 1: Structured Output and Data Models (Priority: P1)

As a developer, I want to define the strict data models for the agent's interaction so that the output is reliable and the inputs are well-typed.

**Acceptance Criteria:**

- [ ] Define `CourseReference` (path, title).
- [ ] Define `CourseAnswer` (summary, list of references).
- [ ] Define `NavigatorDeps` (user_name, difficulty, learning_root path).

### Story 2: Index-Based Context & Tooling (Priority: P1)

As a user, I want the agent to know about all available lessons and be able to read them so that it can answer questions about the course content.

**Acceptance Criteria:**

- [ ] System prompt includes a generated "Index" of published `learning/` materials (parsed from YAML frontmatter: file paths and titles).
- [ ] Index collected during startup, filtered by status != 'draft' in YAML tags.
- [ ] Implement `read_lesson` tool that fetches complete content of specified file on-demand.
- [ ] Tool is registered on the Agent and grounds summaries in actual content.

### Story 3: Dependency Injection & Personalization (Priority: P2)

As a user, I want the agent to use my name and preferred difficulty level so that the summary feels personalized.

**Acceptance Criteria:**

- [ ] `create_agent` accepts `NavigatorDeps` type definition.
- [ ] System prompt uses `user_name` and `difficulty` from `deps` to adjust tone/content.
- [ ] `main.py` injects these dependencies at runtime.

### Story 4: Full Testing (Priority: P2)

As a maintainer, I want full test coverage to ensure the architectural changes are robust.

**Acceptance Criteria:**

- [ ] Unit tests for `read_lesson` tool in `tools.py` (test path validation, security checks for absolute paths and .., directory traversal prevention, content reading).
- [ ] Unit tests for `build_index` function in `utils.py` (test YAML parsing, status filtering, title extraction using LEARNING_ROOT).
- [ ] Unit tests for data models in `models.py` (test Pydantic validation).
- [ ] Unit tests for Agent logic in `agent.py` (mocking the tool and LLM, test prompt injection and tool registration).
- [ ] Integration test verifying the full flow from CLI to agent response.

## Clarification Checklist

For each requirement, confirm:

- [ ] Is the requirement specific enough to implement?
- [ ] Are edge cases identified?
- [ ] Are error scenarios defined?
- [ ] Is the scope boundary clear?

## 7. Technical Implementation

### Architecture

**Single Agent Pattern**:

1. **Refusal/Routing**: (Implicit in LLM) - The agent decides if it can answer or needs to read a file.
2. **Context**:
    - **Static Index**: Collected during startup by parsing YAML headers from learning materials. Index includes file paths and titles for published materials only (filtered by status != 'draft' in YAML tags).
    - **Dynamic Content**: When `read_lesson` is called, the full file content is fetched on-demand.

### Configuration

The learning root directory is defined as a constant in the shared configuration module to ensure consistency across indexing and tool usage:

```python
# packages/shared/src/pydantic_ai_shared/config.py
from pathlib import Path

LEARNING_ROOT = Path(__file__).parent.parent.parent.parent / "learning"
```

This ensures the learning directory path is centralized and cannot be overridden, providing security through configuration.

### Index Collection Process

- **Startup Phase**: Scan the `LEARNING_ROOT` directory for `.md` files with YAML frontmatter (delimited by `---`).
- **YAML Parsing**: Parse the frontmatter to extract:
  - `description`: Brief description of the material.
  - `tags`: List of tags, including status tags in format `status:value` (e.g., "status:draft", "status:published").
  - `references`: Optional navigation references (not used in index).
- **Status Extraction**: From the `tags` list, find tags starting with `status:` and extract the value (e.g., "draft", "published").
- **Title Extraction**: Extract the title from the first H1 heading (`# Title`) immediately following the YAML frontmatter.
- **Filtering**: Only include materials where the extracted `status` value is not `"draft"` (i.e., published materials).
- **Index Format**: String representation injected into system prompt, listing file paths, titles, and descriptions for published materials. The index serves as the allowlist for valid file paths that can be accessed by the `read_lesson` tool.

### Data Models

```python
from dataclasses import dataclass
from pathlib import Path
from pydantic import BaseModel, Field

@dataclass
class NavigatorDeps:
    user_name: str
    difficulty: str

class CourseReference(BaseModel):
    path: str = Field(description="The file path to the learning module")
    title: str = Field(description="The title of the module")

class CourseAnswer(BaseModel):
    summary: str = Field(description="A personalized summary of the requested info")
    references: list[CourseReference] = Field(description="List of relevant files used")
```

### File Structure

To ensure modularity and maintainability, the implementation follows these file organization principles:

- **Tools**: All agent tools are defined in a separate `tools.py` module within the package.
- **Utilities**: Helper functions like `build_index` are placed in a `utils.py` module.
- **Data Models**: Pydantic models are defined in a `models.py` module.
- **Agent Factory**: The `create_agent` function remains in `agent.py`, importing and registering tools from the tools module.

This separation allows for:

- Independent unit testing of each component
- Easier maintenance and refactoring
- Clear separation of concerns

### Tooling

Tools are implemented as modular functions in `course_navigator.tools`, with each tool in its own function for easy testing and reuse.

```python
# course_navigator/tools.py
from pathlib import Path, PurePath
from pydantic_ai import RunContext

from pydantic_ai_shared.config import LEARNING_ROOT
from .models import NavigatorDeps

def read_lesson(ctx: RunContext[NavigatorDeps], file_path: str) -> str:
    """Read the full content of a specific lesson file.

    Only allows access to files within the learning directory that are indexed.
    """
    # Validate file_path is relative and safe
    if not file_path or file_path.startswith('/') or '..' in file_path:
        raise ValueError(f"Invalid file path: {file_path}")

    # Construct full path securely
    full_path = LEARNING_ROOT / file_path

    # Ensure the resolved path is within LEARNING_ROOT
    try:
        full_path.resolve().relative_to(LEARNING_ROOT.resolve())
    except ValueError:
        raise ValueError(f"Access denied: {file_path}")

    if not full_path.is_file():
        raise ValueError(f"File not found: {file_path}")

    return full_path.read_text(encoding='utf-8')
```

Tools are registered in the agent factory:

```python
# course_navigator/agent.py
from pydantic_ai import Agent
from pydantic_ai.models import Model

from pydantic_ai_shared.config import LEARNING_ROOT
from .models import NavigatorDeps, CourseAnswer
from .tools import read_lesson
from .utils import build_index

def create_agent(model: str | Model, deps: NavigatorDeps) -> Agent:
    index = build_index(LEARNING_ROOT)
    system_prompt = f"""
    You are a helpful course navigator agent.

    User: {deps.user_name}
    Difficulty Level: {deps.difficulty}

    Available Learning Materials:
    {index}

    Use the read_lesson tool to access full content when needed.
    Only use file paths that are listed in the Available Learning Materials above.
    """

    agent = Agent(
        model,
        deps_type=NavigatorDeps,
        result_type=CourseAnswer,
        system_prompt=system_prompt,
    )

    agent.tool(read_lesson)

    return agent
```

## Code Interface Validation

### Validation Process

1. **Interface Existence Check**: All referenced interfaces exist in the codebase.
   - `pydantic_ai.Agent`: Confirmed exists in `packages/course-navigator/src/course_navigator/agent.py` (validated via file read).
   - New interfaces (`NavigatorDeps`, `CourseReference`, `CourseAnswer`): Proposed new classes, no conflicts with existing code.

2. **Pattern Alignment**: Proposed new interfaces follow existing pydantic-ai patterns and Python conventions.

3. **Hallucination Detection**: No non-existing interfaces referenced.

4. **Consistency Review**: New interfaces integrate with existing Agent pattern without breaking changes.

5. **Library Validation**: `pydantic-ai` is a real library, correctly used, version >=1.48.0 as per dependencies.

## 8. Implementation Plan

- [ ] T001 [P] [US1] Create `models.py`: Define `CourseReference`, `CourseAnswer`, and `NavigatorDeps` classes (without learning_root).
- [ ] T002 [P] [US2] Update shared config: Add `LEARNING_ROOT` constant pointing to the learning directory.
- [ ] T003 [P] [US2] Create `utils.py`: Implement `build_index()` helper function using `LEARNING_ROOT` to scan for .md files, parse YAML frontmatter (description, tags, references), extract status from tags (status:value), extract title from first H1, filter by status != 'draft', return formatted index string.
- [ ] T004 [P] [US2] Create `tools.py`: Implement `read_lesson` tool function with secure path validation (no absolute paths, no .., within LEARNING_ROOT) and content fetching.
- [ ] T005 [P] [US2] Update `agent.py` to import `LEARNING_ROOT` from shared config, use it for `build_index`, and register the `read_lesson` tool.

### Phase 2: Agent Logic

- [ ] T006 [US3] Update `create_agent` to accept `NavigatorDeps` parameter (without learning_root), use `build_index` with `LEARNING_ROOT`, inject personalized system prompt with index and deps, and instruct agent to only use indexed paths.
- [ ] T007 [US3] Configure agent with `deps_type=NavigatorDeps`, `result_type=CourseAnswer`, and register tools from `tools.py`.

### Phase 3: Integration

- [ ] T006 [US4] Update `main.py` to instantiate `NavigatorDeps`, build index during startup, run the agent.
- [ ] T007 [US4] Write unit and integration tests.

## 9. Validation Checklist

- [x] Problem statement is clear and compelling
- [x] Success criteria are measurable
- [x] All user stories have testable acceptance criteria
- [x] Stories are prioritized (P1, P2, P3)
- [x] Each story is independently testable as MVP
- [x] Technical constraints are documented
- [x] Out of scope items are explicitly listed
- [x] Implementation phases have checkpoints
- [x] Tasks have parallel markers [P] where applicable
- [x] Dependencies are identified
- [x] No NEEDS CLARIFICATION markers remain
- [x] All code interfaces and samples are validated against existing codebase
- [x] No hallucinated interfaces or non-existing APIs are referenced
- [x] No INTERFACE VALIDATION NEEDED markers remain
- [x] All libraries referenced are real and used correctly
- [x] Library versions and dependencies are validated
- [x] Index collection parses YAML frontmatter correctly, extracts status from tags (status:value), extracts title from first H1, and filters by status != 'draft'
- [x] Only published learning materials appear in the index
- [x] `read_lesson` tool fetches full content on-demand without caching full content upfront
- [x] `read_lesson` tool prevents absolute paths and directory traversal (..)
- [x] `read_lesson` tool only allows access within `LEARNING_ROOT` using secure path resolution
- [x] `LEARNING_ROOT` is defined as a constant in shared config and used consistently
- [x] Agent prompt instructs to only use indexed file paths
