from students import students, add_student, average_score
from utils.helpers import highest_score, lowest_score


def main():
    add_student("Ada", 91)
    add_student("Tunde", 67)
    print("Average:", average_score(students))
    print("Highest:", highest_score(students))
    print("Lowest:", lowest_score(students))


if __name__ == "__main__":
    main()
