"""
Class:      CSE1321L
Section:    Module 5
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        11A
"""

def allMath(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = None if b == 0 else a / b
    fdiv = None if b == 0 else a // b
    mod = None if b == 0 else a % b
    pow = a ** b

    return add, sub, mul, div, fdiv, mod, pow


first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))

print(f"Your resulting tuple is {allMath(first, second)}")