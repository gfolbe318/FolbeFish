from constants import *


class Piece():
    def __init__(self, label: str, rank_in, file_in):
        self.color = PieceColor.BLACK if label.islower() else PieceColor.WHITE
        self.piecename = fen_piecename_dict[label]
        self.value = value_dict[self.piecename]
        self.image_file = f'{label}.png'

        self.rank_cur = rank_in
        self.file_cur = file_in
