"""
Class:      CSE1321L
Section:    Module 3
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        6A
"""

def isValid(width, height):
    return (width + height) > 30.0

def area(width, height):
    return width * height

def perimeter(width, height):
    return (2.0 * width) + (2.0 * height)

run = True
while run:
    width_in = float(input("\nEnter width: "))
    height_in = float(input("Enter height: "))

    valid = isValid(width_in, height_in)
    if not valid:
        print("This is an invalid rectangle.")
    else:
        print("This is a valid rectangle.")
        print(f"The area is: {area(width_in, height_in)}")
        print(f"The perimeter is: {perimeter(width_in, height_in)}")

    choice = input("\nDo you want to enter another width and height (Y/N)?: ")
    if choice == "N":
        run = False

print("Program ends")