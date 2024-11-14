# Whack-a-mole!

import pygame
import random
mole_image = pygame.image.load('mole.png')


def main():
    try:
        pygame.init()
        # You can draw the mole with the snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft = (x.y))
        # mole_image = pygame.image.load('mole.png')
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        def draw_grid():
        # draw horizontal lines
            for i in range(1, BOARD_ROWS):
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (HEIGHT, i * SQUARE_SIZE),
                )

            # draw vertical lines
            for i in range(1, BOARD_COLS):
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, WIDTH),
                )

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mouse_x // 32 == mouse_x // 32 and mouse_y // 32 == mouse_y // 32:
                        mole_x = random.randrange(0, BOARD_COLS) *32 +3
                        mole_y = random.randrange(0, BOARD_ROWS) *32 +3
            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, (mole_x, mole_y))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


LINE_COLOR = (0, 0, 0)
SQUARE_SIZE = 32
WIDTH = 512
HEIGHT = 640
LINE_WIDTH = 1
BOARD_ROWS = 16
BOARD_COLS = 20


if __name__ == "__main__":
    main()