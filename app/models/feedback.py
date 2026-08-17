from pydantic import BaseModel

class Feedback(BaseModel):
    question: str
    response: str
    rating: int
    comment: str | None = None
    