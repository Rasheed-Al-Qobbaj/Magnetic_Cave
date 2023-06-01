import numpy as np
from main import is_legal
from main import is_over


# TODO: Improvement: DP Table


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


def possible_moves(board: np.ndarray) -> np.ndarray:
    moves = np.array([])
    for column in range(0, 8):
        for row in range(0, 8):
            if is_legal(board[row, column]):
                moves.append((row, column))
                break
        for row in range(7, -1, -1):
            if is_legal(board[row, column]) and not moves.__contains__((row, column)):
                moves.append((row, column))
                break
    return moves


def mini_max(depth_limit, max_turn, board, depth=0):
    if depth == depth_limit or is_over(board, 1):  # 1 will be changed prolly
        return evaluate(board)

    if max_turn:
        max_eval = -np.inf
        best_move = None

        for move in possible_moves(board):
            board[move] = 1
            eval, tmp = mini_max(depth_limit, False, board, depth + 1)
            board[move] = 0

            if eval > max_eval:
                best_move = move

            max_eval = max(max_eval, eval)

        return max_eval, best_move
    else:
        min_eval = np.inf
        best_move = None
        for move in possible_moves(board):
            board[move] = -1
            eval, tmp = mini_max(depth_limit, True, board, depth + 1)
            board[move] = 0
            if eval < min_eval:
                best_move = move
            min_eval = min(min_eval, eval)

        return min_eval, best_move


def make_move(board: np.ndarray, turn):
    move_value, move = mini_max(3, True, board)
    board[move] = turn
