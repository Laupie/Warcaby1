import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warcaby")

font = pygame.font.Font(None, 74)

# Rysowanie planszy
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Tworzenia planszy
def create_board():
    board = []
    for row in range(ROWS):
        board.append([])
        for col in range(COLS):
            if row % 2 != col % 2:
                if row < 3:
                    board[row].append((RED, False))  # False oznacza, że pionek nie jest damką
                elif row > 4:
                    board[row].append((BLUE, False))
                else:
                    board[row].append(0)
            else:
                board[row].append(0)
    return board

# Rysowania pionków
def draw_pieces(board):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != 0:
                color, king = piece
                pygame.draw.circle(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)
                if king:
                    pygame.draw.circle(screen, (255, 215, 0), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 20, 3)

# Poruszanie się pionkami
def move_piece(board, from_row, from_col, to_row, to_col):
    piece = board[from_row][from_col]
    board[from_row][from_col] = 0
    board[to_row][to_col] = piece

    # Promowanie na damkę
    color, king = piece
    if color == RED and to_row == ROWS - 1:
        board[to_row][to_col] = (color, True)
    elif color == BLUE and to_row == 0:
        board[to_row][to_col] = (color, True)

# Główna pętla gry
def main():
    clock = pygame.time.Clock()
    board = create_board()
    selected_piece = None
    turn = RED

    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if selected_piece:
                    row, col = selected_piece
                    new_row, new_col = row, col
                    if event.key == pygame.K_UP and row > 0:
                        new_row -= 1
                    elif event.key == pygame.K_DOWN and row < ROWS - 1:
                        new_row += 1
                    elif event.key == pygame.K_LEFT and col > 0:
                        new_col -= 1
                    elif event.key == pygame.K_RIGHT and col < COLS - 1:
                        new_col += 1

                    # Jeśli pole jest puste
                    if board[new_row][new_col] == 0:
                        move_piece(board, row, col, new_row, new_col)
                        selected_piece = None
                        turn = BLUE if turn == RED else RED

                else:
                    for row in range(ROWS):
                        for col in range(COLS):
                            if board[row][col] != 0 and board[row][col][0] == turn:
                                selected_piece = (row, col)
                                break

        draw_board()
        draw_pieces(board)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
