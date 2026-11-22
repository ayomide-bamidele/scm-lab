import pytest
from pydantic import ValidationError

from students import add_student, average_score, median_score
from utils.helpers import highest_score, lowest_score


def test_empty_list_is_safe():
    assert average_score([]) == 0.0
    assert median_score([]) == 0.0
    assert highest_score([]) is None
    assert lowest_score([]) is None


def test_statistics():
    data = [{"name": "A", "score": 40}, {"name": "B", "score": 60}, {"name": "C", "score": 90}]
    assert average_score(data) == pytest.approx(63.333, rel=1e-3)
    assert median_score(data) == 60
    assert highest_score(data) == 90
    assert lowest_score(data) == 40


@pytest.mark.parametrize("name,score", [("", 50), ("  ", 50), ("Bob", -1), ("Bob", 101), ("Bob", "x")])
def test_invalid_students_rejected(name, score):
    with pytest.raises(ValidationError):
        add_student(name, score, data=[])
