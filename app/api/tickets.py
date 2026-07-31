from fastapi import APIRouter
from app.models.ticket import Ticket
from app.services.ticket_service import (
    create_ticket,
    get_tickets
)

router = APIRouter()

@router.post("/tickets")
def add_ticket(ticket: Ticket):
    return create_ticket(ticket)

@router.get("/tickets")
def fetch_tickets():
    return get_tickets()
  
