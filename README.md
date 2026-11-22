# SCM Lab - Students Project

Demo project for **SEN 401 - Software Configuration Management and Maintenance**.

## Project structure
```
app.py            # demo application entry point
students.py       # student data + average_score / add_student
utils/helpers.py  # highest_score / lowest_score helpers
requirements.txt  # dependencies
README.md         # this file
```

## Usage
```
python app.py
```

## Branching model
- `main`      : stable, protected (PR review required)
- `dev`       : integration branch
- `feature/*` : new features
- `maint/*`   : maintenance work
