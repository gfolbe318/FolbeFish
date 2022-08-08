from constants import *


def get_board_coordinates(x, y):
    col = (x - HORIZ_OFFSET) // SQUARE_SIZE
    row = (y - VERT_OFFSET) // SQUARE_SIZE

    if col < 0 or col > DIMENSION - 1 or row < 0 or row > DIMENSION - 1:
        return (None, None)
    else:
        return (row, col)
