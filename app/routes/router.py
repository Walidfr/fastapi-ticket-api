"""
FastAPI APIRouter for ticket endpoints.
Defines all REST API routes for ticket management.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()


def get_db():
    """
    Dependency to get a SQLAlchemy session.
    Yields:
        Session: SQLAlchemy session.
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tickets/", response_model=schemas.TicketOut, status_code=201)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    """
    Create a new ticket.
    Args:
        ticket (TicketCreate): Request body for ticket creation.
        db (Session): SQLAlchemy session (dependency).
    Returns:
        TicketOut: Created ticket response.
    """
    return crud.create_ticket(db, ticket)


@router.get("/tickets/", response_model=list[schemas.TicketOut])
def list_tickets(db: Session = Depends(get_db)):
    """
    List all tickets.
    Args:
        db (Session): SQLAlchemy session (dependency).
    Returns:
        List[TicketOut]: List of tickets.
    """
    return crud.get_tickets(db)


@router.get("/tickets/{ticket_id}", response_model=schemas.TicketOut)
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    """
    Get a ticket by UUID.
    Args:
        ticket_id (str): Ticket UUID.
        db (Session): SQLAlchemy session (dependency).
    Returns:
        TicketOut: Ticket response.
    Raises:
        HTTPException: 404 if not found.
    """
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.put("/tickets/{ticket_id}", response_model=schemas.TicketOut)
def update_ticket(ticket_id: str, ticket_update: schemas.TicketUpdate,
                  db: Session = Depends(get_db)):
    """
    Update a ticket by UUID.
    Args:
        ticket_id (str): Ticket UUID.
        ticket_update (TicketUpdate): Fields to update.
        db (Session): SQLAlchemy session (dependency).
    Returns:
        TicketOut: Updated ticket response.
    Raises:
        HTTPException: 404 if not found.
    """
    ticket = crud.update_ticket(db, ticket_id, ticket_update)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.patch("/tickets/{ticket_id}/close", response_model=schemas.TicketOut)
def close_ticket(ticket_id: str, db: Session = Depends(get_db)):
    """
    Close a ticket by setting its status to closed.
    Args:
        ticket_id (str): Ticket UUID.
        db (Session): SQLAlchemy session (dependency).
    Returns:
        TicketOut: Closed ticket response.
    Raises:
        HTTPException: 404 if not found.
    """
    ticket = crud.close_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
