import pygame
from constants import *


class Board():
    def __init__(self):
        self.board = []
        self.selected_piece = None

    def draw_cubes(self, window):
        window.fill(BLACK)

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
                    pygame.draw.rect(window, TAN, (col * 40, row * 40, 40, 40))
                else:
                    pygame.draw.rect(
                        window, BROWN, (col * 40, row * 40, 40, 40)
                    )
