def print_board(board):
    for i in range(8):
        print("  +---+---+---+---+---+---+---+---+")
        print(8 - i, end=" ")
        for j in range(8):
            print("| " + board[i][j] + " ", end="")
        print("|")
    print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h")

board2 = [[" " for x in range(8)] for y in range(8)]

def get_move():
    while True:
        move = input("Enter your move (e.g. e2e4): ")
        if len(move) != 2:
            print("Invalid move: move should be 4 characters long (e.g. e2e4)")
            continue
        if not move[0].isalpha() or not move[1].isdigit():
            print("Invalid move: move should be in algebraic notation (e.g. e2)")
            continue
        return move


def make_move(board, move):
    to_file, to_rank = move
    to_file = ord(to_file) - ord('a')
    to_rank = 8 - int(to_rank)
    piece = board[from_rank][from_file]
    board[from_rank][from_file] = " "
    board[to_rank][to_file] = 'B'

if __name__ == '__main__':
    print_board(board2)
    while True:
        move = get_move()
        make_move(board2, move)
        print_board(board2)
        move = get_move()
        make_move(board2, move)