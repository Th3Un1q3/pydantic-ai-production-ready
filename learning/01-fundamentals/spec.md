# Specification for Learning Fundamentals

## Overview

This module introduces the transition from relying on external tools to developing in-house agentic systems. It focuses on building a production-ready internal application while demonstrating key concepts through hands-on implementation.

## Goal

- Explain the process and benefits of transitioning to in-house development of agentic applications
- Build a realistic first internal application that matches the typical starting point for companies
- Demonstrate fundamental concepts with production-level code quality
- Emphasize evaluation-first principles as essential for building reliable systems

## Key Principles

- **Evaluation First**: Similar to Test-Driven Development (TDD), evaluation is the foundation of any production-ready agentic system. Without proper evaluation, systems cannot be trusted or improved. The evaluation lifecycle includes: defining test cases with inputs and expected outputs, creating custom evaluators for specific assessment logic, building datasets that combine cases and evaluators, running evaluations to generate reports, and analyzing results to iterate on the system. Key principles for evaluations include systematic testing, combining multiple evaluators for comprehensive assessment, using metrics and attributes for deeper insights, and ensuring evaluations are automated and run before deployment.
- **Production-Level Quality**: Avoid surface-level implementations. Use proper testing, code structure, and deployment practices.
- **Realistic Applications**: Focus on applications that companies actually need as their first in-house developments.

## Project: Internal Support Chatbot

Build a simple chatbot application for internal support, such as:

- Handling common IT helpdesk queries
- Routing requests to appropriate departments
- Providing basic troubleshooting guidance
- Escalating complex issues
- Providing a user interface for interaction (e.g., command-line or web-based chat)

This represents a typical first in-house application that many companies develop when transitioning to agentic systems, as it provides immediate value while being manageable in scope.

## Requirements

- No notebooks - implement real code with proper structure
- Comprehensive tests and evaluation suites
- Production-ready code organization (src/, tests/, etc.)
- Clear documentation and setup instructions
- Evaluation metrics and automated testing

## Concepts to Include

- Basic agent architecture and components
- Prompt engineering fundamentals
- Evaluation frameworks and metrics
- Testing strategies for agentic systems
- Code organization and best practices
- Deployment and monitoring basics
- Basic user interface implementation for agent interactions
- Evaluation lifecycle and principles (defining cases, evaluators, datasets, running evaluations, analyzing reports)

## Relevant References from Learning Materials

This module aligns with the **AI Adoption Journey** described in the [main learning README](../README.md), specifically Phase 2: Strategic Adoption, focusing on "Build Internal Apps (Learning & Expertise)" as the transition point for in-house development.

Key concepts from the [Concepts Index](../CONCEPTS.md) covered in this module:

- **Agents**: Dependencies (`deps_type`), Structured Output (`output_type`), System Prompts & Instructions, Model Selection
- **Running & Execution**: `run()` / `run_sync()` - basic execution primitives
- **Messages & History**: ModelRequest & ModelResponse, Conversation Continuity (`message_history`)
- **Evaluations**: `pydantic-evals` framework with `Dataset`, `Case`, and `Evaluator` classes for systematic testing
- **Harnessing LLMs**: Best practices for working with large language models
- **Interfaces**: CLI (clai), Web Chat UI (`Agent.to_web`) - basic user interaction implementations

### References from Pydantic AI Documentation

- **Agent Class**: Core component for creating AI agents, initialized with model (e.g., 'openai:gpt-4o') and instructions
- **Execution Methods**: `run()` (async) and `run_sync()` for running agent interactions
- **Tools**: Function tools via `@agent.tool` decorator, builtin tools like `CodeExecutionTool`, `WebFetchTool`
- **Structured Outputs**: Using `output_type` parameter with Pydantic models for type-safe responses
- **User Interfaces**: `Agent.to_web()` method for built-in web chat interface
- **Evaluations**: `pydantic-evals` framework with `Dataset`, `Case`, and `Evaluator` classes for systematic testing

## Structure

- `src/`: Main application code
- `tests/`: Unit and integration tests
- `evaluations/`: Evaluation scripts and metrics
- `README.md`: Setup and usage instructions
- `requirements.txt` or `pyproject.toml`: Dependencies
