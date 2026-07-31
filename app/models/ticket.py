from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    customer_name: str
    issue: str
    status: str = "open"
