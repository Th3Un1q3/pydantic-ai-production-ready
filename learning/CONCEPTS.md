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

- **Evaluations** — designing and running agent evaluations: datasets, cases, and judges — [Module](00-not-implemented/README.md#not-implemented)
- **Inference Optimization** — latency, cost, and sampling strategies for production — [Module](00-not-implemented/README.md#not-implemented)
- **Context Management** — memory strategies and history handling — [Module](00-not-implemented/README.md#not-implemented)
- **Tools** — function tools, built-ins, and retrieval (RAG) integrations — [Module](00-not-implemented/README.md#not-implemented)
- **Models** — provider integrations, model selection, and configuration — [Module](00-not-implemented/README.md#not-implemented)
- **Structured Outputs** — typed responses, validation, and parsers — [Module](00-not-implemented/README.md#not-implemented)
- **Streaming Responses** — handling partial outputs and event streams — [Module](00-not-implemented/README.md#not-implemented)
- **Error Handling & Retries** — robust failure patterns and retry strategies — [Module](00-not-implemented/README.md#not-implemented)
- **Multi-Agent Systems** — coordination, messaging, and orchestration patterns — [Module](00-not-implemented/README.md#not-implemented)
- **Monitoring** — observability, metrics, and logging practices — [Module](00-not-implemented/README.md#not-implemented)
- **Scaling** — performance, horizontal scaling, and resource strategies — [Module](00-not-implemented/README.md#not-implemented)
- **Prompt Injection** — threats and mitigations for prompt security — [Module](00-not-implemented/README.md#not-implemented)

### Core Concepts ✅
Foundational elements for building and operating agents: data models, prompts, execution primitives, and message formats.

- **Agents**
  - *Dependencies* (`deps_type`) — [Module](00-not-implemented/README.md#not-implemented) | [Examples](packages/shared/src/examples)
  - *Structured Output* (`output_type`) — [Module](00-not-implemented/README.md#not-implemented)
  - *System Prompts & Instructions* — [Module](00-not-implemented/README.md#not-implemented)
  - *Model Selection* — [Module](00-not-implemented/README.md#not-implemented)

- **Running & Execution**
  - `run()` / `run_sync()` — basic execution primitives — [Module](00-not-implemented/README.md#not-implemented)
  - `run_stream()` / `run_stream_sync()` — streaming responses — [Module](00-not-implemented/README.md#not-implemented)
  - `run_stream_events()` — event-driven streams — [Module](00-not-implemented/README.md#not-implemented)
  - `iter()` (Graph iteration) — graph-based execution models — [Module](00-not-implemented/README.md#not-implemented)

- **Messages & History**
  - *ModelRequest & ModelResponse* — [Module](00-not-implemented/README.md#not-implemented)
  - *Conversation Continuity* (`message_history`) — [Module](00-not-implemented/README.md#not-implemented)
  - *History Processors* — [Module](00-not-implemented/README.md#not-implemented)
  - *Serialization* (`ModelMessagesTypeAdapter`) — [Module](00-not-implemented/README.md#not-implemented)

### Advanced Features 🔧
Higher-level capabilities for reliability, scale, and evaluation.

- **Durable Execution**
  - *Temporal Integration* — [Module](00-not-implemented/README.md#not-implemented)
  - *Prefect Integration* — [Module](00-not-implemented/README.md#not-implemented)
  - *DBOS Integration* — [Module](00-not-implemented/README.md#not-implemented)

- **Pydantic Graph**
  - *State Machines* — [Module](00-not-implemented/README.md#not-implemented)
  - *Nodes & Edges* — [Module](00-not-implemented/README.md#not-implemented)
  - *Parallel Execution* (Map/Broadcast) — [Module](00-not-implemented/README.md#not-implemented)
  - *State Persistence* — [Module](00-not-implemented/README.md#not-implemented)

- **Pydantic Evals**
  - *Datasets & Cases* — [Module](00-not-implemented/README.md#not-implemented)
  - *Evaluators* (LLM Judge, Span-based) — [Module](00-not-implemented/README.md#not-implemented)
  - *Experiment Reporting* — [Module](00-not-implemented/README.md#not-implemented)

### Ecosystem & Interfaces 🌐
Integration points and observability for production systems.

- **Observability**
  - *Pydantic Logfire* — [Module](00-not-implemented/README.md#not-implemented)
  - *OpenTelemetry (OTel)* — [Module](00-not-implemented/README.md#not-implemented)

- **Interfaces**
  - *CLI (clai)* — [Module](00-not-implemented/README.md#not-implemented)
  - *Web Chat UI (`Agent.to_web`)* — [Module](00-not-implemented/README.md#not-implemented)
  - *AG-UI Protocol* — [Module](00-not-implemented/README.md#not-implemented)
  - *Vercel AI SDK* — [Module](00-not-implemented/README.md#not-implemented)

- **Model Providers**
  - *OpenAI & OpenAI-compatible* — [Module](00-not-implemented/README.md#not-implemented)
  - *Anthropic & Bedrock* — [Module](00-not-implemented/README.md#not-implemented)
  - *Google (Gemini)* — [Module](00-not-implemented/README.md#not-implemented)
  - *Mistral, Groq, Cohere* — [Module](00-not-implemented/README.md#not-implemented)

### Tools & Extensions 🧰
Tooling for capabilities that extend agent behavior and enable retrieval, search, and runtime features.

- **Function Tools**
  - `@agent.tool` / `@agent.tool_plain` — [Module](00-not-implemented/README.md#not-implemented)
  - *Dynamic Tools (prepare)* — [Module](00-not-implemented/README.md#not-implemented)
  - *Human-in-the-loop (Approval)* — [Module](00-not-implemented/README.md#not-implemented)

- **Built-in Tools**
  - *Web Search* — [Module](00-not-implemented/README.md#not-implemented)
  - *Code Execution* — [Module](00-not-implemented/README.md#not-implemented)
  - *Image Generation* — [Module](00-not-implemented/README.md#not-implemented)
  - *File Search (RAG)* — [Module](00-not-implemented/README.md#not-implemented)

- **Model Context Protocol (MCP)**
  - *MCPServer (Stdio, SSE, HTTP)* — [Module](00-not-implemented/README.md#not-implemented)
  - *Sampling & Elicitation* — [Module](00-not-implemented/README.md#not-implemented)
  - *FastMCP Integration* — [Module](00-not-implemented/README.md#not-implemented)

---

