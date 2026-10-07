def winner(names: list[str], scores: list[float]) -> str:
    best_idx = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_idx]:
            best_idx = i
    return names[best_idx]


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = sorted(range(len(names)), key=lambda i: scores[i], reverse=True)
    return [names[i] for i in indices]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    return [names[i] for i in range(len(names)) if scores[i] > avg]