# Generative AI Customer Support Platform

A Generative AI-powered customer support platform built with **FastAPI**, **Python**, and **Ollama-hosted large language models**. The platform provides context-aware question answering by retrieving relevant support knowledge, enriching prompts with retrieved context, and generating grounded responses through a Retrieval-Augmented Generation (RAG) workflow.

---

## Features

- LLM-powered customer support assistant
- Context-aware question answering using Retrieval-Augmented Generation (RAG)
- Document ingestion and preprocessing pipeline
- Keyword-based document retrieval and ranking
- Prompt engineering for grounded response generation
- Feedback collection and evaluation framework
- Retrieval experimentation and performance comparison
- REST APIs built with FastAPI
- Dockerized deployment
- Automated document-processing workflows

---

## Architecture

```text
Raw Documents
      │
      ▼
Document Ingestion Pipeline
      │
      ▼
Document Cleaning & Validation
      │
      ▼
Processed Knowledge Base
      │
      ▼
Retrieval Service
      │
      ▼
Document Ranking
      │
      ▼
Prompt Construction
      │
      ▼
Ollama LLM
      │
      ▼
Context-Aware Response
```

---

## Project Structure

```text
generative-ai-customer-support-platform/
│
├── app/
│   ├── api/
│   │   ├── chat.py
│   │   ├── feedback.py
│   │   └── tickets.py
│   │
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── retrieval_service.py
│   │   ├── evaluation_service.py
│   │   └── ticket_service.py
│   │
│   ├── ingestion/
│   │   ├── document_loader.py
│   │   ├── document_cleaner.py
│   │   ├── ingestion_pipeline.py
│   │   └── pyspark_pipeline.py
│   │
│   └── models/
│       ├── chat.py
│       ├── feedback.py
│       └── ticket.py
│
├── scripts/
│   ├── ingest_documents.py
│   └── run_pipeline.py
│
├── experiments/
│   ├── keyword_search_test.py
│   ├── scoring_test.py
│   └── results.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Retrieval-Augmented Generation (RAG)

The platform implements a lightweight Retrieval-Augmented Generation workflow:

1. Documents are ingested from organizational knowledge sources.
2. Documents are cleaned and preprocessed.
3. Relevant documents are retrieved using ranking-based retrieval.
4. Retrieved content is added to the LLM prompt as contextual knowledge.
5. The language model generates grounded customer-support responses.

### Workflow

```text
Customer Question
        ↓
Document Retrieval
        ↓
Document Ranking
        ↓
Prompt Enrichment
        ↓
LLM Response Generation
```

---

## Document Ingestion Pipeline

The ingestion pipeline automates document preparation for retrieval workflows.

### Capabilities

- Load raw support documents
- Clean and normalize text
- Validate document content
- Generate structured processed outputs
- Prepare documents for retrieval services

### Run Ingestion

```bash
python scripts/ingest_documents.py
```

### Run Complete Pipeline

```bash
python scripts/run_pipeline.py
```

### Output

```text
data/processed/documents.json
```

---

## REST API Endpoints

### Generate Response

```http
POST /chat
```

Request:

```json
{
  "message": "How do I reset my password?"
}
```

Response:

```json
{
  "response": "..."
}
```

---

### Submit Feedback

```http
POST /feedback
```

Request:

```json
{
  "question": "How do I reset my password?",
  "response": "Go to Account Settings.",
  "rating": 5,
  "comment": "Helpful"
}
```

---

## Evaluation Framework

The platform includes evaluation components for monitoring response quality and user satisfaction.

### Metrics

- Average Rating
- Positive Feedback Rate
- Feedback Count
- Response Quality Tracking

Example:

```json
{
  "average_rating": 4.8,
  "positive_feedback_rate": 92.0
}
```

---

## Retrieval Experiments

Experiments were conducted to evaluate retrieval approaches and ranking strategies.

### Implemented Experiments

- Keyword Matching
- Term-Frequency Scoring
- Hybrid Retrieval Approaches

Results are documented in:

```text
experiments/results.md
```

Example:

```text
Keyword Matching      81%
Term-Frequency        87%
Hybrid Retrieval      90%
```

### Observations

- Keyword matching performs well for exact support queries.
- Ranking-based retrieval improves document relevance.
- Hybrid retrieval approaches provide the highest-quality context for response generation.

---

## Running the Application

### 1. Start Ollama

```bash
ollama serve
```

### 2. Download a Model

```bash
ollama pull llama3.2
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start FastAPI

```bash
python -m uvicorn app.main:app --reload
```

### 5. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Technologies

- Python
- FastAPI
- Ollama
- Natural Language Processing (NLP)
- Information Retrieval
- Retrieval-Augmented Generation (RAG)
- PySpark
- REST APIs
- Docker
- Git

---

## Key Highlights

- Developed a Generative AI customer support platform using FastAPI and locally hosted large language models.
- Implemented retrieval and ranking workflows to improve response relevance and factual grounding.
- Built document ingestion and preprocessing pipelines for organizational knowledge sources.
- Developed reusable REST APIs for AI inference, retrieval, and response generation.
- Designed evaluation and feedback mechanisms to monitor response quality and user satisfaction.
- Improved maintainability and scalability through modular architecture and automated data-processing workflows.

---

## Future Enhancements

- Vector embeddings and semantic search
- FAISS/Chroma vector database integration
- Hybrid retrieval (keyword + vector search)
- User authentication and access controls
- Dashboard for analytics and evaluation metrics
- Multi-document knowledge base support
- Production deployment on cloud infrastructure
