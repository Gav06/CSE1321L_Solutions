"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab: 3C
"""
num_sml = int(input("Enter the number of small sandwiches: "))
num_med = int(input("Enter the number of medium sandwiches: "))
num_lrg = int(input("Enter the number of large sandwiches: "))
num_xl = int(input("Enter the number of extra-large sandwiches: "))

print("\nYou've entered {} {} sandwiches.".format(num_sml, "small"))
print("You've entered {} {} sandwiches.".format(num_med, "medium"))
print("You've entered {} {} sandwiches.".format(num_lrg, "large"))
print("You've entered {} {} sandwiches.".format(num_xl, "extra-large"))

time = (num_sml * 30) + (num_med * 60) + (num_lrg * 75) + (num_xl * 135)
mins = time // 60
secs = time % 60

print("\nTotal cooking time is {} minutes and {} seconds.".format(mins, secs))