# TODO: 1- Change input
# TODO: 2- Use NumPy for array calculations
# TODO: 3- Create tie option in is_over()
# TODO: 4- Fix the grid labeling to the 2d list
# TODO: 5- Fix is_over() method to only check the new piece's surrounding positions

# Methods

# Method to print the grid
def grid():
    print("    A   B   C   D   E   F   G   H")
    for row in range(0, 8):
        print("  +---+---+---+---+---+---+---+---+")
        print(8 - row, "| ", end="")
        for column in range(0, 8):
            print(position[row][column], "| ", end="")
        print(8 - row)
    print("  +---+---+---+---+---+---+---+---+")
    print("    A   B   C   D   E   F   G   H")


# Method to check if the move wanted is legal
def is_legal(position, row, column):
    # Checks if the space is empty
    if position[row][column] != ' ':
        return False
    # Checks if it's at the edge of the board
    if column == coordinates['a'] or column == coordinates['h']:
        return True

    # Checks if the space behind is occupied depending on which side it's placed
    if column <= coordinates['d'] and position[row][column - 1] == " ":
        # Edge case for if in the middle and it gravitates towards the right magnet
        if column == 3 and position[row][column + 1] != ' ':
            return True
        return False
    if column >= 4 and position[row][column + 1] == " ":
        # Edge case for if in the middle and it gravitates towards the left magnet
        if column == 4 and position[row][column - 1] != ' ':
            return True
        return False

    # If no rule violation occurs then it's legal
    return True


# Method to check if the game is over
def is_over(position, char):
    # Checking for 5 in a row vertically
    # Checks all the possible places a 5 in a row could start
    for column in range(0, 8):
        for row in range(0, 4):
            if position[row][column] == char \
                    and position[row + 1][column] == char \
                    and position[row + 2][column] == char \
                    and position[row + 3][column] == char \
                    and position[row + 4][column] == char:
                return True

    # Checking for 5 in a row horizontally
    # Checks all the possible places a 5 in a row could start
    for row in range(0, 8):
        for column in range(0, 4):
            if position[row][column] == char \
                    and position[row][column + 1] == char \
                    and position[row][column + 2] == char \
                    and position[row][column + 3] == char \
                    and position[row][column + 4] == char:
                return True

    # Checking for 5 in a row positively diagonal
    # Checks all the possible places a 5 in a row could start
    for row in range(4, 8):
        for column in range(0, 4):
            if position[row][column] == char \
                    and position[row - 1][column + 1] == char \
                    and position[row - 2][column + 2] == char \
                    and position[row - 3][column + 3] == char \
                    and position[row - 4][column + 4] == char:
                return True

    # Checking for 5 in a row horizontally
    # Checks all the possible places a 5 in a row could start
    for row in range(0, 4):
        for column in range(0, 4):
            if position[row][column] == char \
                    and position[row + 1][column + 1] == char \
                    and position[row + 2][column + 2] == char \
                    and position[row + 3][column + 3] == char \
                    and position[row + 4][column + 4] == char:
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

# Hashmap for relating the character values to integers
coordinates = {
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
BLACK = 0
WHITE = 1
turn = BLACK
GAMEOVER = False

# Start of the game
print("Instructions:")
print("1- Please enter the row as the integer shown on the grid.")
print("2- Please enter the column as the letter shown on the grid.")
grid()

while not GAMEOVER:
    # Prints whose turn it is and gets the coordinates for the place they wish to place the piece
    if turn == BLACK:
        print("Black")
        # -1 To relate the integers on the grid with the array since it starts from 0
        row = int(input("Please enter the row:")) - 1
        # Casefold lower-cases the input so no common input errors occur
        temp = str.casefold(input("Please enter the column:"))
        if coordinates.__contains__(temp):
            # Gets the value from the Hashmap based on the key entered
            column = coordinates[temp]
            if is_legal(position, row, column):
                position[row][column] = "□"
                turn = WHITE
                GAMEOVER = is_over(position, "□")
            else:
                print("Illegal move, Try again!")
        else:
            print("Wrong Column, Try again!")
        grid()
        if GAMEOVER:
            print("Black won!")
            break
    if turn == WHITE:
        print("White")
        row = int(input("Please enter the row:")) - 1
        temp = str.casefold(input("Please enter the column:"))
        if coordinates.__contains__(temp):
            column = coordinates[temp]
            if is_legal(position, row, column):
                position[row][column] = "■"
                turn = BLACK
                GAMEOVER = is_over(position, "■")
            else:
                print("Illegal move, Try again!")
        else:
            print("Wrong Column, Try again!")
        grid()
        if GAMEOVER:
            print("White won!")
            break
