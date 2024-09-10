"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        5B
"""
size = int(input("Please enter a value for the size: "))

# for printing the box
print(f"This is the requested {size}x{size} box:")
for row in range(size):
    line = ""
    for col in range(size):
        line += "*"
    print(line)

# right-facing triangle
print(f"This is the requested right-facing {size}x{size} right-triangle:")
for row in range(size):
    line = ""
    for col in range(size):
        if col <= row:
            line += "*"
        else:
            line += " "
    print(line)

# left-facing triangle
print(f"This is the requested left-facing {size}x{size} right-triangle:")
for row in range(size):
    line = ""
    for col in range(size):
        if (col + 1) > (size - (row + 1)):
            line += "*"
        else:
            line += " "
    print(line)
