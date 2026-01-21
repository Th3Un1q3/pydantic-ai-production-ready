"""
Internal Support Agent - Main Module

This module implements an AI agent for internal company support.
"""
import asyncio
import os
from typing import List

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from loguru import logger


class SupportTicket(BaseModel):
    """Support ticket structure."""
    title: str
    category: str  # "IT", "HR", "Finance", "General"
    priority: str  # "low", "medium", "high", "urgent"
    description: str
    suggested_action: str
    requires_escalation: bool = False


class InternalSupportAgent:
    """AI agent for internal support queries."""
    
    def __init__(self, model: str = "openai:gpt-4"):
        """Initialize the support agent.
        
        Args:
            model: The model to use
        """
        self.agent = Agent(
            model,
            result_type=SupportTicket,
            system_prompt="""You are an internal company support AI assistant.
            Help employees with:
            - IT issues (password resets, access requests, software problems)
            - HR questions (policies, benefits, time off)
            - General company information
            
            Create structured support tickets from employee queries.
            Prioritize based on urgency and impact.
            Escalate complex or sensitive issues."""
        )
        logger.info(f"Internal support agent initialized with {model}")
    
    async def process_query(self, query: str) -> SupportTicket:
        """Process an employee support query.
        
        Args:
            query: The employee's question or issue
            
        Returns:
            A structured support ticket
        """
        logger.info(f"Processing query: {query[:50]}...")
        result = await self.agent.run(query)
        logger.info(f"Created ticket: {result.data.title}")
        return result.data


async def main():
    """Demo the internal support agent."""
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Set OPENAI_API_KEY environment variable to run this example")
        return
    
    agent = InternalSupportAgent()
    
    # Example queries
    queries = [
        "I can't access the shared drive and need files for a client meeting in 1 hour",
        "What is our company's policy on remote work?",
        "My laptop keeps freezing when I open multiple applications",
    ]
    
    print("=" * 70)
    print("Internal Support Agent Demo")
    print("=" * 70)
    
    for query in queries:
        print(f"\n📩 Employee Query:")
        print(f"   {query}")
        
        ticket = await agent.process_query(query)
        
        print(f"\n🎫 Support Ticket Created:")
        print(f"   Title: {ticket.title}")
        print(f"   Category: {ticket.category}")
        print(f"   Priority: {ticket.priority}")
        print(f"   Action: {ticket.suggested_action}")
        print(f"   Escalate: {'Yes' if ticket.requires_escalation else 'No'}")
        print("-" * 70)


if __name__ == "__main__":
    asyncio.run(main())
