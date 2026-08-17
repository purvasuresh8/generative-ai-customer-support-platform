from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RetrievalService:

    def __init__(self):

        self.documents = [
            "Customers can reset passwords from Account Settings.",
            "Refund requests must be submitted within 30 days.",
            "Premium users receive priority support."
        ]

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        embeddings = self.model.encode(
            self.documents
        )

        self.index = faiss.IndexFlatL2(
            embeddings.shape[1]
        )

        self.index.add(
            np.array(embeddings).astype("float32")
        )

    def retrieve(self, query, k=3):

        query_embedding = self.model.encode(
            [query]
        )

        _, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            k
        )

        return [
            self.documents[i]
            for i in indices[0]
        ]
        
        