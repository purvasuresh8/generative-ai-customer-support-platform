from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

documents = [
    "Customers can reset passwords from account settings",
    "Refund requests are accepted within 30 days",
    "Premium users receive priority support"
]

query = "password reset"

# BM25
tokenized_docs = [doc.split() for doc in documents]
bm25 = BM25Okapi(tokenized_docs)
bm25_scores = bm25.get_scores(query.split())

# Vector
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    np.array(embeddings).astype("float32")
)

query_embedding = model.encode([query])

_, vector_indices = index.search(
    np.array(query_embedding).astype("float32"),
    3
)

print("BM25 Scores:")
print(bm25_scores)

print("\nVector Search Results:")
print(vector_indices)
