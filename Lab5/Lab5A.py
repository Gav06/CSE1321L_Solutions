"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        5A
"""
print("Please enter 10 numbers and this program will display the largest.")
largest = None
for i in range(10):
    num = int(input(f"Please enter number {i + 1}: "))
    if largest is None or largest < num:
        largest = num

print(f"\nThe largest number was {largest}")
