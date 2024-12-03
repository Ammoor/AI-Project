import pygame
import sys
from draw_board import draw_chessboard

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CheckMate AI")
pygame.display.set_icon(pygame.image.load("assets/images/fav_icon.png"))

def main():
    # Main loop for the program
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the chessboard
        draw_chessboard(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second
if __name__ == "__main__":
    main()
