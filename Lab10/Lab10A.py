"""
Class:      CSE1321L
Section:    Module 5
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        10A
"""
print("[Mailing List]")

emails = []

running = True
while running:
    print("\n1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")

    sel = int(input("Make your selection: "))

    match sel:
        case 1:
            email = input("Enter the email to be added: ")
            emails.append(email)
        case 2:
            email = input("Enter the email to be removed: ")
            if email in emails:
                emails.remove(email)
                print(f"{email} has been removed from the mailing list.")
            else:
                print(f"No such email in list: {email}")
        case 3:
            print()
            for email in emails:
                print(email)
        case 4:
            running = False

print("\nShutting down...")