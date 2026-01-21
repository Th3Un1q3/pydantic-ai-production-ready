"""
Corporate Agentic System - Orchestrator

This module implements a multi-agent orchestrator for corporate tasks.
Uses Anthropic's Claude by default for enhanced reasoning.
"""
import asyncio
import os
from typing import List, Dict
from dataclasses import dataclass

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from loguru import logger

# Import from shared package
try:
    from pydantic_ai_shared.config import get_default_model
except ImportError:
    # Fallback for development
    import sys
    sys.path.insert(0, "../../shared/src")
    from config import get_default_model


class Task(BaseModel):
    """A corporate task."""
    title: str
    description: str
    assigned_agent: str
    priority: int = Field(ge=1, le=5)
    estimated_time: str


class WorkflowResult(BaseModel):
    """Result of workflow execution."""
    status: str
    tasks_completed: List[str]
    summary: str
    next_steps: List[str] = Field(default_factory=list)


@dataclass
class CorporateContext:
    """Context for corporate operations."""
    user_role: str
    department: str
    access_level: str = "standard"


class CorporateOrchestrator:
    """Orchestrator for corporate agentic system."""
    
    def __init__(self, model: str = None):
        """Initialize the orchestrator.
        
        Args:
            model: The model to use (defaults to configured Anthropic model for corporate use)
        """
        if model is None:
            # Default to Anthropic for corporate use (enhanced reasoning)
            model = get_default_model("anthropic")
            
        self.planner = Agent(
            model,
            result_type=WorkflowResult,
            deps_type=CorporateContext,
            system_prompt="""You are a corporate workflow planning AI.
            Analyze requests and break them into actionable tasks.
            Consider company policies, priorities, and resource availability.
            Delegate tasks to appropriate specialized agents."""
        )
        logger.info(f"Corporate orchestrator initialized with {model}")
    
    async def plan_workflow(
        self, 
        request: str, 
        context: CorporateContext
    ) -> WorkflowResult:
        """Plan a workflow for a corporate request.
        
        Args:
            request: The corporate request or task
            context: User and organizational context
            
        Returns:
            Planned workflow with tasks
        """
        logger.info(f"Planning workflow for: {request[:50]}...")
        result = await self.planner.run(request, deps=context)
        logger.info(f"Workflow planned: {result.data.status}")
        return result.data


async def main():
    """Demo the corporate agentic system."""
    # This example works without API keys by demonstrating structure
    print("=" * 70)
    print("Corporate Agentic System Demo")
    print("=" * 70)
    print("\n📋 System Architecture:")
    print("   - Planning Agent: Analyzes and breaks down requests")
    print("   - Document Agent: Handles document processing")
    print("   - Scheduling Agent: Manages meetings and calendars")
    print("   - Analytics Agent: Provides data insights")
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n⚠️  Set ANTHROPIC_API_KEY to run live demo")
        print("💡 This system uses Claude for enhanced reasoning")
        return
    
    orchestrator = CorporateOrchestrator()
    context = CorporateContext(
        user_role="manager",
        department="engineering",
        access_level="elevated"
    )
    
    # Example request
    request = """Prepare for our quarterly business review:
    1. Analyze last quarter's metrics
    2. Schedule meetings with team leads
    3. Compile status reports from all projects
    4. Create presentation slides"""
    
    print(f"\n📬 Corporate Request:")
    print(f"   {request}")
    
    workflow = await orchestrator.plan_workflow(request, context)
    
    print(f"\n✅ Workflow Status: {workflow.status}")
    print(f"\n📊 Tasks:")
    for task in workflow.tasks_completed:
        print(f"   - {task}")
    
    print(f"\n📝 Summary:")
    print(f"   {workflow.summary}")
    
    if workflow.next_steps:
        print(f"\n➡️  Next Steps:")
        for step in workflow.next_steps:
            print(f"   - {step}")


if __name__ == "__main__":
    asyncio.run(main())
