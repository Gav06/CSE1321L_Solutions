"""
Class:      CSE1321L
Section:    Module 1
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 2A
"""
age = int(input("Enter your age: "))
price = 0

if age < 12:
    price = 8
elif age <= 17:
    price = 10
elif age <= 64:
    member = input("Are you a member of the cinema club (yes or no)? ")
    if member == "yes":
        price = 12
    else:
        price = 15
else:
    price = 10

print("Your ticket price is: $" + str(price))
