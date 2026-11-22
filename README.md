# SCM Lab - Students Project

Demo project for **SEN 401 - Software Configuration Management and Maintenance**.

## Project structure
```
app.py              # demo application entry point
students.py         # Student model (Pydantic), add_student, average/median, table formatter
utils/helpers.py    # highest_score / lowest_score helpers
tests/              # pytest unit tests
requirements.txt    # pydantic, pytest
```

## Setup and usage
```
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
pytest
```
Requires Python 3.12+ (works on 3.10+).

## Branching model
- `main` stable and protected (PR review required)
- `dev` integration branch
- `feature/*` new features
- `maint/*` maintenance work; `maintenance` holds the Lab 2 changes

## Releases
- **v1.0** baseline project
- **v1.1** corrective, adaptive, perfective and preventive maintenance
