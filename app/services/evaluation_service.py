class EvaluationService:

    @staticmethod
    def average_rating(feedback_data):

        if not feedback_data:
            return 0

        ratings = [
            item["rating"]
            for item in feedback_data
        ]

        return round(
            sum(ratings) / len(ratings),
            2
        )

    @staticmethod
    def positive_feedback_rate(feedback_data):

        if not feedback_data:
            return 0

        positive = len([
            item
            for item in feedback_data
            if item["rating"] >= 4
        ])

        return round(
            (positive / len(feedback_data)) * 100,
            2
        )
        