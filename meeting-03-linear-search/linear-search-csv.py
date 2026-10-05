import csv


def load_students(filename):
    """
    Read student records from a CSV file.

    Returns a list of dictionaries.
    """

    students = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


def find_student_by_id(students, target_id):
    """
    Perform a linear search for a student ID.

    Return the matching student record.
    Return None if the ID is not found.
    """

    for student in students:
        if student["ID"] == target_id:
            return student

    return None


def main():
    filename = "student_records_5000.csv"

    students = load_students(filename)

    print("ATCS Student Record Search")
    print("--------------------------")
    print(f"Loaded {len(students)} student records.")

    target_id = input("Enter a student ID to search for: ").strip()

    student = find_student_by_id(students, target_id)

    print()

    if student is None:
        print("Student ID not found.")

    else:
        print("Student Record")
        print("--------------")
        print("ID:   ", student["ID"])
        print("Name: ", student["Name"])
        print("Score:", student["Score"])


if __name__ == "__main__":
    main()
