# Core Concepts

Deep dive into Pydantic AI's core components and patterns.

## Learning Objectives

By the end of this module, you will:

- Understand agent architecture in depth
- Master different model providers
- Implement and use tools effectively
- Work with structured outputs and validation
- Handle context and dependencies

## Lessons

1. Agents Deep Dive
2. Working with Models
3. Tool Calling and Function Execution
4. Structured Outputs with Pydantic
5. Context and Dependencies

## Exercises

Complete the exercises in the `exercises/` directory.

## Evaluations ✅

Evaluations serve not only as sanity checks but as essential learning signals. They help you understand how changes to prompts, tool descriptions, outputs, and context management affect system performance — enabling informed design decisions instead of guesswork.

- **Purpose:** Measure, compare, and iterate on agent behavior and tool outputs. 💡
- **Types:** Automated metrics (accuracy, F1), human evaluations (ratings, pairwise comparisons), and ablation studies to isolate effects.
- **Setup:** Define hypotheses, pick clear metrics, create representative scenarios, run experiments reproducibly, and record results.
- **Practices:** Use structured outputs for easier scoring, version prompts and tool descriptions, keep an evaluation changelog, and automate runs when possible.
- **Example exercise:** Create two prompt variants for the "Tool Calling" lesson, run them over 10 scenarios, score outputs with a simple rubric, and save findings to `learning/reports/` with recommendations.
- **Example Decisions:**
  - **Contextual compression:** Compare limiting message history vs. compressing context via prompt to understand performance impact.
  - **Model selection:** Evaluate different model providers to see how they affect task success rates.
  - **Prompt engineering:** Learn how changes to the prompt impact the performance of the system.
  - **Tool optimization:** Learn how changes to tool descriptions and outputs impact performance.
  - **Output formats:** Determine which structured output formats yield the best results for specific tasks.
  - **Generation configurations:** Assess how different generation settings (e.g., temperature, max tokens) influence output quality.
  - **Context management:** Make meaningful design decisions about context management based on data rather than guessing.

> **Note:** Use evaluations iteratively — small experiments and clear metrics lead to better, faster design decisions.

## Estimated Time

4-5 hours

## Prerequisites

- Completed Module 01: Fundamentals
- Understanding of Python type hints
- Basic async/await knowledge
