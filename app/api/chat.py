from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.llm_service import generate_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    response = generate_response(request.message)

    return {
        "response": response
    }
    