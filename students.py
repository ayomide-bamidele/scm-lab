"""Student records module.

Holds the in-memory student list and the functions that operate on it:
validation (Pydantic), adding students and computing score statistics.
"""
from __future__ import annotations

from statistics import median

from pydantic import BaseModel, Field, field_validator

__all__ = ["Student", "students", "add_student", "average_score", "median_score", "format_table"]

Record = dict[str, str | float]


class Student(BaseModel):
    """A validated student record (name must be non-blank, score in 0-100)."""

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        """Trim whitespace and reject names that are only spaces."""
        value = value.strip()
        if not value:
            raise ValueError("name must not be blank")
        return value


# Seed data used by the demo application.
students: list[Record] = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
]


def _scores(data: list[Record]) -> list[float]:
    """Return the scores in ``data`` as floats (single place to extract them: DRY)."""
    return [float(d["score"]) for d in data]


def add_student(name: str, score: float, data: list[Record] | None = None) -> Record:
    """Validate and append a student.

    Args:
        name: Student name (non-blank).
        score: Score between 0 and 100.
        data: Target list; defaults to the module-level ``students`` list.

    Returns:
        The stored record.

    Raises:
        pydantic.ValidationError: If the name or score is invalid.
    """
    target = students if data is None else data
    record = Student(name=name, score=score).model_dump()
    target.append(record)
    return record


def average_score(data: list[Record]) -> float:
    """Return the mean score, or 0.0 for an empty list."""
    scores = _scores(data)
    return sum(scores) / len(scores) if scores else 0.0


def median_score(data: list[Record]) -> float:
    """Return the median score, or 0.0 for an empty list."""
    scores = _scores(data)
    return median(scores) if scores else 0.0


def format_table(data: list[Record]) -> str:
    """Render the records as an aligned two-column text table."""
    if not data:
        return "(no students)"
    width = max(len("Name"), *(len(str(d["name"])) for d in data))
    lines = [f"{'Name':<{width}} | Score", f"{'-' * width}-+-------"]
    lines += [f"{str(d['name']):<{width}} | {float(d['score']):>5.1f}" for d in data]
    return "\n".join(lines)
