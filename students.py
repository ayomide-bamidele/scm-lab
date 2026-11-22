students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
]


def average_score(data):
    if len(data) == 0:
        return 0.0  # avoid division by zero on an empty list
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    if isinstance(score, bool) or not isinstance(score, (int, float)) or not 0 <= score <= 100:
        raise ValueError("score must be a number between 0 and 100")
    students.append({"name": name.strip(), "score": score})
