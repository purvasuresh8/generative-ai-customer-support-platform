class RetrievalService:

    def __init__(self):
        self.documents = [
            "Customers can reset passwords from Account Settings.",
            "Refund requests must be submitted within 30 days.",
            "Premium users receive priority support.",
            "Users can update profile information from the dashboard."
        ]

    def retrieve(self, query):

        query_words = query.lower().split()

        matches = []

        for doc in self.documents:
            score = sum(
                1 for word in query_words
                if word in doc.lower()
            )

            matches.append((score, doc))

        matches.sort(reverse=True)

        return [
            doc
            for score, doc in matches[:3]
            if score > 0
        ]
        