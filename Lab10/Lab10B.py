"""
Class:      CSE1321L
Section:    Module 5
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        10B
"""
print("[Friend List]")

friends = []

running = True
while running:
    print("\n1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")

    sel = int(input("Make your selection: "))

    match sel:
        case 1:
            print()
            friend = input("Enter your friend's name: ")
            age = input("Enter your friend's age: ")
            friends.append((friend, age))
        case 2:
            print()
            for friend in friends:
                print(f"Name: {friend[0]}, Age: {friend[1]}")
        case 3:
            running = False

print("\nShutting down...")