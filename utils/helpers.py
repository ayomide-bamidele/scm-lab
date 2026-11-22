def highest_score(data):
    return max(d["score"] for d in data)


def lowest_score(data):
    return min(d["score"] for d in data)
