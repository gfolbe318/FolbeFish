import pygame
from constructs import board

if __name__ == '__main__':
    FPS = 60

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Let's play chess!")
    b = board.Board()

    run = True

    while(run):
        clock.tick(FPS)
        b.draw_cubes(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
