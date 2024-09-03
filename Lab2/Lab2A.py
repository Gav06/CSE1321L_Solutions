"""
Class:      CSE1321L
Section:    Module 1
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab4:        2A
"""
name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
sentence = ("Once upon a time, there was a person named {} who had a child named {}. "
            "This child would {} {} while singing to strangers.").format(name1, name2, verb, adverb)
print(sentence)