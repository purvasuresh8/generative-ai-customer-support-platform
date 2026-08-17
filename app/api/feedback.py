from fastapi import APIRouter
from app.models.feedback import Feedback
from app.services.evaluation_service import EvaluationService

router = APIRouter()

feedback_store = []

@router.post("/feedback")
def submit_feedback(feedback: Feedback):

    feedback_store.append(
        feedback.model_dump()
    )

    return {
        "message": "Feedback received"
    }

@router.get("/feedback/metrics")
def get_metrics():

    return {
        "feedback_count": len(feedback_store),
        "average_rating":
            EvaluationService.average_rating(
                feedback_store
            ),
        "positive_feedback_rate":
            EvaluationService.positive_feedback_rate(
                feedback_store
            )
    }
    