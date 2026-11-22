from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class Student(BaseModel):
    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("name must not be blank")
        return value


students: list[dict[str, str | float]] = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
]


def average_score(data: list[dict]) -> float:
    if not data:
        return 0.0
    return sum(float(d["score"]) for d in data) / len(data)


def add_student(name: str, score: float, data: list[dict] | None = None) -> dict:
    target = students if data is None else data
    record = Student(name=name, score=score).model_dump()
    target.append(record)
    return record


def median_score(data: list[dict]) -> float:
    scores = sorted(float(d["score"]) for d in data)
    if not scores:
        return 0.0
    mid = len(scores) // 2
    return scores[mid] if len(scores) % 2 else (scores[mid - 1] + scores[mid]) / 2


def format_table(data: list[dict]) -> str:
    if not data:
        return "(no students)"
    width = max(len("Name"), *(len(str(d["name"])) for d in data))
    lines = [f"{'Name':<{width}} | Score", f"{'-' * width}-+-------"]
    lines += [f"{str(d['name']):<{width}} | {float(d['score']):>5.1f}" for d in data]
    return "\n".join(lines)
