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
# Klasa dla planszy
class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = []
        for row in range(ROWS):
            board.append([])
            for col in range(COLS):
                if (row + col) % 2 != 0:  # Tylko ciemne pola
                    if row < 3:
                        board[row].append(Piece(RED))  # Pionki czerwone
                    elif row > 4:
                        board[row].append(Piece(BLUE))  # Pionki niebieskie
                    else:
                        board[row].append(None)  # Puste pole
                else:
                    board[row].append(None)  # Puste pole
        return board

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece:
                    piece_color = piece.color
                    pygame.draw.circle(screen, piece_color, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)
                    if piece.is_king:
                        pygame.draw.circle(screen, GOLD, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 20, 3)


# Tworzenia planszy
class Piece:
    def __init__(self, color, is_king=False):
        self.color = color
        self.is_king = is_king

    def make_king(self):
        self.is_king = True

# Klasa dla planszy
class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = []
        for row in range(ROWS):
            board.append([])
            for col in range(COLS):
                if (row + col) % 2 != 0:  # Tylko ciemne pola
                    if row < 3:
                        board[row].append(Piece(RED))  # Pionki czerwone
                    elif row > 4:
                        board[row].append(Piece(BLUE))  # Pionki niebieskie
                    else:
                        board[row].append(None)  # Puste pole
                else:
                    board[row].append(None)  # Puste pole
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
class Game:
    def __init__(self):
        self.board = Board()
        self.selected_piece = None
        self.turn = RED
        self.font = pygame.font.Font(None, 74)

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected_piece = (row, col)

    def move_selected_piece(self, row, col):
        if self.selected_piece:
            from_row, from_col = self.selected_piece
            self.board.move_piece(from_row, from_col, row, col)
            self.selected_piece = None
            self.turn = BLUE if self.turn == RED else RED

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
            if self.selected_piece:
                self.move_selected_piece(row, col)
            else:
                self.select_piece(row, col)

    def draw(self, screen):
        self.board.draw(screen)

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
