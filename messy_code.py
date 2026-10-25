# Student Marks Calculator

students = ["Aman", "Riya", "Karan"]

marks1 = [80, 45, 90]
marks2 = [70, 55, 85]
marks3 = [90, 60, 95]

print("STUDENT MARKS REPORT")
print("--------------------")

for i in range(len(students)):
    total = marks1[i] + marks2[i] + marks3[i]
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Name:", students[i])
    print("Marks:", marks1[i], marks2[i], marks3[i])
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
    print("--------------------")
