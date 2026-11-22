def highest_score(data):
    if not data:
        return None  # max() on an empty sequence raises ValueError
    return max(d["score"] for d in data)


def lowest_score(data):
    if not data:
        return None
    return min(d["score"] for d in data)
