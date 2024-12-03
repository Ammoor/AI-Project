import pygame

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 600 // 8  # Adjust based on the screen width
COLOR_1 = (216, 186, 134)  # Beige
COLOR_2 = (79, 43, 26)  # Brown

# Load chess piece images
piece_images = {
    'white_pawn': pygame.image.load("assets/images/white_pawn.png"),
    'black_pawn': pygame.image.load("assets/images/black_pawn.png"),
    'white_rook': pygame.image.load("assets/images/white_rook.png"),
    'black_rook': pygame.image.load("assets/images/black_rook.png"),
    'white_knight': pygame.image.load("assets/images/white_knight.png"),
    'black_knight': pygame.image.load("assets/images/black_knight.png"),
    'white_bishop': pygame.image.load("assets/images/white_bishop.png"),
    'black_bishop': pygame.image.load("assets/images/black_bishop.png"),
    'white_queen': pygame.image.load("assets/images/white_queen.png"),
    'black_queen': pygame.image.load("assets/images/black_queen.png"),
    'white_king': pygame.image.load("assets/images/white_king.png"),
    'black_king': pygame.image.load("assets/images/black_king.png")
}

# Initial board setup with pieces 
initial_board = [
    ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
    ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn'],
    ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'],
    ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'],
    ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'],
    ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty'],
    ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn'],
    ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

def draw_chessboard(screen):
    # Draws an 8x8 chessboard
    for row in range(8):
        for col in range(8):
            # Alternate between COLOR_1 and COLOR_2 squares
            color = COLOR_1 if (row + col) % 2 == 0 else COLOR_2
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

            # Draw the piece if there is one
            piece = initial_board[row][col]
            if piece != 'empty':
                piece_image = piece_images.get(piece)
                # Scale the image to fit the tile size (80% of the tile size)
                scaled_size = int(TILE_SIZE * 0.8)  # 80% of the tile size
                piece_image = pygame.transform.scale(piece_image, (scaled_size, scaled_size))
                # Position the image at the center of the tile
                screen.blit(piece_image, (col * TILE_SIZE + (TILE_SIZE - scaled_size) // 2, row * TILE_SIZE + (TILE_SIZE - scaled_size) // 2))


