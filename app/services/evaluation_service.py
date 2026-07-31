def evaluate_response(response):

    word_count = len(response.split())

    return {
        "relevance_score": min(word_count / 20, 1.0),
        "quality": "good" if word_count > 10 else "poor"
    }
