"""Utility helpers for score analysis."""
from __future__ import annotations

Record = dict[str, str | float]


def highest_score(data: list[Record]) -> float | None:
    """Return the highest score, or None if ``data`` is empty."""
    return max((float(d["score"]) for d in data), default=None)


def lowest_score(data: list[Record]) -> float | None:
    """Return the lowest score, or None if ``data`` is empty."""
    return min((float(d["score"]) for d in data), default=None)
