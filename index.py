import pygame
import sys
from source import player_vs_player_board
from source import player_vs_pc_board
# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XOTelligence")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
GRAY = (200, 200, 200)
HOVER_COLOR = (100, 100, 255)

# Define fonts
font_title = pygame.font.Font(None, 60)
font_button = pygame.font.Font(None, 40)

# Create text for buttons and title
title_text = font_title.render("Welcome to XOTelligence!", True, BLACK)
pvp_text = font_button.render("Player vs Player", True, WHITE)
pc_text = font_button.render("Player vs PC", True, WHITE)

# Button dimensions
BUTTON_WIDTH, BUTTON_HEIGHT = 250, 60
pvp_button = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH //
                         2, HEIGHT // 2 - 100), (BUTTON_WIDTH, BUTTON_HEIGHT))
pc_button = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2,
                        HEIGHT // 2 + 20), (BUTTON_WIDTH, BUTTON_HEIGHT))


def draw_main_menu():
    screen.fill(WHITE)
    # Draw title
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

    # Draw buttons
    pygame.draw.rect(screen, BLUE, pvp_button, border_radius=15)
    pygame.draw.rect(screen, GREEN, pc_button, border_radius=15)

    # Draw button text
    screen.blit(pvp_text, (pvp_button.x + (BUTTON_WIDTH - pvp_text.get_width()) //
                2, pvp_button.y + (BUTTON_HEIGHT - pvp_text.get_height()) // 2))
    screen.blit(pc_text, (pc_button.x + (BUTTON_WIDTH - pc_text.get_width()) //
                2, pc_button.y + (BUTTON_HEIGHT - pc_text.get_height()) // 2))


def main():
    # Main function to run the Pygame loop.
    running = True
    while running:
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Check for mouse click on buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(mouse_pos):
                    player_vs_player_board.pvp_board()
                elif pc_button.collidepoint(mouse_pos):
                    player_vs_pc_board.main()

        draw_main_menu()

        # Highlight button when hovered
        if pvp_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, pvp_button, border_radius=15)
            screen.blit(pvp_text, (pvp_button.x + (BUTTON_WIDTH - pvp_text.get_width()) //
                        2, pvp_button.y + (BUTTON_HEIGHT - pvp_text.get_height()) // 2))

        if pc_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, pc_button, border_radius=15)
            screen.blit(pc_text, (pc_button.x + (BUTTON_WIDTH - pc_text.get_width()) //
                        2, pc_button.y + (BUTTON_HEIGHT - pc_text.get_height()) // 2))

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
