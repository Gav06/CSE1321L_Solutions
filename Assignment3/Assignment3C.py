"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 3C
"""
total = 0
for i in range(5):
    for j in range(5):
        total += 1
        odd_or_even = "E" if (total % 2 == 0) else "O"
        print(f"{total}({odd_or_even}) ", end="")
    print("")
