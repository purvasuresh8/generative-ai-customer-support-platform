from rank_bm25 import BM25Okapi

documents = [
    "Customers can reset passwords from account settings",
    "Refund requests are accepted within 30 days",
    "Premium users receive priority support"
]

tokenized_docs = [doc.split() for doc in documents]

bm25 = BM25Okapi(tokenized_docs)

query = "How do I reset my password"

scores = bm25.get_scores(query.split())

print("BM25 Scores:")
print(scores)
