# TODO: 1- Fix the grid labeling to the 2d list
# TODO: 2- Fix is_over() method to only check the new piece's surrounding positions

from heuristic import evaluate
import numpy as np
# Methods

# Method to print the grid
def print_grid():
    print("    A   B   C   D   E   F   G   H")
    for row in range(0, 8):
        print("  +---+---+---+---+---+---+---+---+")
        print(row+1, "| ", end="")
        for column in range(0, 8):
            print(position[row][column], "| ", end="")
        print(row+1)
    print("  +---+---+---+---+---+---+---+---+")
    print("    A   B   C   D   E   F   G   H")


# Method to check if the move wanted is legal
def is_legal(board, row, column):
    # Checks if the space is empty
    if board[row, column] != 0:
        return False
    # Checks if it's at the edge of the board
    if column == columns['a'] or column == columns['h']:
        return True

    # Checks the column behind and in front to place a piece
    if board[row, column-1] == 0 and board[row, column+1] == 0:
        return False

    # If no rule violation occurs then it's legal
    return True


# Method to check if the game is over
def is_over(board, turn):
    # Checking for 5 in a row vertically
    # Checks all the possible places a 5 in a row could start
    for column in range(0, 8):
        for row in range(0, 4):
            if board[row, column] == turn \
                    and board[(row + 1), column] == turn \
                    and board[(row + 2), column] == turn \
                    and board[(row + 3), column] == turn \
                    and board[(row + 4), column] == turn:
                return True

    # Checking for 5 in a row horizontally
    # Checks all the possible places a 5 in a row could start
    for row in range(0, 8):
        for column in range(0, 4):
            if board[row][column] == turn \
                    and board[row, (column + 1)] == turn \
                    and board[row, (column + 2)] == turn \
                    and board[row, (column + 3)] == turn \
                    and board[row, (column + 4)] == turn:
                return True

    # Checking for 5 in a row positively diagonal
    # Checks all the possible places a 5 in a row could start
    for row in range(4, 8):
        for column in range(0, 4):
            if board[row][column] == turn \
                    and board[(row - 1), (column + 1)] == turn \
                    and board[(row - 2), (column + 2)] == turn \
                    and board[(row - 3), (column + 3)] == turn \
                    and board[(row - 4), (column + 4)] == turn:
                return True

    # Checking for 5 in a row horizontally
    # Checks all the possible places a 5 in a row could start
    for row in range(0, 4):
        for column in range(0, 4):
            if board[row][column] == turn \
                    and board[(row + 1), (column + 1)] == turn \
                    and board[(row + 2), (column + 2)] == turn \
                    and board[(row + 3), (column + 3)] == turn \
                    and board[(row + 4), (column + 4)] == turn:
                return True

    return False


# Initialized Variables

# Game grid positions
position = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# Mathematical grid
board = np.zeros((8, 8))

# Hashmap for relating the character values to integers
columns = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

# Turns to make the code more readable
BLACK = 1
WHITE = -1
turn = BLACK
GAMEOVER = False

# Start of the game
print("------------Magnetic Cave------------\n")
print_grid()

while not GAMEOVER:
    # Prints whose turn it is and gets the columns for the place they wish to place the piece
    if turn == BLACK:
        print("Black")
        coordinate = input("Please enter the coordinate (Ex. a1):")
        row = int(coordinate[1]) - 1
        # Casefold lower-cases the input so no common input errors occur
        temp = str.casefold(coordinate[0])
        if columns.__contains__(temp) and row in range(0, 9):
            # Gets the value from the Hashmap based on the key entered
            column = columns[temp]
            if is_legal(board, row, column):
                position[row][column] = "□"
                board[row, column] = BLACK
                turn = WHITE
                GAMEOVER = is_over(board, BLACK)
            else:
                print("Illegal move, Try again!")
        else:
            print("Index wrong, Try again!")
        print_grid()
        print(evaluate(board))
        # print(board)
        if GAMEOVER:
            print("Black won!")
            break
        if np.all(board):
            print("Draw!")
            break
    if turn == WHITE:
        print("White")
        coordinate = input("Please enter the coordinate (Ex. a1):")
        row = int(coordinate[1]) - 1
        temp = str.casefold(coordinate[0])
        if columns.__contains__(temp) and row in range(0, 9):
            column = columns[temp]
            if is_legal(board, row, column):
                position[row][column] = "■"
                board[row, column] = WHITE
                turn = BLACK
                GAMEOVER = is_over(board, WHITE)
            else:
                print("Illegal move, Try again!")
        else:
            print("Wrong Column, Try again!")
        print_grid()
        print(evaluate(board))
        # print(board)
        if GAMEOVER:
            print("White won!")
            break
        if np.all(board):
            print("Draw!")
            break
