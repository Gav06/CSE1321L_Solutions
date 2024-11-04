"""
Class:      CSE1321L
Section:    Module 5
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 6B
"""
from random import random

def print_board(board_in):
    for r in range(len(board_in)):
        for c in range(len(board_in[r])):
            print(board_in[r][c], end=" ")
        print()

width = int(input("Enter dungeon width: "))
height = int(input("Enter dungeon height: "))

board = []
numberOfUndiscoveredTreasures = 0

# Fill the board
for row in range(width):
    l = []
    for col in range(height):
        rand = random()
        if rand >= 0.7:
            l.append("T")
            numberOfUndiscoveredTreasures += 1
        else:
            l.append("O")
    board.append(l)

print(f"Treasures are hidden in {numberOfUndiscoveredTreasures} locations.")

while numberOfUndiscoveredTreasures > 0:
    row = int(input(f"Enter a row to check (0-{width - 1}): "))
    col = int(input(f"Enter a column to check (0-{height - 1}): "))

    loc = board[row][col]

    match loc:
        case "T":
            print(f"You found a treasure at ({row}, {col})!")
            board[row][col] = "X"
            numberOfUndiscoveredTreasures -= 1
        case "O":
            print(f"No treasure found at ({row}-{col})")
        case "X":
            print(f"You already discovered the treasure at ({row}, {col})")

print("You found all the treasure!")
print_board(board)