# practice problem for the midterm

import random

continue_playing = True
user_score = 0
cpu_score = 0

while continue_playing:
    initial_num = random.randint(10, 25)

    num_add = random.randint(1, 6)
    num_sub = random.randint(1, 6)

    print("[Over/Under]")

    print(f"Options:\n1) Add {num_add}\n2) Subtract {num_sub}")
    choice = int(input("Choice: "))

    print(f"The original number was {initial_num}!")
    new_num = initial_num
    if choice == 1:
        new_num += num_add
    elif choice == 2:
        new_num -= num_sub

    print(f"Your final total was {new_num}.")

    initial_dist = abs(20 - initial_num)
    new_dist = abs(20 - new_num)
    victory = False
    if new_dist < initial_dist:
        victory = True

    if victory:
        print("You win!")
        user_score += 1
    else:
        print("CPU wins.")
        cpu_score += 1

    play_again = input("Do you want to play again? (Y/N) ")
    if play_again == "Y":
        continue_playing = True
    elif play_again == "N":
        continue_playing = False


print(f"Your wins: {user_score} --- CPU Wins: {cpu_score}")

