from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.tickets import router as ticket_router
from app.api.feedback import router as feedback_router

app = FastAPI(
    title="Generative AI Customer Support Platform"
)

app.include_router(chat_router)
app.include_router(ticket_router)
app.include_router(feedback_router)

@app.get("/")
def health_check():
    return {
        "status": "healthy"
    }
  
