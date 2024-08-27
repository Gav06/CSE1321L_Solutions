"""
Class:      CSE1321L
Section:    Module 1
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 1C
"""
kilos = float(input("Enter your weight in kilograms: "))
cm = float(input("Enter your height in centimeters: "))
meters = cm / 100
bmi = round(kilos / (meters**2), 1)
weight_class = 1 + (bmi >= 18.5) + (bmi >= 25) + (bmi >= 30)
print("Your BMI is: " + str(bmi))
print("You are classified as: " + str(weight_class) + " weight")