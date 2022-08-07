import pygame
from constants import SQUARE_SIZE
from elements import board
import os

if __name__ == '__main__':
    FPS = 60

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Let's play chess!")

    b = board.Board()
    b.load_images()

    run = True

    while(run):
        clock.tick(FPS)
        b.draw_squares(window)

        b.draw_pieces(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
