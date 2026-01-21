# Exercises: Fundamentals

Complete these exercises to practice what you've learned in the fundamentals module.

## Prerequisites

- Completed reading all lessons in this module
- Development environment set up
- Basic Python knowledge

## Exercise 1: Simple Q&A Agent

**Objective**: Create an agent that answers questions about Python

**Tasks**:
1. Create a new file `exercise1_qa_agent.py`
2. Create an agent with a system prompt that makes it a Python expert
3. Ask it 3 questions about Python
4. Print the responses

**Starter Code**:
```python
from pydantic_ai import Agent
import asyncio

async def main():
    # TODO: Create agent with appropriate system prompt
    # TODO: Ask questions and print responses
    pass

if __name__ == "__main__":
    asyncio.run(main())
```

**Expected Output**:
```
Q: What is a list comprehension?
A: [Agent's detailed answer]
...
```

## Exercise 2: Data Extractor

**Objective**: Extract structured data from text

**Tasks**:
1. Create a new file `exercise2_extractor.py`
2. Define a Pydantic model for a Book (title, author, year, genre)
3. Create an agent that extracts Book information from text
4. Test with sample book descriptions

**Starter Code**:
```python
from pydantic import BaseModel
from pydantic_ai import Agent

class Book(BaseModel):
    # TODO: Define fields
    pass

# TODO: Create agent
# TODO: Test with sample text
```

**Test Data**:
```
"The Great Gatsby by F. Scott Fitzgerald, published in 1925, is a classic American novel."
"1984 is a dystopian novel written by George Orwell in 1949."
```

## Exercise 3: Calculator Agent

**Objective**: Create an agent with math tools

**Tasks**:
1. Create a new file `exercise3_calculator.py`
2. Define tools for: add, subtract, multiply, divide
3. Create an agent that can use these tools
4. Ask the agent to perform calculations

**Starter Code**:
```python
from pydantic_ai import Agent, RunContext

agent = Agent('openai:gpt-4')

@agent.tool
async def add(ctx: RunContext[None], a: float, b: float) -> float:
    """Add two numbers."""
    # TODO: Implement
    pass

# TODO: Add more tools (subtract, multiply, divide)

# TODO: Test the agent
```

**Test Queries**:
```
"What is 15 plus 27?"
"Multiply 8 by 9"
"What is 100 divided by 4?"
```

## Exercise 4: Weather Agent (Mock)

**Objective**: Create an agent that provides weather information using a mock tool

**Tasks**:
1. Create a new file `exercise4_weather.py`
2. Create a tool that returns mock weather data
3. Create an agent that can check weather for cities
4. Handle queries about weather in different cities

**Starter Code**:
```python
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass

@dataclass
class WeatherContext:
    default_city: str = "New York"

agent = Agent('openai:gpt-4', deps_type=WeatherContext)

@agent.tool
async def get_weather(ctx: RunContext[WeatherContext], city: str) -> str:
    """Get weather for a city (mock data)."""
    # TODO: Return mock weather data
    # e.g., "Sunny, 72°F" for different cities
    pass

# TODO: Test the agent
```

## Exercise 5: Multi-Tool Agent

**Objective**: Combine multiple tools in one agent

**Tasks**:
1. Create a new file `exercise5_multi_tool.py`
2. Create an agent with at least 3 different tools
3. Tools can include: time, date, random number, coin flip, etc.
4. Test the agent with queries that require different tools

**Example Tools**:
- `get_current_time()`: Returns current time
- `get_random_number(min, max)`: Returns random number
- `flip_coin()`: Returns "heads" or "tails"

**Bonus Challenge**:
- Add error handling for invalid inputs
- Add a tool that requires context from a previous tool call
- Implement rate limiting or usage tracking

## Submission

For each exercise:
1. Create the file in this `exercises/` directory
2. Test your code
3. Add comments explaining your implementation
4. Optional: Add type hints and docstrings

## Solutions

Solutions are available in `exercises/solutions/` directory, but try to complete the exercises on your own first!

## Need Help?

- Review the lesson material
- Check the example code in `/projects/src/examples/`
- Refer to [Pydantic AI documentation](https://ai.pydantic.dev/)
- Ask questions in GitHub Discussions

Good luck! 🚀
