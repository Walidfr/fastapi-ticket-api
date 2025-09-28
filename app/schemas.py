"""
Pydantic schemas for Ticket API requests and responses.
Defines validation and serialization models.
"""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
import enum


class TicketStatus(str, enum.Enum):
    """
    Enum for ticket status values.
    Values: open, stalled, closed.
    """
    open = "open"
    stalled = "stalled"
    closed = "closed"


class TicketBase(BaseModel):
    """
    Base schema for ticket creation and update.
    Fields:
        title (str): Ticket title
        description (str): Ticket description
    """
    title: str
    description: str


class TicketCreate(TicketBase):
    """
    Schema for creating a ticket.
    Inherits title and description from TicketBase.
    """
    pass


class TicketUpdate(BaseModel):
    """
    Schema for updating a ticket.
    All fields are optional.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TicketStatus] = None


class TicketOut(TicketBase):
    """
    Schema for ticket response.
    Fields:
        id (str): Ticket UUID
        status (TicketStatus): Status enum
        created_at (datetime): Creation timestamp
    """
    id: str = Field(..., description="Ticket UUID")
    status: TicketStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
