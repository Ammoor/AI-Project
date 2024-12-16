import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 3
LINE_WIDTH = 10
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = CELL_SIZE // 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XO Game")

# Initialize the board
board = [['' for _ in range(3)] for _ in range(3)]

# Characters for player and PC
player_char = ''
pc_char = ''

# Fonts
font = pygame.font.Font(None, 60)


def draw_grid():
    # Draw the grid for the game.
    screen.fill(WHITE)
    for row in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * row),
                         (WIDTH, CELL_SIZE * row), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (CELL_SIZE * row, 0),
                         (CELL_SIZE * row, HEIGHT), LINE_WIDTH)


def draw_marks():
    # Draw the marks (X and O) on the board.
    for row in range(3):
        for col in range(3):
            x, y = col * CELL_SIZE, row * CELL_SIZE
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (x + SPACE, y + SPACE),
                                 (x + CELL_SIZE - SPACE, y + CELL_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, (x + SPACE, y + CELL_SIZE - SPACE),
                                 (x + CELL_SIZE - SPACE, y + SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen, BLUE, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)


def is_winner(char):
    # Check if a character has won the game.
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == char for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == char for row in range(3)):
            return True
    if all(board[i][i] == char for i in range(3)) or all(board[i][2 - i] == char for i in range(3)):
        return True
    return False


def is_draw():
    # Check if the game is a draw.
    return all(board[row][col] != '' for row in range(3) for col in range(3))


def minimax(depth, is_maximizing):
    # Minimax algorithm for the computer's move.
    if is_winner(pc_char):
        return 10 - depth
    if is_winner(player_char):
        return depth - 10
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = pc_char
                    score = minimax(depth + 1, False)
                    board[row][col] = ''
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = player_char
                    score = minimax(depth + 1, True)
                    board[row][col] = ''
                    best_score = min(best_score, score)
        return best_score


def pc_move():
    # Make the computer's move.
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = pc_char
                score = minimax(0, False)
                board[row][col] = ''
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        row, col = best_move
        board[row][col] = pc_char
        if is_winner(pc_char):
            show_message("PC Wins!")
        elif is_draw():
            show_message("It's a Draw!")


def show_message(message):
    # Display the game result and reset the game.
    text = font.render(message, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(WHITE)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    reset_game()


def reset_game():
    # Reset the game.
    global board
    board = [['' for _ in range(3)] for _ in range(3)]
    draw_grid()


def player_move(row, col):
    # Handle the player's move.
    if board[row][col] == '':
        board[row][col] = player_char
        if is_winner(player_char):
            show_message("You Win!")
        elif is_draw():
            show_message("It's a Draw!")
        else:
            pc_move()


def get_cell(pos):
    # Get the board cell based on mouse position.
    x, y = pos
    row, col = y // CELL_SIZE, x // CELL_SIZE
    return row, col


def main():
    # Main game loop.
    global player_char, pc_char
    clock = pygame.time.Clock()
    draw_grid()

    # Character selection
    selecting = True
    while selecting:
        screen.fill(WHITE)
        text_x = font.render("Play as X", True, RED)
        text_o = font.render("Play as O", True, BLUE)
        screen.blit(
            text_x, (WIDTH // 4 - text_x.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(text_o, (3 * WIDTH // 4 -
                    text_o.get_width() // 2, HEIGHT // 2 - 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if WIDTH // 4 - text_x.get_width() // 2 <= event.pos[0] <= WIDTH // 4 + text_x.get_width() // 2:
                    player_char, pc_char = 'X', 'O'
                    selecting = False
                elif 3 * WIDTH // 4 - text_o.get_width() // 2 <= event.pos[0] <= 3 * WIDTH // 4 + text_o.get_width() // 2:
                    player_char, pc_char = 'O', 'X'
                    selecting = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                row, col = get_cell(event.pos)
                player_move(row, col)

        draw_grid()
        draw_marks()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
