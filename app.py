from students import add_student, average_score, format_table, median_score, students
from utils.helpers import highest_score, lowest_score


def main() -> None:
    add_student("Ada", 91)
    add_student("Tunde", 67)
    try:
        add_student("Bad Input", 150)
    except ValueError as exc:
        print("Rejected invalid student:", exc.errors()[0]["msg"] if hasattr(exc, "errors") else exc)

    print("=== Student Report ===")
    print(format_table(students))
    print("-" * 20)
    print(f"Average : {average_score(students):.2f}")
    print(f"Median  : {median_score(students):.2f}")
    print(f"Highest : {highest_score(students)}")
    print(f"Lowest  : {lowest_score(students)}")


if __name__ == "__main__":
    main()
