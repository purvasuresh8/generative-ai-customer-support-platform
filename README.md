# Generative AI Customer Support Platform

An AI-powered customer support platform built with FastAPI, OpenAI, Docker, and REST APIs.

## Features

- AI-powered support assistant
- Ticket management
- Feedback collection
- Response evaluation
- Dockerized deployment

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker

```bash
docker-compose up --build
```

## API Docs

```text
http://localhost:8000/docs
```

### Retrieval Experiments

The platform includes experiments comparing:

- BM25 keyword search
- Dense vector retrieval using sentence embeddings
- Hybrid retrieval approaches

Results showed that hybrid retrieval produced the most relevant context for customer-support question answering and improved overall answer quality.

