"""
Class:      CSE1321L
Section:    Module 2
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        4C
"""
bal = 1000
print(f"Welcome!\nYou have ${bal} in your account.")
flag = True
while flag:
    print(f"\nMenu"
          f"\n0 – Make a deposit"
          f"\n1 – Make a withdrawal"
          f"\n2 – Display account value")
    selection = int(input("Please make a selection: "))
    match selection:
        case 0:
            bal += float(input("How much would you like to deposit?: "))
            print(f"Your current balance is ${bal}")
        case 1:
            amt = float(input("How much would you like to withdraw?: "))
            if amt > bal:
                print("Not enough balance. Withdrawal cancelled.")
            else:
                bal -= amt
            print(f"Your current balance is ${bal}")
        case 2:
            print(f"Your current balance is ${bal}")
        case _:
            print("Invalid entry, please try again.")
    ret = input("Would you like to return to the main menu (Y/N)?: ")
    if ret == "N":
        flag = False
    elif ret == "Y":
        flag = True
print("\nThank you for banking with us!")