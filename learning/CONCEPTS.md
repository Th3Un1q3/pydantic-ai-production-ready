# Concepts

## Overview

Index of concepts and techniques covered in the learning modules. Allows to see what is covered where, and find related code and documentation.

Example:

```markdown
Context Management - Techniques for managing conversational context in AI agents, including memory strategies and state tracking.
- [Module 3](03-advanced-patterns/02-context-management.md#context-management)
- [Specific Solution](packages/shared/src/examples/context_management.py)
- [Documentation](https://pydantic.ai/docs/usage/agents/context-management)
```

## Index

This page organizes the core ideas and techniques covered across the learning modules, grouped by logical areas to make it easier to find related content and examples.

### Related topics 🔗

Quick cross-cutting topics and short descriptions you can reference from modules and examples:

- **Evaluations** — designing and running agent evaluations: datasets, cases, and judges — [Docs](https://ai.pydantic.dev/evals/)
- **Inference Optimization** — latency, cost, and sampling strategies for production — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Context Management** — memory strategies and history handling — [Docs](https://ai.pydantic.dev/message-history/)
- **Chains** — differences, when to use which, and hybrid patterns — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Tools** — function tools, built-ins, and retrieval (RAG) integrations — [Docs](https://ai.pydantic.dev/tools/)
- **Models** — provider integrations, model selection, and configuration — [Docs](https://ai.pydantic.dev/models/overview/)
- **Structured Outputs** — typed responses, validation, and parsers — [Docs](https://ai.pydantic.dev/output/)
- **Streaming Responses** — handling partial outputs and event streams — [Docs](https://ai.pydantic.dev/output/#streamed-results)
- **Error Handling & Retries** — robust failure patterns and retry strategies — [Docs](https://ai.pydantic.dev/retries/)
- **Multi-Agent Systems** — coordination, messaging, and orchestration patterns — [Docs](https://ai.pydantic.dev/multi-agent-applications/)
- **Monitoring** — observability, metrics, and logging practices — [Docs](https://ai.pydantic.dev/logfire/)
- **Scaling** — performance, horizontal scaling, and resource strategies — [Docs](https://ai.pydantic.dev/durable_execution/overview/)
- **Prompt Injection** — threats and mitigations for prompt security — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Harnessing LLMs** — best practices for working with large language models — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Runaway Agents** — detection and prevention of uncontrolled behavior — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Agent-to-Agent Communication (A2A Protocol)** — protocols and standards for direct communication between agents — [Docs](https://ai.pydantic.dev/a2a/)

### Core Concepts ✅

Foundational elements for building and operating agents: data models, prompts, execution primitives, and message formats.

- **Agents**
  - *Dependencies* (`deps_type`) — [Docs](https://ai.pydantic.dev/dependencies/) | [Examples](packages/shared/src/examples)
  - *Structured Output* (`output_type`) — [Docs](https://ai.pydantic.dev/output/)
  - *System Prompts & Instructions* — [Docs](https://ai.pydantic.dev/agents/#instructions)
  - *Model Selection* — [Docs](https://ai.pydantic.dev/models/overview/)

- **Running & Execution**
  - `run()` / `run_sync()` — basic execution primitives — [Docs](https://ai.pydantic.dev/run/)
  - `run_stream()` / `run_stream_sync()` — streaming responses — [Docs](https://ai.pydantic.dev/output/#streamed-results)
  - `run_stream_events()` — event-driven streams — [Docs](https://ai.pydantic.dev/run/)
  - `iter()` (Graph iteration) — graph-based execution models — [Docs](https://ai.pydantic.dev/graph/)

- **Messages & History**
  - *ModelRequest & ModelResponse* — [Docs](https://ai.pydantic.dev/api/messages/)
  - *Conversation Continuity* (`message_history`) — [Docs](https://ai.pydantic.dev/message-history/)
  - *History Processors* — [Docs](https://ai.pydantic.dev/message-history/)
  - *Serialization* (`ModelMessagesTypeAdapter`) — [Docs](https://ai.pydantic.dev/api/messages/)

### Advanced Features 🔧

Higher-level capabilities for reliability, scale, and evaluation.

- **Durable Execution**
  - *Temporal Integration* — [Docs](https://ai.pydantic.dev/durable_execution/temporal/)
  - *Prefect Integration* — [Docs](https://ai.pydantic.dev/durable_execution/prefect/)
  - *DBOS Integration* — [Docs](https://ai.pydantic.dev/durable_execution/dbos/)

- **Pydantic Graph**
  - *State Machines* — [Docs](https://ai.pydantic.dev/graph/)
  - *Nodes & Edges* — [Docs](https://ai.pydantic.dev/graph/)
  - *Parallel Execution* (Map/Broadcast) — [Docs](https://ai.pydantic.dev/graph/beta/parallel/)
  - *State Persistence* — [Docs](https://ai.pydantic.dev/graph/)

- **Pydantic Evals**
  - *Datasets & Cases* — [Docs](https://ai.pydantic.dev/evals/core-concepts/)
  - *Evaluators* (LLM Judge, Span-based) — [Docs](https://ai.pydantic.dev/evals/evaluators/overview/)
  - *Experiment Reporting* — [Docs](https://ai.pydantic.dev/evals/reporting/)

### Ecosystem & Interfaces 🌐

Integration points and observability for production systems.

- **Observability**
  - *Pydantic Logfire* — [Docs](https://ai.pydantic.dev/logfire/)
  - *OpenTelemetry (OTel)* — [Docs](https://ai.pydantic.dev/logfire/#alternative-observability-backends)

- **Interfaces**
  - *CLI (clai)* — [Docs](https://ai.pydantic.dev/cli/)
  - *Web Chat UI (`Agent.to_web`)* — [Docs](https://ai.pydantic.dev/web/)
  - *AG-UI Protocol* — [Docs](https://ai.pydantic.dev/ui/ag-ui/)
  - *Vercel AI SDK* — [Docs](https://ai.pydantic.dev/ui/vercel-ai/)

- **Model Providers**
  - *OpenAI & OpenAI-compatible* — [Docs](https://ai.pydantic.dev/models/openai/)
  - *Anthropic & Bedrock* — [Docs](https://ai.pydantic.dev/models/)
  - *Google (Gemini)* — [Docs](https://ai.pydantic.dev/models/google/)
  - *Mistral, Groq, Cohere* — [Docs](https://ai.pydantic.dev/models/)

### Tools & Extensions 🧰

Tooling for capabilities that extend agent behavior and enable retrieval, search, and runtime features.

- **Function Tools**
  - `@agent.tool` / `@agent.tool_plain` — [Docs](https://ai.pydantic.dev/tools/)
  - *Dynamic Tools (prepare)* — [Docs](https://ai.pydantic.dev/tools-advanced/)
  - *Human-in-the-loop (Approval)* — [Docs](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval)

- **Built-in Tools**
  - *Web Search* — [Docs](https://ai.pydantic.dev/builtin-tools/)
  - *Code Execution* — [Docs](https://ai.pydantic.dev/builtin-tools/)
  - *Image Generation* — [Docs](https://ai.pydantic.dev/builtin-tools/)
  - *File Search (RAG)* — [Docs](https://ai.pydantic.dev/builtin-tools/)

- **Model Context Protocol (MCP)**
  - *MCPServer (Stdio, SSE, HTTP)* — [Docs](https://ai.pydantic.dev/mcp/server/)
  - *Sampling & Elicitation* — [Docs](https://ai.pydantic.dev/mcp/overview/)
  - *FastMCP Integration* — [Docs](https://ai.pydantic.dev/mcp/fastmcp-client/)
