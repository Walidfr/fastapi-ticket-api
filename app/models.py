"""
SQLAlchemy models for the Ticket API.
Defines TicketStatus enum and Ticket table.
"""

from sqlalchemy import Column, String, DateTime, Enum
import uuid
from sqlalchemy.sql import func
import enum
from .database import Base


class TicketStatus(str, enum.Enum):
    """
    Enum for ticket status values.
    Values: open, stalled, closed.
    """
    open = "open"
    stalled = "stalled"
    closed = "closed"


class Ticket(Base):
    """
    SQLAlchemy model for a ticket.
    Fields:
        id (str): UUID string, primary key
        title (str): Ticket title
        description (str): Ticket description
        status (TicketStatus): Status enum
        created_at (datetime): Creation timestamp
    """
    __tablename__ = "tickets"
    id = Column(
        String, primary_key=True, index=True,
        default=lambda: str(uuid.uuid4())
    )
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(
        Enum(TicketStatus), default=TicketStatus.open, nullable=False
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
