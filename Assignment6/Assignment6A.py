"""
Class:      CSE1321L
Section:    Module 5
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 6A
"""

# Method from the module 5 part 1 slideshow
def bubble_sort(numbers):
    l = len(numbers)

    for it in range(l):
        for pos in range(l - it - 1):
            if numbers[pos] > numbers[pos + 1]:
                temp = numbers[pos]
                numbers[pos] = numbers[pos + 1]
                numbers[pos + 1] = temp


def count_positive(numbers):
    i = 0
    for num in numbers:
        if num > 0:
            i += 1
    return i


def count_negative(numbers):
    i = 0
    for num in numbers:
        if num < 0:
            i += 1
    return i


numbers = input("Enter numbers separated by space: ").split(" ")
# Convert every string into a number
numbers = list(map(int, numbers))

bubble_sort(numbers)

print(f"Sorted List: {numbers}")
print(f"Positive numbers: {count_positive(numbers)}")
print(f"Negative numbers: {count_negative(numbers)}")
