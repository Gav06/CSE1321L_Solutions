"""
Class:      CSE1321L
Section:    Module 1
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 1B
"""
principle = float(input("Enter the loan amount: "))
apr = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the loan term (in years): "))
m_apr = (apr / 100.0) / 12
n_payments = years * 12
payment = (principle * m_apr * pow(1 + m_apr, n_payments)) / (pow(1 + m_apr, n_payments) - 1)
payment = round(payment, 2)
print("Your monthly payment is: $" + str(payment))
