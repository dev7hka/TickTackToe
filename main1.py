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


















"""
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], order='C')
print(arr)

dt = np.dtype("int16")
print(dt)
print(arr.shape)
arr.shape = (3,4)
arr =  arr.reshape(4,3)
print(np.ndim(arr))

arr = np.arange(1,31)
arr = arr.reshape(6,5)
print(arr)

arr2 = np.empty((3,4))
arr3 = np.zeros((3,4))
arr4 = np.ones((3,4))
arr5 = np.full((3,4), 5)
print(arr5)

x = [(1,2,3,4), (5,6)]
ab = np.asarray(x)
print(ab)

arr = np.array([[1,2,3],[4,5]])
print(arr)

s = b'Hello World'
a = np.frombuffer(s, dtype = 'S1')
print(a)


arr = np.arange(0,31,2)
arr.shape = (4,4)
print(arr)
print("---------")
print(arr[1,...])

ab = arr[[0,0,3,3],[0,3,0,3]]
print(ab)

arr2 = np.array([[[1,2],[3,4]],
                [[11,22],[33,44]]])
print(arr2)
print(arr2[[0,1],[1,1],[1,0]])
print(arr)
print(arr[arr % 3 == 0])

print(np.isreal(arr))


arr1 = np.full((3,4),5)
arr2 = np.full((3,1), 4)
arr3 = np.array([[1,2],[3,4],[5,6]])
print(arr1)
print(arr3)
print(arr3.T)


arr4 = np.array([[1,2],[3,4],[5,6]])
for i in np.nditer(arr4):
    print(i, end=",")

print(arr4)
print(np.asarray(arr4.flat))
b = arr4.flatten()
print(b)
print("------------------------")
arr4 = np.array([
    [[1,2],[3,4]],
    [[5,6], [7,8]]
])
print(arr4)
arr5 = np.transpose(arr4)
print(arr5)
print(arr5.T)


arr1 = np.arange(8).reshape((1,8))
print(arr1)
arr1 = np.broadcast_to(arr1,(4,8))
print(arr1)

arr2 = np.array([1,2,3,])
arr3 = np.array([[1],[2],[3]])
print(arr2.shape)
print(arr3.shape)
arr4 = np.arange(6).reshape((2,1,3))
print(arr4.shape)
arr4 = np.squeeze(arr4)
print(arr4.shape)
print("-------------------------")
arr2 = np.arange(9).reshape((3,3))
arr3 = np.array([[1,2,3],[4,5,6]])
# print(np.concatenate((arr2,arr3), axis=0))
print(np.stack(arr3, axis=1).shape)

arr1 = np.arange(6).reshape((2,3))
arr2 = np.array([[3,6,9],[9,12,15]])
print(np.add(arr1,arr2))

arr3 = np.array(["def"])
arr4 = np.array(["xxx"])
# print(np.add(arr3,arr4))
print(np.char.add(['hello', 'hi'],[' abc', ' xyz']))

print(np.char.center("HIII", 6, fillchar="$"))
print(np.char.split("Merhaba ben kerim arslan", sep="e"))

arr5 = np.array([[3,0],[1,0]])
print(np.asarray(np.nonzero(arr5)).T)
print(arr5.ravel())
print(np.ravel(arr5))


a = np.array([[10,10], [2,3], [4,5]])

s = a[: , :1]
print(a)
print(s)
a[0,0] = 11
print(a)
print(s)
del a
print(s)

arr1 = np.array([[1,2,3],[4,5,6]], dtype="int32")
arr2 = np.array(arr1, copy=True)
print(arr1)
print(arr2)
print(arr1)
print(arr2)

np.save("abc", arr1)
arr3 = np.load("abc.npy")
print(arr3)
"""
numbers = [1,2,3,4,5,6,7,8,9]

def binary_search(numbers, num):

    mid = len(numbers) // 2

    if len(numbers) < 2:
        return num if numbers[0] == num else -1
    elif numbers[mid] == num:
        return numbers[mid]
    elif numbers[mid] < num:
        return binary_search(numbers[mid:], num)
    else:
        return binary_search(numbers[0:mid], num)

# print(binary_search(numbers, 10))

def guess_number():
    seed(0)
    last_guess = 0
    mynum = randint(0,20)
    while(True):
        user = int(input("Guess what: "))
        if user == mynum:
            print("That is Corrrrectto")
            break
        elif abs(user - mynum) < last_guess:
            print("Hotty")
        else:
            print("It == pretty COLD huh")
        last_guess = abs(user-mynum)

# guess_number()

def rock_paper_scissor():

    pos = ["rock","paper","scissor"]
    user = ""
    while user != "exit":
        myguess = pos[randint(0,2)]
        user = input("Make your Guess ('exit' to leave):")

        print(f"Your guess is {user}, my guess is {myguess}")

        if myguess == user:
            print("YOu soab we are equal")
        elif myguess == "rock" and user == "paper":
            print("You lucky bastard")
        elif myguess == "rock" and user == "scissor":
            print("I smash you :)")
        elif myguess == "paper" and user == "rock":
            print("Okay you suck")
        elif myguess == "paper" and user == "scissor":
            print("Don't cut me")
        elif myguess == "scissor" and user == "rock":
            print("You got me")
        elif myguess == "scissor" and user == "paper":
            print("Gotchaa")

# rock_paper_scissor()






