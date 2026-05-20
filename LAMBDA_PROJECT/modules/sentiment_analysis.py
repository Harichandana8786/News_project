POSITIVE_WORDS = [
    "good",
    "great",
    "excellent",
    "positive",
    "success",
    "growth",
    "profit",
    "win",
    "happy",
    "improve",
    "strong",
    "benefit",
    "rise",
    "best"
]

NEGATIVE_WORDS = [
    "bad",
    "poor",
    "negative",
    "loss",
    "fail",
    "drop",
    "decline",
    "crash",
    "sad",
    "risk",
    "weak",
    "fall",
    "worst",
    "problem"
]


def analyze_sentiment(text):

    text = text.lower()

    positive_score = 0
    negative_score = 0

    # =====================================
    # CHECK POSITIVE WORDS
    # =====================================

    for word in POSITIVE_WORDS:

        if word in text:
            positive_score += 1

    # =====================================
    # CHECK NEGATIVE WORDS
    # =====================================

    for word in NEGATIVE_WORDS:

        if word in text:
            negative_score += 1

    # =====================================
    # CALCULATE FINAL SCORE
    # =====================================

    score = positive_score - negative_score

    # =====================================
    # CLASSIFY SENTIMENT
    # =====================================

    if score > 0:
        sentiment = "Positive"

    elif score < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment, score