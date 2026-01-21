"""
Example: Simple Chatbot Agent

This example demonstrates a basic chatbot using Pydantic AI.
"""
import asyncio
import os

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from loguru import logger

from .config import get_default_model


class ChatMessage(BaseModel):
    """A chat message structure."""
    role: str
    content: str


class ChatbotExample:
    """A simple chatbot example using Pydantic AI."""
    
    def __init__(self, model: str = None):
        """Initialize the chatbot.
        
        Args:
            model: The model to use (defaults to configured OpenAI model)
        """
        if model is None:
            model = get_default_model("openai")
        
        self.agent = Agent(
            model,
            system_prompt="""You are a helpful assistant. 
            Provide concise, accurate responses. 
            Be friendly and professional."""
        )
        logger.info(f"Chatbot initialized with model: {model}")
    
    async def chat(self, message: str) -> str:
        """Send a message and get a response.
        
        Args:
            message: The user's message
            
        Returns:
            The agent's response
        """
        logger.debug(f"User message: {message}")
        result = await self.agent.run(message)
        logger.debug(f"Agent response: {result.data}")
        return result.data


async def main():
    """Run the chatbot example."""
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        logger.warning("OPENAI_API_KEY not set. Using mock mode.")
        print("Note: Set OPENAI_API_KEY environment variable to use real API")
        return
    
    chatbot = ChatbotExample()
    
    # Example conversations
    examples = [
        "Hello! How are you?",
        "What is Python?",
        "Can you help me with coding?",
    ]
    
    print("=" * 60)
    print("Simple Chatbot Example")
    print("=" * 60)
    
    for message in examples:
        print(f"\n👤 User: {message}")
        response = await chatbot.chat(message)
        print(f"🤖 Bot: {response}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
