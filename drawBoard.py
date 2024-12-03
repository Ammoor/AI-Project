import pygame

import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TILE_SIZE = SCREEN_WIDTH // 8  # Chessboard is 8x8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chessboard")


def draw_chessboard():
    """Draws an 8x8 chessboard."""
    for row in range(8):
        for col in range(8):
            # Alternate between white and black squares
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * TILE_SIZE,
                             row * TILE_SIZE, TILE_SIZE, TILE_SIZE))


def main():
    """Main loop for the program."""
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the chessboard
        screen.fill(WHITE)  # Background
        draw_chessboard()

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second


if __name__ == "__main__":
    main()
