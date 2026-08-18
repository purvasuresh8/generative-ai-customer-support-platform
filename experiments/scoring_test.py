queries = [
    "reset password",
    "refund request",
    "premium support"
]

documents = [
    "Reset password instructions",
    "Refund policy information",
    "Premium support details"
]

correct_matches = 0

for query in queries:

    scores = []

    for doc in documents:
        score = sum(
            1 for word in query.split()
            if word.lower() in doc.lower()
        )

        scores.append(score)

    if max(scores) > 0:
        correct_matches += 1

accuracy = correct_matches / len(queries)

print(f"Accuracy: {accuracy * 100:.2f}%")
