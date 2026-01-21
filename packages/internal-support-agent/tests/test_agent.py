"""Tests for internal support agent."""
import pytest


def test_basic():
    """Test basic import."""
    from internal_support_agent import agent
    assert hasattr(agent, "InternalSupportAgent")


@pytest.mark.asyncio
async def test_support_ticket_structure():
    """Test that SupportTicket model works."""
    from internal_support_agent.agent import SupportTicket
    
    ticket = SupportTicket(
        title="Test Ticket",
        category="IT",
        priority="high",
        description="Test description",
        suggested_action="Test action",
        requires_escalation=True
    )
    
    assert ticket.title == "Test Ticket"
    assert ticket.priority == "high"
    assert ticket.requires_escalation is True
