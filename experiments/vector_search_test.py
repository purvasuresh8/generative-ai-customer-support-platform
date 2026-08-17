from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

documents = [
    "Customers can reset passwords from account settings",
    "Refund requests are accepted within 30 days",
    "Premium users receive priority support"
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    np.array(embeddings).astype("float32")
)

query = "How do I reset my password?"

query_vector = model.encode([query])

distances, indices = index.search(
    np.array(query_vector).astype("float32"),
    2
)

print("Retrieved Documents:")

for idx in indicesprint(documents[idx])
