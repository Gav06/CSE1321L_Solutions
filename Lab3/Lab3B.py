"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab4: 3B
"""
c1h = int(input("Course 1 hours: "))
c1g = int(input("Grade for course 1: "))
c2h = int(input("Course 2 hours: "))
c2g = int(input("Grade for course 2: "))
c3h = int(input("Course 3 hours: "))
c3g = int(input("Grade for course 3: "))
c4h = int(input("Course 4 hours: "))
c4g = int(input("Grade for course 4: "))
total_hours = c1h + c2h + c3h + c4h
total_qp = (c1g * c1h) + (c2g * c2h) + (c3g * c3h) + (c4g * c4h)
gpa = round(total_qp / total_hours, 2)
print("Total hours: " + str(total_hours))
print("Total quality points: " + str(total_qp))
print("Your GPA for this semester is " + str(gpa))
