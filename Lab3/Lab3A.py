"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab: 3A
"""
amount = float(input("Amount owed: $"))
apr = float(input("APR: "))
mpr = apr / 12
payment = round(amount * (mpr / 100), 2)
print("Monthly percentage rate: " + str(round(mpr, 3)))
print("Minimum payment: $" + str(payment))