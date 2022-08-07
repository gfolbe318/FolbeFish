from enum import Enum

DIMENSION = 8

SQUARE_SIZE = 60

TOP_OFFSET = 60
LEFT_OFFSET = 160


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
