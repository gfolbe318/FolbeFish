from tkinter import LEFT
import pygame
from constants import *
from elements.piece import Piece


class Board():
    def __init__(self):
        self.board = [
            [Piece('r'), Piece('n'), Piece('b'), Piece('k'),
             Piece('q'), Piece('b'), Piece('n'), Piece('r')],
            [Piece('p'), Piece('p'), Piece('p'), Piece('p'),
             Piece('p'), Piece('p'), Piece('p'), Piece('p')],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            [Piece('P'), Piece('P'), Piece('P'), Piece('P'),
             Piece('P'), Piece('P'), Piece('P'), Piece('P')],
            [Piece('R'), Piece('N'), Piece('B'), Piece('K'),
             Piece('Q'), Piece('B'), Piece('N'), Piece('R')],
        ]

        for rank in range(DIMENSION):
            for file in range(DIMENSION):
                if self.board[rank][file] != '-':
                    self.board[rank][file].setRank(rank)
                    self.board[rank][file].setFile(file)

        self.images = {}

    def __repr__(self):
        for rank in range(DIMENSION):
            for file in range(DIMENSION):

                end_char = "\n" if file == DIMENSION - 1 else "  "
                print(self.board[rank][file], end=end_char)

        return ""

    # Adding this function because the __repr__ wasn't doing its job
    def pretty_print(self):
        for rank in range(DIMENSION):
            for file in range(DIMENSION):

                end_char = "\n" if file == DIMENSION - 1 else "  "
                print(self.board[rank][file], end=end_char)

        print("\n")

    def draw_squares(self, window):
        window.fill(pygame.Color('black'))

        colors = [pygame.Color(0, 122, 122), pygame.Color('white')]

        for row in range(DIMENSION):
            for col in range(DIMENSION):
                color = colors[(row + col) % 2]

                pygame.draw.rect(
                    window, color, (HORIZ_OFFSET + col * SQUARE_SIZE,
                                    VERT_OFFSET + row * SQUARE_SIZE,
                                    SQUARE_SIZE,
                                    SQUARE_SIZE)
                )

    def load_images(self):
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if self.board[row][col] != '-':
                    piece = self.board[row][col]
                    filepath = piece.image_file
                    label = piece.label

                    image = pygame.transform.scale(
                        pygame.image.load(filepath), (SQUARE_SIZE, SQUARE_SIZE))

                    self.images[label] = image

    def draw_pieces(self, window):
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if self.board[row][col] != '-':

                    image = self.images[self.board[row][col].label]
                    window.blit(image, (HORIZ_OFFSET + col * SQUARE_SIZE,
                                        VERT_OFFSET + row * SQUARE_SIZE,
                                        SQUARE_SIZE,
                                        SQUARE_SIZE))
