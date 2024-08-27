"""
Class:      CSE1321L
Section:    Module 1
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 1A
"""
print("[Let's create a mailing address!]\n")
name = input("Name: ")
street = input("Street Address: ")
city = input("City: ")
state = input("State: ")
zip = input("Zip Code: ")
full_addr = name + "\n" + street + "\n" + city + ", " + state + " " + zip
print("\nYour mailing address is:\n" + full_addr)