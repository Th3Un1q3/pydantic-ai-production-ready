"""Tests for corporate agentic system."""
import pytest


def test_basic():
    """Test basic import."""
    from corporate_agentic_system import orchestrator
    assert hasattr(orchestrator, "CorporateOrchestrator")


@pytest.mark.asyncio
async def test_workflow_result_structure():
    """Test that WorkflowResult model works."""
    from corporate_agentic_system.orchestrator import WorkflowResult
    
    result = WorkflowResult(
        status="planned",
        tasks_completed=["task1", "task2"],
        summary="Test summary",
        next_steps=["step1", "step2"]
    )
    
    assert result.status == "planned"
    assert len(result.tasks_completed) == 2
    assert len(result.next_steps) == 2
