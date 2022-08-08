import pygame
from constants import *
from elements import board, game, piece
from utils import *

if __name__ == '__main__':
    FPS = 60

    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Let's play chess!")

    b = board.Board()
    b.load_images()

    g = game.Game(b)

    run = True

    src_row, src_col, dst_row, dst_col = None, None, None, None
    selected_piece, selected_image = None, None
    mouse_state = MouseState.MOUSE_UP

    while(run):
        clock.tick(FPS)
        b.draw_squares(window)
        b.draw_pieces(window)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_state = MouseState.MOUSE_DOWN

                # Get source coordinates
                src_row, src_col = get_board_coordinates(
                    pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                # Select the piece and temporarily remove it from the destination square
                # If the src row is valid, select the piece if it exists
                if src_row != None:
                    selected_piece = b.board[src_row][src_col]
                    b.board[src_row][src_col] = "-"

                    if selected_piece != '-':
                        selected_image = b.images[selected_piece.label]

                    else:
                        selected_piece = None
                        selected_image = None

            # When the button is released, reset the mouse state to be up
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_state = MouseState.MOUSE_UP

                if selected_piece != None:

                    # Get coordinates when mouse is released
                    dst_row, dst_col = get_board_coordinates(
                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                    # If the dst row is valid, draw the image at the correct square
                    # and modify the board to have updated pieces
                    if dst_row != None:
                        window.blit(selected_image,
                                    (HORIZ_OFFSET + dst_col * SQUARE_SIZE,
                                     VERT_OFFSET + dst_row * SQUARE_SIZE,
                                     SQUARE_SIZE,
                                     SQUARE_SIZE))

                        b.board[dst_row][dst_col] = selected_piece

                        # only update board if square changed
                        if(src_row != dst_row and src_col != dst_col):
                            b.board[src_row][src_col] = '-'

                    # If the dst row is invalid, redraw the image where it originally was
                    # and modify the board to have updated pieces
                    else:
                        window.blit(selected_image,
                                    (HORIZ_OFFSET + src_col * SQUARE_SIZE,
                                     VERT_OFFSET + src_row * SQUARE_SIZE,
                                     SQUARE_SIZE,
                                     SQUARE_SIZE))

                        b.board[src_row][src_col] = selected_piece

                # Reset selected piece as the attempted move was unsuccessful
                selected_piece = None
                selected_image = None

        # logic for click and drag. Needs to be outside of loop so we aren't waiting for an event
        if (event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN) and \
                mouse_state == MouseState.MOUSE_DOWN and selected_piece != None:

            window.blit(selected_image,
                        (pygame.mouse.get_pos()[0] - SQUARE_SIZE/2,
                         pygame.mouse.get_pos()[1] - SQUARE_SIZE/2,
                         SQUARE_SIZE,
                         SQUARE_SIZE)
                        )

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
