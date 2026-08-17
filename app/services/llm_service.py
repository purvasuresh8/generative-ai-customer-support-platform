from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.services.retrieval_service import RetrievalService

client = OpenAI(api_key=OPENAI_API_KEY)

retriever = RetrievalService()


def generate_response(message: str):

    context = retriever.retrieve(message)

    prompt = f"""
You are a professional customer support assistant.

Use ONLY the provided context when answering.

Context:
{chr(10).join(context)}

Customer Query:
{message}

Answer professionally and clearly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
    