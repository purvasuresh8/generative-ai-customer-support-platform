documents = [
    "Reset password instructions",
    "Refund policy information",
    "Premium support details"
]

query = "password reset"

for doc in documents:
    score = sum(
        1 for word in query.split()
        if word.lower() in doc.lower()
    )

    print(f"{doc}: {score}")
    