"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 2C
"""
number = int(input("Enter a number (1-7): "))

day = None

match number:
    case 1:
        day = "Monday"
    case 2:
        day = "Tuesday"
    case 3:
        day = "Wednesday"
    case 4:
        day = "Thursday"
    case 5:
        day = "Friday"
    case 6:
        day = "Saturday"
    case 7:
        day = "Sunday"
    case _:
        day = "unknown"

if day != "unknown":
    print("The day of the week is: " + day)
else:
    print("Invalid input. Please enter a number between 1 and 7.")
