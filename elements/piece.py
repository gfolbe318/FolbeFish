from constants import *
import os


class Piece():
    def __init__(self, label: str):
        self.label = label

        self.color = PieceColor.BLACK if label.islower() else PieceColor.WHITE
        self.piecename = fen_piecename_dict[label.lower()]
        self.value = value_dict[self.piecename]

        color = "w" if self.color == PieceColor.WHITE else "b"
        self.image_file = os.path.join('images', f'{color}{label.lower()}.png')

        self.rank = None
        self.file = None

    def __repr__(self):
        return self.label

    def setRank(self, rank_in):
        self.rank = rank_in

    def setFile(self, file_in):
        self.file = file_in
