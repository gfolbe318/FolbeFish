from enum import Enum

# Colors used
BROWN = (60, 30, 0)
TAN = (210, 180, 140)
BLACK = (0, 0, 0)

NUM_ROWS = 8
NUM_COLS = 8


class PieceColor(Enum):
    WHITE = 0
    BLACK = 1


class PieceName(Enum):
    PAWN = 0
    BISHOP = 1
    KNIGHT = 2
    ROOK = 3
    QUEEN = 4
    KING = 5


fen_piecename_dict = {
    'p': PieceName.PAWN,
    'b': PieceName.BISHOP,
    'n': PieceName.KNIGHT,
    'r': PieceName.ROOK,
    'q': PieceName.QUEEN,
    'k': PieceName.KING
}

value_dict = {
    PieceName.PAWN: 1,
    PieceName.BISHOP: 3,
    PieceName.KNIGHT: 3,
    PieceName.ROOK: 5,
    PieceName.QUEEN: 9,
    PieceName.KING: 100
}
