# ----------------------------------
# Student Marks Analyzer
# Author: Priyanshi Sharma
# Date: November 2025
# ----------------------------------

# This program helps to store student marks,
# find averages, top marks, grades, and pass/fail status.

# ----------------------------------
# Step 1: Take student details
# ----------------------------------

students = {}

print("Welcome to Student Marks Analyzer")
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i + 1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# ----------------------------------
# Step 2: Find top marks and average
# ----------------------------------

marks_list = list(students.values())
top_score = max(marks_list)
average = sum(marks_list) / len(marks_list)

# Find all students who got the top score
top_students = [name for name, m in students.items() if m == top_score]

# ----------------------------------
# Step 3: Check pass or fail
# ----------------------------------

passed = [name for name, marks in students.items() if marks >= 40]
failed = [name for name, marks in students.items() if marks < 40]

# ----------------------------------
# Step 4: Grade function
# ----------------------------------

def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'

# ----------------------------------
# Step 5: Display results in a table
# ----------------------------------

print("\n" + "-" * 40)
print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}{'Status':<10}")
print("-" * 40)

# Sort students by marks (highest first)
for name, marks in sorted(students.items(), key=lambda x: x[1], reverse=True):
    grade = get_grade(marks)
    status = "Pass" if marks >= 40 else "Fail"
    print(f"{name:<15}{marks:<10.2f}{grade:<5}{status:<10}")

print("-" * 40)
print(f"Top Score: {top_score} ({', '.join(top_students)})")
print(f"Average Score: {average:.2f}")
print(f"Passed Students: {len(passed)}")
print(f"Failed Students: {len(failed)}")
print(f"Passed: {', '.join(passed) if passed else 'None'}")
print(f"Failed: {', '.join(failed) if failed else 'None'}")
print("-" * 40)
print("✅ Analysis Complete! Thank you for using the program.")
