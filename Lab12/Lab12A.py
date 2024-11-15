"""
Class:      CSE1321L
Section:    Module 6
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        12A
"""

class Chair:
    def __init__(self, numOfLegs = 4, rolling = False, material = "plastic"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material


print("You are about to create a chair.")
num_legs = int(input("How many legs does your chair have: "))
rolling_input = input("Is your chair rolling (true/false): ")
is_rolling = True if rolling_input == "true" else False
material = input("What is your chair made of: ")

chair = Chair(num_legs, is_rolling, material)

print(f"Your chair has {chair.numOfLegs} legs, is {" " if chair.rolling else "not "}rolling, and is made of {chair.material}.")

print("This program is going to change that.")

chair.rolling = False
chair.numOfLegs = 4
chair.material = "wood"

print(f"Your chair has {chair.numOfLegs} legs, is {"" if chair.rolling else "not"} rolling, and is made of {chair.material}.")
