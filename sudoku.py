from util import *

def solve(board):

    find = find_empty(board)
    #base case
    if not find:
        return True
    else:
        row, col = find
    #check the empty spot for a valid number
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    return False

def valid(board, num, pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = (pos[1] // 3) * 3
    box_y = (pos[0] // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if board[box_y + i][box_x + j] == num and pos != (i,j):
                return False
    return True

def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j!= 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None
# print_board(board)
# solve(board)
# print()
# print()
# print_board(board)