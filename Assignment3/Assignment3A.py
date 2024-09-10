"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 3A
"""
num = int(input("Enter a positive number: "))

if num <= 0:
    print("Error: positive number required!")
    exit(1)

val = 0
for i in range(num):
    for j in range(i + 1):
        val += 1
        print(f"{val} ", end="")
    print("")
