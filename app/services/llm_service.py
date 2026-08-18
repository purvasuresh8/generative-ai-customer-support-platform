import ollama
from app.services.retrieval_service import RetrievalService

retriever = RetrievalService()

def generate_response(message: str):

    context = retriever.retrieve(message)

    prompt = f"""
You are a professional customer support assistant.

Support Knowledge:
{chr(10).join(context)}

Customer Query:
{message}

Answer professionally and clearly.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]