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

- **Evaluations** — designing and running agent evaluations: datasets, cases, and judges — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Inference Optimization** — latency, cost, and sampling strategies for production — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Context Management** — memory strategies and history handling — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Chains** — differences, when to use which, and hybrid patterns — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Tools** — function tools, built-ins, and retrieval (RAG) integrations — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Models** — provider integrations, model selection, and configuration — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Structured Outputs** — typed responses, validation, and parsers — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Streaming Responses** — handling partial outputs and event streams — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Error Handling & Retries** — robust failure patterns and retry strategies — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Multi-Agent Systems** — coordination, messaging, and orchestration patterns — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Monitoring** — observability, metrics, and logging practices — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Scaling** — performance, horizontal scaling, and resource strategies — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Prompt Injection** — threats and mitigations for prompt security — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Harnessing LLMs** — best practices for working with large language models — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Runaway Agents** — detection and prevention of uncontrolled behavior — [Module](00-misc/NOT_IMPLEMENTED.md)
- **Agent-to-Agent Communication (A2A Protocol)** — protocols and standards for direct communication between agents — [Module](00-misc/NOT_IMPLEMENTED.md)

### Core Concepts ✅

Foundational elements for building and operating agents: data models, prompts, execution primitives, and message formats.

- **Agents**
  - *Dependencies* (`deps_type`) — [Module](00-misc/NOT_IMPLEMENTED.md) | [Examples](packages/shared/src/examples)
  - *Structured Output* (`output_type`) — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *System Prompts & Instructions* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Model Selection* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Running & Execution**
  - `run()` / `run_sync()` — basic execution primitives — [Module](00-misc/NOT_IMPLEMENTED.md)
  - `run_stream()` / `run_stream_sync()` — streaming responses — [Module](00-misc/NOT_IMPLEMENTED.md)
  - `run_stream_events()` — event-driven streams — [Module](00-misc/NOT_IMPLEMENTED.md)
  - `iter()` (Graph iteration) — graph-based execution models — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Messages & History**
  - *ModelRequest & ModelResponse* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Conversation Continuity* (`message_history`) — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *History Processors* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Serialization* (`ModelMessagesTypeAdapter`) — [Module](00-misc/NOT_IMPLEMENTED.md)

### Advanced Features 🔧

Higher-level capabilities for reliability, scale, and evaluation.

- **Durable Execution**
  - *Temporal Integration* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Prefect Integration* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *DBOS Integration* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Pydantic Graph**
  - *State Machines* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Nodes & Edges* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Parallel Execution* (Map/Broadcast) — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *State Persistence* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Pydantic Evals**
  - *Datasets & Cases* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Evaluators* (LLM Judge, Span-based) — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Experiment Reporting* — [Module](00-misc/NOT_IMPLEMENTED.md)

### Ecosystem & Interfaces 🌐

Integration points and observability for production systems.

- **Observability**
  - *Pydantic Logfire* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *OpenTelemetry (OTel)* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Interfaces**
  - *CLI (clai)* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Web Chat UI (`Agent.to_web`)* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *AG-UI Protocol* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Vercel AI SDK* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Model Providers**
  - *OpenAI & OpenAI-compatible* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Anthropic & Bedrock* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Google (Gemini)* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Mistral, Groq, Cohere* — [Module](00-misc/NOT_IMPLEMENTED.md)

### Tools & Extensions 🧰

Tooling for capabilities that extend agent behavior and enable retrieval, search, and runtime features.

- **Function Tools**
  - `@agent.tool` / `@agent.tool_plain` — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Dynamic Tools (prepare)* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Human-in-the-loop (Approval)* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Built-in Tools**
  - *Web Search* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Code Execution* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Image Generation* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *File Search (RAG)* — [Module](00-misc/NOT_IMPLEMENTED.md)

- **Model Context Protocol (MCP)**
  - *MCPServer (Stdio, SSE, HTTP)* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *Sampling & Elicitation* — [Module](00-misc/NOT_IMPLEMENTED.md)
  - *FastMCP Integration* — [Module](00-misc/NOT_IMPLEMENTED.md)
