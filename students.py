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
