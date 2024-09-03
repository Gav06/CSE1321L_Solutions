"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        4A
"""
score = round(float(input("Enter the score of your exam: ")))
grade = None
if score >= 92:
    grade = "A"
    if 100 >= score >= 98:
        grade += "+"
    elif 94 >= score >= 92:
        grade += "-"
elif score >= 83:
    grade = "B"
    if 91 >= score >= 89:
        grade += "+"
    elif 85 >= score >= 83:
        grade += "-"
elif score >= 74:
    grade = "C"
    if 82 >= score >= 80:
        grade += "+"
    elif 76 >= score >= 74:
        grade += "-"
elif score >= 65:
    grade = "D"
    if 73 >= score >= 71:
        grade += "+"
    elif 67 >= score >= 65:
        grade += "-"
else:
    grade = "F"

print("Letter grade is: " + grade)