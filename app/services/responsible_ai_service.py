def evaluate_response(response):

    return {
        "contains_response": bool(response),
        "response_length": len(response),
        "transparency": "Context provided"
    }
  
