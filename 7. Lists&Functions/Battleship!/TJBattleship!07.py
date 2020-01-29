from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board_in):
    for row in board_in:
        print (" ".join(row))


# Add your code below!

def random_row(board_in):
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    return randint(0, len(board_in) - 1)


random_row(board)
random_col(board)
