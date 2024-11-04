"""
Class:      CSE1321L
Section:    Module 5
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        11B
"""

def letterPositions(str1, str2):
    indicies = []

    flat = str1.lower()
    reg = str2[0].lower()

    for i in range(len(flat)):
        if flat[i] == reg:
            indicies.append(i)

    return tuple(indicies)

phrase = input("Enter your phrase: ")
letter = input("Enter a letter: ")

print(f"{letter} appears in your phrase in the following positions: {letterPositions(phrase, letter)}")