def average_score(scores: list[int]) -> float:
    if len(scores) != 3:
        raise ValueError("Expected exactly three scores")

    average = sum(scores) / 3
    return float(average)
print(average_score([80, 90, 70]))

