import numpy as np

# board = np.array([0, 1, 0, -1, 1])
#
# print(board)
# print(np.count_nonzero(board == -1))

def score(board):
    score = 0
    for row in range(4, 8):
        for column in range(0, 4):
            window = board[row - 4:row + 1, column:column + 5]
            score += 1 * window[0, 0] + 2 * window[1, 1] + 3 * window[2, 2] + 2 * window[3, 3] + 1 * window[4, 4]
            score += 1 * window[4, 0] + 2 * window[3, 1] + 3 * window[2, 2] + 2 * window[1, 3] + 1 * window[0, 4]
            if (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == 5 or (window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == 5:
                score = 100000
            elif (window[0, 0] + window[1, 1] + window[2, 2] + window[3, 3] + window[4, 4]) == -5 or (window[4, 0] + window[3, 1] + window[2, 2] + window[1, 3] + window[0, 4]) == -5:
                score = -100000
            elif np.count_nonzero(window == 1) == 4 and np.count_nonzero(window == 0) == 1:
                score += 50
    return score


board = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

print(score(board))
