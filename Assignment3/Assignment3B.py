"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 3B
"""

continue_playing = True
while continue_playing:
    direction = None
    direction_ok = False
    while not direction_ok:
        direction = input("You are in a room. Choose a direction to move in (north, south, east, west): ")
        if direction == "north" or direction == "south" or direction == "east" or direction == "west":
            direction_ok = True

    choice_ok = False
    choice = None
    match direction:
        case "north":
            while not choice_ok:
                choice = input("You move north and find a river. What will you do? (swim/build a raft): ")
                if choice == "swim" or choice == "build a raft":
                    choice_ok = True

            match choice:
                case "swim":
                    print("You swim across the river and find a hidden treasure.")
                case "build a raft":
                    print("Your raft gets stuck on a rock and you are eaten by piranhas.")
        case "south":
            while not choice_ok:
                choice = input("You move south and discover a dense forest. What will you do? (climb a tree/walk deeper): ")
                if choice == "climb a tree" or choice == "walk deeper":
                    choice_ok = True

            match choice:
                case "climb a tree":
                    print("You find a hidden tree fort with food and weapons")
                case "walk deeper":
                    print("You end up stuck in a bog, never to be seen again")
        case "east":
            while not choice_ok:
                choice = input("You move east and encounter a mountain. What will you do? (climb the mountain/go around it): ")
                if choice == "climb the mountain" or choice == "go around it":
                    choice_ok = True

            match choice:
                case "climb the mountain":
                    print("You climb the mountain to be attacked by a Yeti and killed.")
                case "go around it":
                    print("You go around the mountain and discover a lost village filled with people.")
        case "west":
            while not choice_ok:
                choice = input("You move west and stumble upon a cave. What will you do? (enter the cave/walk past it): ")
                if choice == "enter the cave" or choice == "walk past it":
                    choice_ok = True

            match choice:
                case "enter the cave":
                    print("You enter the cave and find a sleeping dragon.")
                case "walk past it":
                    print("You walk past the cave and notice claw marks on the nearby trees.")

    answer_good = False
    answer = None
    while not answer_good:
        answer = input("Would you like to continue playing? (yes/no): ")
        answer_good = (answer == "yes") or (answer == "no")
        if answer_good:
            continue_playing = (answer == "yes")

print("Thank you for playing!")