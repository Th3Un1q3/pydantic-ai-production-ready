"""Tests for internal support agent."""
import pytest


def test_basic():
    """Test basic import."""
    import src
    assert hasattr(src, "__version__")


@pytest.mark.asyncio
async def test_support_ticket_structure():
    """Test that SupportTicket model works."""
    from src.agent import SupportTicket
    
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
