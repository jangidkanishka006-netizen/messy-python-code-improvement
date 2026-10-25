# Improved Student Marks Calculator

students = [
    {"name": "Aman", "marks": [80, 70, 90]},
    {"name": "Riya", "marks": [45, 55, 60]},
    {"name": "Karan", "marks": [90, 85, 95]}
]


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    return "D"


def display_report(student):
    marks = student["marks"]
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print(f"Name: {student['name']}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("-" * 25)


print("STUDENT MARKS REPORT")
print("-" * 25)

for student in students:
    display_report(student)
