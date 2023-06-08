# TODO: 1- Fix the grid labeling to the 2d list
# TODO: 2- Fix is_over() method to only check the new piece's surrounding positions

import numpy as np


# Methods
#


def evaluate(board, move=0) -> int:
    window = np.array([0] * 5)
    score = 0
    # Horizontal
    for row in range(0, 8):
        for column in range(0, 4):
            window = board[row, column:column + 5]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[4]
    # Vertical
    for column in range(0, 8):
        for row in range(0, 4):
            window = board[row:row + 5, column]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[4]

    # Diagonal
    for row in range(4, 8):
        for column in range(0, 4):
            window = board[row - 4:row + 1, column:column + 5]
            score += 1 * window[0, 0] + 2 * window[1, 1] + 3 * window[2, 2] + 2 * window[3, 3] + 1 * window[4, 4]
            score += 1 * window[4, 0] + 2 * window[3, 1] + 3 * window[2, 2] + 2 * window[1, 3] + 1 * window[0, 4]

    return score

    """        
    :param board: 
    :param turn: 
    :param move: 
    :return: 
    """


legal_moves = {}

for i in range(0, 8):
    legal_moves[(0, i)] = True
    legal_moves[(7, i)] = True
def update_legal_moves(column, row):
    legal_moves.pop((row, column))
    if column - 1 >= 0:
        if board[row, column - 1] == 0:
            legal_moves[(row, column - 1)] = True
    if column + 1 <= 7:
        if board[row, column + 1] == 0:
            legal_moves[(row, column + 1)] = True

#
# def possible_moves(board: np.ndarray) -> np.ndarray:
#     moves = np.array([])
#     for column in range(0, 8):
#         for row in range(0, 8):
#             if is_legal(row, column):
#                 np.append(moves, (row, column))
#                 break
#         for row in range(7, -1, -1):
#             if is_legal(row, column) and not moves.__contains__((row, column)):
#                 np.append(moves, (row, column))
#
#                 break
#     return moves


def mini_max(depth_limit, max_turn: bool, board, depth=0):

    if depth == depth_limit or is_over(board, 1):  # 1 will be changed prolly
        return [evaluate(board), None]

    if max_turn:
        max_eval = -np.inf
        best_move = None

        for move in legal_moves.keys():

            tmp_col = move[1]
            tmp_row = move[0]
            board[tmp_col,tmp_row] = 1

            templ = list(mini_max(depth_limit, False, board, depth + 1))

            eval = templ[0]
            tmp = templ[1]
            board[tmp_col,tmp_row] = 0

            if eval > max_eval:
                best_move = move

            max_eval = max(max_eval, eval)
        r_value = [max_eval, best_move]
        return r_value
    else:
        min_eval = np.inf
        best_move = None
        for move in legal_moves.keys():

            tmp_col = move[1]
            tmp_row = move[0]
            board[tmp_col, tmp_row] = 1

            tmpl = list(mini_max(depth_limit, True, board, depth + 1))
            eval = tmpl[0]
            tmp = tmpl[1]
            board[tmp_col,tmp_row] = 0
            if eval < min_eval:
                best_move = move
            min_eval = min(min_eval, eval)
            r_value = [min_eval, best_move]
        return r_value


def make_move(board: np.ndarray, turn):
    move_value, move = mini_max(3, True, board)
    board[move] = turn


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
    if column == columns['a'] or column == columns['h']:
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
                if columns.__contains__(temp) and row in range(0, 9):
                    # Gets the value from the Hashmap based on the key entered
                    column = columns[temp]
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
                if columns.__contains__(temp) and row in range(0, 9):
                    column = columns[temp]
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
                if columns.__contains__(temp) and row in range(0, 9):
                    # Gets the value from the Hashmap based on the key entered
                    column = columns[temp]
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
                print(board)
                if GAMEOVER:
                    print("Black won!")
                    break
                if np.all(board):
                    print("Draw!")
                    break
            if turn == WHITE:
                make_move(board, WHITE)
                print(board)
                turn = BLACK
                if GAMEOVER:
                    print("White won!")
                    break
                if np.all(board):
                    print("Draw!")
                    break
