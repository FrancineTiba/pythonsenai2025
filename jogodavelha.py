import pygame
import sys

# Inicializa o pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 300, 350  # Aumentei a altura para acomodar a mensagem
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 5
CROSS_WIDTH = 5
SPACE = SQUARE_SIZE // 4

# Cores
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
MSG_COLOR = (255, 255, 255)
MSG_BG_COLOR = (50, 50, 50)

# Configuração da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')
screen.fill(BG_COLOR)

# Tabuleiro
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Desenha as linhas do tabuleiro
def draw_lines():
    # Linhas horizontais
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Linhas verticais
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)

# Desenha as figuras (X e O)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                 (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                  int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                 CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                CROSS_WIDTH)

# Marca a posição no tabuleiro
def mark_square(row, col, player):
    board[row][col] = player

# Verifica se a posição está disponível
def available_square(row, col):
    return board[row][col] is None

# Verifica se o tabuleiro está cheio
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

# Verifica vitória
def check_win(player):
    # Verifica vitória nas linhas
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    
    # Verifica vitória nas colunas
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    # Verifica vitória nas diagonais
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

# Mostra mensagem de status
def draw_status_message(message):
    pygame.draw.rect(screen, MSG_BG_COLOR, (0, HEIGHT - 50, WIDTH, 50))
    font = pygame.font.SysFont('Arial', 24)
    text = font.render(message, True, MSG_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 40))

# Reinicia o jogo
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None
    draw_status_message("Vez do Jogador X")

# Jogo principal
def main():
    draw_lines()
    
    player = 'X'  # X começa
    game_over = False
    draw_status_message("Vez do Jogador X")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    player = 'X'
                    game_over = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y
                
                # Verifica se o clique foi dentro do tabuleiro
                if mouseY < HEIGHT - 50:
                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)
                    
                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        if check_win(player):
                            draw_status_message(f"Jogador {player} venceu! Pressione R para reiniciar")
                            game_over = True
                        elif is_board_full():
                            draw_status_message("Empate! Pressione R para reiniciar")
                            game_over = True
                        else:
                            player = 'O' if player == 'X' else 'X'
                            draw_status_message(f"Vez do Jogador {player}")
                        
                        draw_figures()
        
        pygame.display.update()

if __name__ == "__main__":
    main()