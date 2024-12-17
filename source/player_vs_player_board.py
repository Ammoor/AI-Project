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
X_COLOR = (220, 20, 60)
O_COLOR = (30, 144, 255)
RED = (255, 0, 0)

# Define fonts
font_title = pygame.font.Font(None, 60)
font_button = pygame.font.Font(None, 40)
font_symbol = pygame.font.Font(None, 80)
font_message = pygame.font.Font(None, 50)

# Global variables
player_x = ""
player_o = ""
current_turn = "X"  # Start with player 'X'
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 grid


def draw_text(text, font, color, x, y, center=True):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)


def player_selection_screen():
    global player_x, player_o, current_turn
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Select Players", font_title, BLACK, WIDTH // 2, 50)
        draw_text("Who will be 'X'?", font_button, BLACK, WIDTH // 2, 150)

        player1_button = pygame.Rect(WIDTH // 2 - 150, 200, 300, 60)
        player2_button = pygame.Rect(WIDTH // 2 - 150, 300, 300, 60)

        pygame.draw.rect(screen, BLUE, player1_button, border_radius=10)
        pygame.draw.rect(screen, GREEN, player2_button, border_radius=10)
        draw_text("Player 1", font_button, WHITE, player1_button.centerx, player1_button.centery)
        draw_text("Player 2", font_button, WHITE, player2_button.centerx, player2_button.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if player1_button.collidepoint(mouse_pos):
                    player_x = "Player 1"
                    player_o = "Player 2"
                    current_turn = "X"  # Player 1 starts as X
                    running = False
                elif player2_button.collidepoint(mouse_pos):
                    player_x = "Player 2"
                    player_o = "Player 1"
                    current_turn = "O"  # Player 2 starts as X
                    running = False

        pygame.display.flip()

    game_board_screen()


def draw_board():
    cell_size = WIDTH // 3
    for row in range(3):
        for col in range(3):
            cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, cell_rect, width=5)

            if board[row][col] == "X":
                draw_text("X", font_symbol, X_COLOR, cell_rect.centerx, cell_rect.centery)
            elif board[row][col] == "O":
                draw_text("O", font_symbol, O_COLOR, cell_rect.centerx, cell_rect.centery)


def check_winner():
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None


def is_draw():
    return all(board[row][col] != "" for row in range(3) for col in range(3))


def show_message(message):
    # Display the game result and reset the game.
    screen.fill(WHITE)
    draw_text(message, font_message, RED, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(2000)
    reset_game()


def reset_game():
    # Reset the game, including the board and turn order.
    global board, current_turn
    board = [["" for _ in range(3)] for _ in range(3)]
    current_turn = "X" if player_x == "Player 1" else "O"
    game_board_screen()


def game_board_screen():
    # Main game loop
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

                if board[row][col] == "":
                    board[row][col] = current_turn
                    winner = check_winner()
                    if winner:
                        show_message(f"{winner} Wins!")
                        return
                    elif is_draw():
                        show_message("It's a Draw!")
                        return
                    current_turn = "O" if current_turn == "X" else "X" 

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
