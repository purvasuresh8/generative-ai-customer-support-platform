from app.services.retrieval_service import RetrievalService

def test_retrieve():

    service = RetrievalService()

    docs = service.retrieve(
        "How do I reset my password?"
    )

    assert len(docs) > 0
    