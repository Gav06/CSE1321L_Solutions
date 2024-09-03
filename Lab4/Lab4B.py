"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        4B
"""
num = float(input("Welcome!\nPlease input a number: "))
print("\nWhat would you like to do to this number:")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")
choice = int(input())
print("\n")
match choice:
    case 0:
        print(f"The additive inverse of {num} is {-num} ")
    case 1:
        if num == 0:
            print("Cannot divide by 0!")
        else:
            print(f"The reciprocal of {num} is {1/num}")
    case 2:
        print(f"The square of {num} is {num**2}")
    case 3:
        print(f"The cube of {num} is {num**3}")
    case 4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid input, please try again!")