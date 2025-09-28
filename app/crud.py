"""
CRUD operations for Ticket model.
Each function interacts with the database session and returns SQLAlchemy model
instances or None.
"""

from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional


def create_ticket(db: Session, ticket: schemas.TicketCreate) -> models.Ticket:
    """
    Create a new ticket in the database.
    Args:
        db (Session): SQLAlchemy session.
        ticket (TicketCreate): Pydantic model for ticket creation.
    Returns:
        Ticket: The created Ticket SQLAlchemy model.
    """
    db_ticket = models.Ticket(
        **ticket.model_dump()
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_ticket(db: Session, ticket_id: str) -> Optional[models.Ticket]:
    """
    Retrieve a ticket by its UUID.
    Args:
        db (Session): SQLAlchemy session.
        ticket_id (str): UUID of the ticket.
    Returns:
        Optional[Ticket]: The Ticket model or None if not found.
    """
    return db.query(models.Ticket).filter(
        models.Ticket.id == ticket_id
    ).first()


def get_tickets(db: Session) -> List[models.Ticket]:
    """
    List all tickets in the database.
    Args:
        db (Session): SQLAlchemy session.
    Returns:
        List[Ticket]: List of Ticket models.
    """
    return db.query(models.Ticket).all()


def update_ticket(
    db: Session,
    ticket_id: str,
    ticket_update: schemas.TicketUpdate
) -> Optional[models.Ticket]:
    """
    Update a ticket's fields.
    Args:
        db (Session): SQLAlchemy session.
        ticket_id (str): UUID of the ticket.
        ticket_update (TicketUpdate): Pydantic model with fields to update.
    Returns:
        Optional[Ticket]: The updated Ticket model or None if not found.
    """
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        return None
    for field, value in ticket_update.model_dump(exclude_unset=True).items():
        setattr(ticket, field, value)
    db.commit()
    db.refresh(ticket)
    return ticket


def close_ticket(db: Session, ticket_id: str) -> Optional[models.Ticket]:
    """
    Set a ticket's status to closed.
    Args:
        db (Session): SQLAlchemy session.
        ticket_id (str): UUID of the ticket.
    Returns:
        Optional[Ticket]: The updated Ticket model or None if not found.
    """
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        return None
    ticket.status = models.TicketStatus.closed
    db.commit()
    db.refresh(ticket)
    return ticket
