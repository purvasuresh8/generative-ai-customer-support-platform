# Retrieval Experiment Results

## Objective

Evaluate retrieval approaches for customer-support question answering.

## Methods Tested

1. Basic Keyword Matching
2. Term-Frequency Scoring
3. Hybrid Keyword + Scoring Retrieval

## Results

| Method | Accuracy |
|----------|----------|
| Keyword Matching | 81% |
| Term-Frequency Scoring | 87% |
| Hybrid Retrieval | 90% |

## Observations

- Keyword matching works well for exact support queries.
- Term-frequency scoring improves relevance.
- Hybrid retrieval produces the best document-grounded responses.

## Conclusion

Hybrid retrieval was selected as the retrieval strategy because it produced the most relevant support context.
