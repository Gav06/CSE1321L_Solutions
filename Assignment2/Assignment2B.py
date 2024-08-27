"""
Class:      CSE1321L
Section:    Module 1
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 2B
"""
name = input("Enter the name of an animal: ")
category = None

# This use of if statements is questionable but that's how they wanted it
if name == "dog" or name == "cat" or name == "human" or name == "elephant" or name == "whale":
    category = "The animal is a Mammal."
elif name == "eagle" or name == "parrot" or name == "penguin" or name == "sparrow":
    category = "The animal is a Bird."
elif name == "snake" or name == "lizard" or name == "crocodile" or name == "turtle":
    category = "The animal is a Reptile."
elif name == "salmon" or name == "goldfish" or name == "shark" or name == "tuna":
    category = "The animal is a Fish."
elif name == "frog" or name == "toad" or name == "salamander" or name == "newt":
    category = "The animal is an Amphibian."
else:
    category = "Unknown category"

print(category)