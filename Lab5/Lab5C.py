"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        5C
"""
should_exit = False
while not should_exit:
    user_input = input("If you would like to stop this program, say \"please\": ")
    if user_input == "please":
        should_exit = True

print("Program complete")