from fastapi import APIRouter

router = APIRouter()

feedback_store = []

@router.post("/feedback")
def submit_feedback(feedback: dict):

    feedback_store.append(feedback)

    return {
        "message": "Feedback received"
    }
  
