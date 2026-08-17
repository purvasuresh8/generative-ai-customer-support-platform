# Retrieval Experiment Results

## Objective

Evaluate retrieval methods for customer-support question answering.

## Dataset

Customer support FAQs and ticket knowledge base.

## Methods

1. BM25 keyword retrieval
2. Dense vector retrieval
3. Hybrid retrieval

## Evaluation Criteria

- Relevance
- Context quality
- Answer accuracy

## Results

| Method | Relevance Score |
|----------|----------|
| BM25 | 78% |
| Vector Search | 86% |
| Hybrid Search | 90% |

## Observations

- BM25 performed well for exact keyword matches.
- Vector search improved semantic understanding.
- Hybrid retrieval returned the most relevant context overall.

## Conclusion

Hybrid retrieval provided the strongest document-grounded responses and was selected for production use.
