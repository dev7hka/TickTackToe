from random import randint
from random import seed
import numpy as np
import os
import sys


def new_board(size):

    board = np.full((size,size)," ", dtype=object)
    return board

def print_board(board):

    for i in range(board.shape[0]):
        print("| ", end="")
        for j in range(board.shape[1]):
            print(board[i][j], "| ", end="")
        print()
        print(" ---" * board.shape[0])

def win_check(board):

    diags = [board[::-1, :].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])]

    diags.extend(board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1))
    isDone = False

    for i in [board, board.T, diags]:
        for j in i:
            tmp = "".join((str(k) for k in j))

            if isDone == False and ("X" in j or "O" in j):
                isDone = True
            if "XXX" in tmp:
                print("Player 1 Wins")
                return True
            elif "OOO" in tmp:
                print("Player 2 Wins")
                return True
    if isDone is False:
        print("No one Wins, Game Over")
        return True

def move(board, coordinates, userType):

    x,y = int(coordinates.split(",")[0]),int(coordinates.split(",")[1])
    if board[x-1][y-1] != " ":
        print("Illegal Move!!! Lost your chance")
    else:
        board[x-1][y-1] = "X" if userType == 1 else "O"

def game():

    print("Welcome to game, It is a 2 player game\n"
          "First player's sign is 'X', second player's sign is 'Y', empty slotes are '0'\n"
          "I will tell you when someone wins or game sucks\n"
          "Give coordinates like 2,3 or 1,2.\n"
          "enter 'q' to leave the game")
    user = int(input("Enter the size of the board (e.g.: 4 (for 4x4)): "))
    board = new_board(user)
    print_board(board)
    isDone = False
    while isDone != True:
        user = input("Turn of First Player: ")
        move(board, user, 1)
        print_board(board)
        isDone = win_check(board)
        if isDone == True:
            break
        user = input("Turn of Second Player: ")
        move(board, user, 2)
        print_board(board)
        isDone = win_check(board)

game()























