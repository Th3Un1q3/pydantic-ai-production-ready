---
description: Learn how to build your first type-safe agent with Pydantic AI. This lesson covers the basics of the Agent primitive, structured output validation, tool integration, and context management.
tags:
  - status:published
  - verified:false
  - TODO
references:
    previous: "./02-setup.md"
    next: "../02-core-concepts/README.md"
---

# Building Your First Type-Safe Agent

In this lesson, we will instantiate the `Agent` class—the core orchestration primitive in Pydantic AI—and progressively add type safety, asynchronous capabilities, and context awareness.

## The Agent Primitive

The `Agent` component manages the lifecycle of the LLM interaction, including:

1. State management (chat history)
2. Tool execution and recursion
3. Result validation
4. Dependency injection

### Minimal Implementation

At its simplest, an agent wraps a model string and returns unstructured text.

```python
import asyncio
from pydantic_ai import Agent

# Create an agent instance bonded to a specific model
agent = Agent('openai:gpt-4')

async def main():
    # Asynchronous execution is the default and recommended pattern
    result = await agent.run('What is the capital of France?')
    print(result.output)
    # Output: "The capital of France is Paris."

if __name__ == "__main__":
    asyncio.run(main())
```

> **Note:** While `agent.run_sync()` exists for scripts and prototyping, enterprise applications should almost exclusively use `await agent.run()` to prevent blocking the event loop in high-throughput environments (e.g., FastAPI).

## Structured Output (The Validation Layer)

The true power of Pydantic AI lies in `output_type`. By defining a Pydantic model for the output, you enforce a strict contract on the LLM's response. This is effectively a "runtime unit test" for the model's output.

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class CityInfo(BaseModel):
    name: str
    country: str
    population: int
    famous_for: list[str]

agent = Agent(
    'openai:gpt-4',
    output_type=CityInfo, # <--- The Contract
    system_prompt='Extract city information from user queries.',
)

async def main():
    result = await agent.run('Tell me about Paris')

    # The result.output is guaranteed to be a valid CityInfo instance
    # No more `json.loads()` or rigorous error checking needed here
    print(f"City: {result.output.name}")
    print(f"Country: {result.output.country}")

import asyncio
asyncio.run(main())
```

## Agent with Tools

Give your agent the ability to call functions:

```python
from pydantic_ai import Agent, RunContext

# Create an agent
agent = Agent('openai:gpt-4')

@agent.tool
async def get_weather(ctx: RunContext[None], city: str) -> str:
    """Get the current weather for a city.

    Args:
        ctx: The run context
        city: The name of the city

    Returns:
        Weather information as a string
    """
    # In a real application, you'd call a weather API
    # For now, we'll return mock data
    return f"The weather in {city} is sunny and 72°F"

# The agent can now call the get_weather tool
result = agent.run_sync('What is the weather like in Paris?')
print(result.output)
# The agent will call get_weather('Paris') and incorporate the result
```

## Agent with Context

Pass context/state through your agent runs:

```python
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

@dataclass
class UserContext:
    user_id: int
    username: str

agent = Agent('openai:gpt-4', deps_type=UserContext)

@agent.tool
async def get_user_preferences(ctx: RunContext[UserContext]) -> str:
    """Get preferences for the current user."""
    user = ctx.deps
    # In a real app, fetch from database
    return f"User {user.username} prefers concise responses"

# Run with context
user = UserContext(user_id=123, username="alice")
result = agent.run_sync('Give me a summary', deps=user)
```

## Practical Example: Customer Support Bot

Let's build a more realistic example:

```python
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass

class SupportTicket(BaseModel):
    category: str
    priority: str  # 'low', 'medium', 'high', 'urgent'
    summary: str
    requires_human: bool

@dataclass
class SupportContext:
    customer_id: str
    ticket_history: list[str]

agent = Agent(
    'openai:gpt-4',
    output_type=SupportTicket,
    deps_type=SupportContext,
    system_prompt='''You are a customer support AI assistant.
    Analyze customer inquiries and create support tickets.
    Escalate to humans when necessary.'''
)

@agent.tool
async def check_order_status(ctx: RunContext[SupportContext], order_id: str) -> str:
    """Check the status of a customer order."""
    # Mock implementation
    return f"Order {order_id} is being shipped"

@agent.tool
async def get_customer_history(ctx: RunContext[SupportContext]) -> str:
    """Get customer's previous interactions."""
    return f"Previous tickets: {len(ctx.deps.ticket_history)}"

# Use the agent
async def handle_support_request(message: str, customer_id: str):
    context = SupportContext(
        customer_id=customer_id,
        ticket_history=[]
    )

    result = await agent.run(message, deps=context)
    ticket = result.output

    print(f"Category: {ticket.category}")
    print(f"Priority: {ticket.priority}")
    print(f"Summary: {ticket.summary}")
    print(f"Needs human: {ticket.requires_human}")

    return ticket

# Example usage
import asyncio
asyncio.run(handle_support_request(
    "I ordered a laptop 2 weeks ago and still haven't received it!",
    customer_id="CUST-123"
))
```

## Best Practices

1. **Use Type Hints**: Always specify types for better validation
2. **System Prompts**: Provide clear instructions for your agent's behavior
3. **Error Handling**: Wrap agent calls in try-except blocks
4. **Async by Default**: Use async/await for better performance
5. **Tool Documentation**: Write clear docstrings for tools (the LLM reads them!)

## Common Patterns

### Retry Logic

```python
from pydantic_ai import Agent

agent = Agent(
    'openai:gpt-4',
    retries=3,  # Retry failed calls
)
```

### Model Selection

```python
# Different models for different tasks
cheap_agent = Agent('openai:gpt-3.5-turbo')  # Fast and cheap
smart_agent = Agent('openai:gpt-4')          # More capable
local_agent = Agent('ollama:llama2')         # Local/private
```

## Exercises

Try these exercises to practice:

1. **Simple Q&A Agent**: Create an agent that answers questions about a specific topic
2. **Data Extractor**: Build an agent that extracts structured data from text
3. **Calculator Agent**: Create an agent with tools for basic math operations
4. **Multi-Tool Agent**: Build an agent with multiple tools that it can choose between

## Next Steps

Module 02 is planned and will be implemented later from its specification. For now, keep this placeholder forward link: [Module 02: Core Concepts (planned)](../02-core-concepts/README.md).

## Resources

- [Pydantic AI Agents Documentation](https://ai.pydantic.dev/agents/)
- [Pydantic AI Tools Documentation](https://ai.pydantic.dev/tools/)
- [Reference Package: course-navigator](../../packages/course-navigator/README.md)
