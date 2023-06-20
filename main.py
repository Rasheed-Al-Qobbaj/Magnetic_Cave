import numpy as np
import time


def evaluate(board) -> int:
    window = np.array([0] * 5)  # Sliding Window of 5 

    score = 0  # Score of the board currently
    # Horizontal windows of 5  checked 
    for row in range(0, 8):
        for column in range(0, 4):
            window = board[row, column:column + 5]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[
                4]  # Score of the window
            if (window[0] + window[1] + window[2] + window[3] + window[4]) == 5:  # If 5 in a row of BLACK
                score += 100000
            elif (window[0] + window[1] + window[2] + window[3] + window[4]) == -5:  # If 5 in a row of WHITE
                score += -100000
    # Vertical windows of 5 checked 
    for column in range(0, 8):
        for row in range(0, 4):
            window = board[row:row + 5, column]
            score += 1 * window[0] + 2 * window[1] + 3 * window[2] + 2 * window[3] + 1 * window[
                4]  # Score of the window
            if row > 0:
                if window[row - 1] == window[row] and window[row + 1] == window[row]:
                    score += (50 * window[row])
            if (window[0] + window[1] + window[2] + window[3] + window[4]) == 5:  # If 5 in a row of BLACK
                score += 100000
            elif (window[0] + window[1] + window[2] + window[3] + window[4]) == -5:  # If 5 in a row of WHITE
                score += -100000
    # Diagonal windows of 5 checked
    for row in range(4, 8):
        for column in range(0, 4):
            window = board[row - 4:row + 1, column:column + 5]
            score += 1 * window[0, 0] + 2 * window[1, 1] + 3 * window[2, 2] + 2 * window[3, 3] + 1 * window[
                4, 4]  # Score of the window diagonally positive
            score += 1 * window[4, 0] + 2 * window[3, 1] + 3 * window[2, 2] + 2 * window[1, 3] + 1 * window[
                0, 4]  # Score of the window diagonally negative
            if (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == 5 or (
                    window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == 5:
                score += 100000
            elif (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == -5 or (
                    window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == -5:
                score += -100000
    return score


def possible_moves(board: np.ndarray):  # Returns a set of possible moves
    moves = set()  # Set of possible moves
    for row in range(0, 8):
        for column in range(0, 8):
            if is_legal(row, column):  # If the move is legal
                moves.add((row, column))  # Add it to the set
                break
        for column in range(7, -1, -1):
            if is_legal(row, column):
                moves.add((row, column))
                break

    return list(moves)


def mini_max(current_board_position, depth_limit: int, max_turn: bool, depth: int, alpha,
             beta):  # Minimax algorithm with alpha beta pruning
    if max_turn:  # If it's the max turn then the turn is 1
        turn = 1
    else:  # If it's the min turn then the turn is -1
        turn = -1

    if depth == depth_limit:  # If the depth limit is reached then return the evaluation of the board and the board
        # print("Depth Limit Reached")
        return evaluate(current_board_position), current_board_position,

    elif is_over(current_board_position, turn):
        # print("--------------Is Over-----------------")
        return evaluate(current_board_position), current_board_position
    if max_turn:
        max_eval = -np.inf  # Max evaluation of the board
        best_move = [(0, 0)]

        for move in possible_moves(current_board_position):
            current_board_position[move[0], move[1]] = 1  # simulate the move
            evaluation, tmp = mini_max(current_board_position, depth_limit, False, (depth + 1), alpha, beta)

            # print("MAX EVAL = ", evaluation, "DEPTH = ", depth)
            # print(".", end="")
            current_board_position[move[0], move[1]] = 0  # undo the simulation
            max_eval = max(max_eval, evaluation)  # Max evaluation of the board

            if evaluation == max_eval:
                best_move = move

            alpha = max(alpha, max_eval)  # Alpha Beta Pruning

            if alpha >= beta:  # Pruning
                break

        return max_eval, best_move  # return the best move and the evaluation of the board
    else:

        min_eval = np.inf  # Min evaluation of the board
        best_move = [(0, 0)]  # dummy move

        for move in possible_moves(current_board_position):  # For all the possible moves
            current_board_position[move[0], move[1]] = -1  # simulate the move
            evaluation, tmp = mini_max(current_board_position, depth_limit, True, (depth + 1), alpha,
                                       beta)  # Recursively call the minimax algorithm
            current_board_position[move[0], move[1]] = 0  # undo the simulation
            min_eval = min(min_eval, evaluation)  # Min evaluation of the board

            if evaluation == min_eval:  # If the evaluation is the minimum evaluation
                best_move = move

            beta = min(beta, min_eval)

            if beta <= alpha:
                break

        return min_eval, best_move  # return the best move and the evaluation of the board


def make_move(board: np.ndarray, turn):  # Makes a move based on the minimax algorithm
    if turn == 1:  # If it's the max turn then the turn is 1
        max_turn = False
    else:  # If it's the min turn then the turn is -1
        max_turn = True

    move_eval, move_position = mini_max(board, 3, max_turn, 0, alpha=-np.inf,
                                        beta=np.inf)  # Minimax algorithm with alpha beta pruning
    row = move_position[0]  # Get the row and column of the move
    column = move_position[1]  # Get the row and column of the move
    board[row, column] = turn  # Place the piece on the board
    # print(row, column)
    if turn == BLACK:
        position[row][column] = "□"  # Place the piece on the grid
    else:
        position[row][column] = "■"  # Place the piece on the grid


#

# Method to print the grid
def print_grid():  # Prints the grid
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
def is_legal(row, column):  # Checks if the move is legal
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
def is_over(board, turn):  # Checks if the game is over
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


def ascii():  # Prints the ascii art
    print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

    """)
    print("""


████████╗░█████╗░
╚══██╔══╝██╔══██╗
░░░██║░░░██║░░██║
░░░██║░░░██║░░██║
░░░██║░░░╚█████╔╝
░░░╚═╝░░░░╚════╝░    

    """)

    print("""

███╗░░░███╗░█████╗░░██████╗░███╗░░██╗███████╗████████╗██╗░█████╗    ░░█████╗░░█████╗░██╗░░░██╗███████╗
████╗░████║██╔══██╗██╔════╝░████╗░██║██╔════╝╚══██╔══╝██║██╔══██╗   ██╔══██╗██╔══██╗██║░░░██║██╔════╝
██╔████╔██║███████║██║░░██╗░██╔██╗██║█████╗░░░░░██║░░░██║██║░░╚═╝   ██║░░╚═╝███████║╚██╗░██╔╝█████╗░░
██║╚██╔╝██║██╔══██║██║░░╚██╗██║╚████║██╔══╝░░░░░██║░░░██║██║░░██╗   ██║░░██╗██╔══██║░╚████╔╝░██╔══╝░░
██║░╚═╝░██║██║░░██║╚██████╔╝██║░╚███║███████╗░░░██║░░░██║╚█████╔╝   ╚█████╔╝██║░░██║░░╚██╔╝░░███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝ ░╚════╝   ░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
    """)


if __name__ == '__main__':  # Main method to run the game
    # Initialized Variables

    # Game grid positions for the pieces
    position = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # Mathematical grid
    board = np.zeros((8, 8))  # 8x8 grid

    # Hashmap for relating the character values to integers for the columns
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
    GAMEOVER = False  # Game over flag

    ascii()  # Prints the ascii art

    # Start of the game
    print('Select Game Mode:')
    print('1. Player vs Player')
    print('2. Player [BLACK] vs AI [WHITE] ')
    print('3. Player [WHITE] vs AI [BLACK] ')

    choice = input('Enter your choice: ')  # Gets the choice from the user
    if len(choice) == 1 and 48 <= ord(choice) <= 57:  # Checks the input  if valid
        choice = int(choice)
    else:
        print("Invalid choice")

    while choice not in range(1, 4):  # Checks the input  if valid
        choice = input('Enter your choice: ')
        if len(choice) == 1 and 48 <= ord(choice) <= 57:
            choice = int(choice)
        else:
            print("Invalid choice")

    print_grid()

    if choice == 1:
        while not GAMEOVER:  # While the game is not over
            # Prints whose turn it is and gets the columns for the place they wish to place the piece
            if turn == BLACK:
                print("Black")
                coordinate = input("Please enter the coordinate (Ex. a1):")  # Gets the coordinate from the user
                if len(coordinate) != 2 or not 48 < ord(coordinate[1]) < 57:  # To check for repeated characters
                    print("Incorrect input, Try again!")
                else:
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
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("Black won!")
                        print('==============================================')
                        break
                    if np.all(board):
                        print("Draw!")
                        break
            if turn == WHITE:
                print("White")
                coordinate = input("Please enter the coordinate (Ex. a1):")
                if len(coordinate) != 2 or not 48 < ord(coordinate[1]) < 57:
                    print("Incorrect input, Try again!")
                else:
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
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("White won!")
                        print('==============================================')
                        break
                    if np.all(board):
                        print("Draw!")
                        break

    elif choice == 2:  # Player vs AI
        while not GAMEOVER:
            # Prints whose turn it is and gets the columns for the place they wish to place the piece
            if turn == BLACK:
                print("Black")
                coordinate = input("Please enter the coordinate (Ex. a1):")
                if len(coordinate) != 2 or not 48 < ord(coordinate[1]) < 57:
                    print("Incorrect input, Try again!")
                else:
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
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("Black won!")
                        print('==============================================')
                        break
                    if np.all(board):
                        print("Draw!")
                        break
            if turn == WHITE:
                print("Loading Move")
                timer_start = time.time()
                make_move(board, WHITE)
                GAMEOVER = is_over(board, WHITE)
                # print('test1')
                print_grid()
                print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                timer_end = time.time()
                print(f'Time taken from AI = {timer_end - timer_start} Seconds')

                # print(board)

                turn = BLACK
                if GAMEOVER:
                    print('==============================================')
                    print("White won!")
                    print('==============================================')
                    break
                if np.all(board):
                    print("Draw!")
                    break

    elif choice == 3:
        while not GAMEOVER:
            # Prints whose turn it is and gets the columns for the place they wish to place the piece
            if turn == WHITE:
                print("white")
                coordinate = input("Please enter the coordinate (Ex. a1):")
                if len(coordinate) != 2 or not 48 < ord(coordinate[1]) < 57:
                    print("Incorrect input, Try again!")
                else:
                    row = int(coordinate[1]) - 1
                    # Casefold lower-cases the input so no common input errors occur
                    temp = str.casefold(coordinate[0])
                    if COULMNS.__contains__(temp) and row in range(0, 9):
                        # Gets the value from the Hashmap based on the key entered
                        column = COULMNS[temp]
                        if is_legal(row, column):
                            position[row][column] = "■"
                            board[row, column] = WHITE
                            turn = BLACK
                            GAMEOVER = is_over(board, WHITE)
                        else:
                            print("Illegal move, Try again!")
                    else:
                        print("Index wrong, Try again!")
                    print_grid()
                    print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                    # print(board)
                    if GAMEOVER:
                        print('==============================================')
                        print("White won!")
                        print('==============================================')
                        break
                    if np.all(board):
                        print("Draw!")
                        break
            if turn == BLACK:
                print("Loading Move")
                timer_start = time.time()
                make_move(board, BLACK)
                GAMEOVER = is_over(board, BLACK)
                print_grid()
                print(f'Board Evaluation +ve:BLACK, -ve(WHITE): {evaluate(board)}')
                timer_end = time.time()
                print(f'Time taken from AI = {timer_end - timer_start} Seconds')  #

                # print(board)

                turn = WHITE
                if GAMEOVER:
                    print('==============================================')
                    print("Black won!")
                    print('==============================================')
                    break
                if np.all(board):
                    print("Draw!")
                    break
    else:
        print("Invalid option")
