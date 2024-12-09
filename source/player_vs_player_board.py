import pygame
import sys

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
X_COLOR = (220, 20, 60)
O_COLOR = (30, 144, 255)

# Define fonts
font_title = pygame.font.Font(None, 60)
font_button = pygame.font.Font(None, 40)
font_symbol = pygame.font.Font(None, 80)

# Global variables
player_x = ""
player_o = ""
current_turn = "X"  # Start with player 'X'
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 grid


def draw_text(text, font, color, x, y, center=True):
    # Helper function to draw text on the screen.
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)


def player_selection_screen():
    # Screen where players select who will play as X and O.
    global player_x, player_o
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Select Players", font_title, BLACK, WIDTH // 2, 50)
        draw_text("Who will be 'X'?", font_button, BLACK, WIDTH // 2, 150)

        # Buttons for Player 1 and Player 2
        player1_button = pygame.Rect(WIDTH // 2 - 150, 200, 300, 60)
        player2_button = pygame.Rect(WIDTH // 2 - 150, 300, 300, 60)

        pygame.draw.rect(screen, BLUE, player1_button, border_radius=10)
        pygame.draw.rect(screen, GREEN, player2_button, border_radius=10)
        draw_text("Player 1", font_button, WHITE,
                  player1_button.centerx, player1_button.centery)
        draw_text("Player 2", font_button, WHITE,
                  player2_button.centerx, player2_button.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if player1_button.collidepoint(mouse_pos):
                    player_x = "Player 1"
                    player_o = "Player 2"
                    running = False
                elif player2_button.collidepoint(mouse_pos):
                    player_x = "Player 2"
                    player_o = "Player 1"
                    running = False

        pygame.display.flip()

    # Proceed to the game board
    game_board_screen()


def draw_board():
    cell_size = WIDTH // 3
    for row in range(3):
        for col in range(3):
            cell_rect = pygame.Rect(
                col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, cell_rect,
                             width=5)  # Draw grid lines

            # Draw X or O in the cell
            if board[row][col] == "X":
                draw_text("X", font_symbol, X_COLOR,
                          cell_rect.centerx, cell_rect.centery)
            elif board[row][col] == "O":
                draw_text("O", font_symbol, O_COLOR,
                          cell_rect.centerx, cell_rect.centery)


def game_board_screen():
    # Main game screen with the 3x3 board.
    global current_turn
    cell_size = WIDTH // 3

    while True:
        screen.fill(WHITE)

        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = mouse_pos[1] // cell_size, mouse_pos[0] // cell_size

                # Place X or O if the cell is empty
                if board[row][col] == "":
                    board[row][col] = current_turn
                    current_turn = "O" if current_turn == "X" else "X"  # Switch turns

        pygame.display.flip()


def pvp_board():
    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            player_selection_screen()

        pygame.display.flip()


if __name__ == "__main__":
    pvp_board()
