import numpy as np

# board = np.zeros((8, 8))
board = np.array([[1, 2, 4, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]])

if np.all(board):
    print("Nice")

print(board[0])
