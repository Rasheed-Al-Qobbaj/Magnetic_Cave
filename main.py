# TODO: 1- Fix the grid labeling to the 2d list
# TODO: 2- Fix is_over() method to only check the new piece's surrounding positions

import numpy as np
import time

# Methods
#


def evaluate(board) -> int:
    window = np.array([0] * 5)
    score = 0
    # Horizontal
    for row in range(0, 8):
        for column in range(0, 4):
            window = board[row, column:column + 5]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[4]
            if (window[0] + window[1] + window[2] + window[3] + window[4]) == 5:
                score = 100000
            elif (window[0] + window[1] + window[2] + window[3] + window[4]) == -5:
                score = -100000
    # Vertical
    for column in range(0, 8):
        for row in range(0, 4):
            window = board[row:row + 5, column]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[4]
            if row > 0:
                if window[row-1] == window[row] and window[row+1] == window[row]:
                    score += (50*window[row])
            if (window[0] + window[1] + window[2] + window[3] + window[4]) == 5:
                score = 100000
            elif (window[0] + window[1] + window[2] + window[3] + window[4]) == -5:
                score = -100000
    # Diagonal
    for row in range(4, 8):
        for column in range(0, 4):
            window = board[row - 4:row + 1, column:column + 5]
            score += 1 * window[0, 0] + 2 * window[1, 1] + 3 * window[2, 2] + 2 * window[3, 3] + 1 * window[4, 4]
            score += 1 * window[4, 0] + 2 * window[3, 1] + 3 * window[2, 2] + 2 * window[1, 3] + 1 * window[0, 4]
            if (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == 5 or (window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == 5:
                score = 100000
            elif (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == -5 or (window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == -5:
                score = -100000
    return score

"""        
:param board: 
:param turn: 
:param move: 
:return: 
"""


legal_moves = {}

for i in range(0, 8):  # fir
    legal_moves[(i, 0)] = True
    legal_moves[(i, 7)] = True


def update_legal_moves(column, row):
    tmp_tuple = (row, column)
    if tmp_tuple in legal_moves:
        del legal_moves[tmp_tuple]
    if column - 1 >= 0:
        if board[row, column - 1] == 0:
            legal_moves[(row, column - 1)] = True
    if column + 1 <= 7:
        if board[row, column + 1] == 0:
            legal_moves[(row, column + 1)] = True


def possible_moves(board: np.ndarray):
    moves = set()
    for row in range(0, 8):
        for column in range(0, 8):
            if is_legal(row, column):
                moves.add((row, column))
                break
        for column in range(7, -1, -1):
            if is_legal(row, column):
                moves.add((row, column))
                break

    return list(moves)


def mini_max(current_board_position, depth_limit: int, max_turn: bool, depth: int):
    if max_turn:
        turn = 1
    else:
        turn = -1

    if depth == depth_limit or is_over(current_board_position, turn):  # 1 will be changed prolly
        return evaluate(current_board_position), current_board_position  #

    if max_turn:
        max_eval = -np.inf
        best_move = [(0, 0)]

        for move in possible_moves(current_board_position):
            current_board_position[move[0], move[1]] = 1  # simulate the move
            evaluation, tmp = mini_max(current_board_position, depth_limit, False, (depth + 1))
            print("MAX EVAL = ", evaluation, "DEPTH = ", depth)
            current_board_position[move[0], move[1]] = 0  # undo the simulation
            max_eval = max(max_eval, evaluation)
            if evaluation == max_eval:
                best_move = move
        return max_eval, best_move
    else:

        min_eval = np.inf
        best_move = [(0, 0)]

        for move in possible_moves(current_board_position):
            current_board_position[move[0], move[1]] = 1  # simulate the move
            evaluation, tmp = mini_max(current_board_position, depth_limit, True, (depth + 1))
            print("MIN EVAL = ", evaluation, "DEPTH = ", depth)
            current_board_position[move[0], move[1]] = 0  # undo the simulation
            min_eval = min(min_eval, evaluation)
            if evaluation == min_eval:
                best_move = move
        return min_eval, best_move


def make_move(board: np.ndarray, turn):
    move_eval, move_position = mini_max(board, 7, True, 3)
    row = move_position[0]
    column = move_position[1]
    board[row, column] = turn
    if turn == BLACK:
        position[row][column] = "□"
    else:
        position[row][column] = "■"


#

# Method to print the grid
def print_grid():
    print("    A   B   C   D   E   F   G   H")
    for row in range(0, 8):
        print("  +---+---+---+---+---+---+---+---+")
        print(row + 1, "| ", end="")
        for column in range(0, 8):
            print(position[row][column], "| ", end="")
        print(row + 1)
    print("  +---+---+---+---+---+---+---+---+")
    print("    A   B   C   D   E   F   G   H")


# Method to check if the move wanted is legal
def is_legal(row, column):
    # Checks if the space is empty
    if board[row, column] != 0:
        return False
    # Checks if it's at the edge of the board
    if column == COULMNS['a'] or column == COULMNS['h']:
        return True

    # Checks the column behind and in front to place a piece
    if board[row, column - 1] == 0 and board[row, column + 1] == 0:
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


if __name__ == '__main__':
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
    COULMNS = {
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
    print("Welcome to Magnetic Cave!")
    print('Select Game Mode:')
    print('1. Player vs Player')
    print('2. Player vs AI  [BLACK]')
    print('3. Player vs AI  [WHITE]')

    choice = int(input('Enter your choice: '))
    print_grid()

    if choice == 1:
        while not GAMEOVER:
            # Prints whose turn it is and gets the columns for the place they wish to place the piece
            if turn == BLACK:
                print("Black")
                coordinate = input("Please enter the coordinate (Ex. a1):")
                row = int(coordinate[1]) - 1
                # Casefold lower-cases the input so no common input errors occur
                temp = str.casefold(coordinate[0])
                if COULMNS.__contains__(temp) and row in range(0, 9):
                    # Gets the value from the Hashmap based on the key entered
                    column = COULMNS[temp]
                    if is_legal(row, column):
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
                if COULMNS.__contains__(temp) and row in range(0, 9):
                    column = COULMNS[temp]
                    if is_legal(row, column):
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
    elif choice == 2:
        while not GAMEOVER:
            # Prints whose turn it is and gets the columns for the place they wish to place the piece
            if turn == BLACK:
                print("Black")
                coordinate = input("Please enter the coordinate (Ex. a1):")
                row = int(coordinate[1]) - 1
                # Casefold lower-cases the input so no common input errors occur
                temp = str.casefold(coordinate[0])
                if COULMNS.__contains__(temp) and row in range(0, 9):
                    # Gets the value from the Hashmap based on the key entered
                    column = COULMNS[temp]
                    if is_legal(row, column):
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
                #print(board)
                if GAMEOVER:
                    print("Black won!")
                    break
                if np.all(board):
                    print("Draw!")
                    break
            if turn == WHITE:
                timer_start = time.time()
                make_move(board, WHITE)
                GAMEOVER = is_over(board, WHITE)
                #print('test1')
                print_grid()
                print(evaluate(board))
                timer_end = time.time()
                print(timer_end - timer_start)
                #print(board)
                turn = BLACK
                if GAMEOVER:
                    print("White won!")
                    break
                if np.all(board):
                    print("Draw!")
                    break
