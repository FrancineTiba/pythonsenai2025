import pygame
import random
import time

# Inicializa o pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I - ciano
    (0, 0, 255),    # J - azul
    (255, 165, 0),  # L - laranja
    (255, 255, 0),  # O - amarelo
    (0, 255, 0),    # S - verde
    (128, 0, 128),  # T - roxo
    (255, 0, 0)     # Z - vermelho
]

# Configurações do jogo
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
GAME_AREA_LEFT = BLOCK_SIZE

# Formas das peças (tetrominós)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    
    [[1, 0, 0],
     [1, 1, 1]],     # J
     
    [[0, 0, 1],
     [1, 1, 1]],     # L
     
    [[1, 1],
     [1, 1]],        # O
     
    [[0, 1, 1],
     [1, 1, 0]],     # S
     
    [[0, 1, 0],
     [1, 1, 1]],     # T
     
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

# Configuração da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.fall_speed = 0.5  # segundos
        self.fall_time = 0
        self.clearing_lines = False
        self.lines_to_clear = []
        self.clear_animation_time = 0
        self.clear_animation_duration = 0.3  # segundos
        
    def new_piece(self):
        # Escolhe uma forma aleatória
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        
        # Posição inicial (centro no topo)
        x = GRID_WIDTH // 2 - len(shape[0]) // 2
        y = 0
        
        return {"shape": shape, "color": color, "x": x, "y": y}
    
    def valid_move(self, piece, x_offset=0, y_offset=0):
        for y, row in enumerate(piece["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece["x"] + x + x_offset
                    new_y = piece["y"] + y + y_offset
                    
                    if (new_x < 0 or new_x >= GRID_WIDTH or 
                        new_y >= GRID_HEIGHT or 
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True
    
    def rotate_piece(self):
        # Transpõe a matriz da peça e inverte as linhas para girar 90°
        rotated = [list(row) for row in zip(*self.current_piece["shape"][::-1])]
        
        old_shape = self.current_piece["shape"]
        self.current_piece["shape"] = rotated
        
        # Se a rotação não for válida, volta para a forma original
        if not self.valid_move(self.current_piece):
            self.current_piece["shape"] = old_shape
    
    def lock_piece(self):
        for y, row in enumerate(self.current_piece["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    # Garante que a peça não está acima do grid
                    if self.current_piece["y"] + y >= 0:
                        self.grid[self.current_piece["y"] + y][self.current_piece["x"] + x] = self.current_piece["color"]
        
        # Verifica linhas completas
        self.check_lines()
        
        # Se não estiver limpando linhas, cria uma nova peça
        if not self.clearing_lines:
            self.current_piece = self.new_piece()
            
            # Verifica se o jogo acabou
            if not self.valid_move(self.current_piece):
                self.game_over = True
    
    def check_lines(self):
        self.lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                self.lines_to_clear.append(y)
        
        if self.lines_to_clear:
            self.clearing_lines = True
            self.clear_animation_time = 0
    
    def clear_lines(self):
        lines_cleared = len(self.lines_to_clear)
        
        # Remove as linhas completas
        for y in sorted(self.lines_to_clear):
            # Move todas as linhas acima para baixo
            for y2 in range(y, 0, -1):
                self.grid[y2] = self.grid[y2-1][:]
            self.grid[0] = [0 for _ in range(GRID_WIDTH)]
        
        # Atualiza a pontuação
        if lines_cleared == 1:
            self.score += 100 * self.level
        elif lines_cleared == 2:
            self.score += 300 * self.level
        elif lines_cleared == 3:
            self.score += 500 * self.level
        elif lines_cleared == 4:
            self.score += 800 * self.level
        
        # Aumenta o nível a cada 10 linhas
        self.level = 1 + self.score // 2000
        
        # Aumenta a velocidade conforme o nível
        self.fall_speed = max(0.05, 0.5 - (self.level - 1) * 0.05)
        
        # Reseta o estado de limpeza
        self.clearing_lines = False
        self.lines_to_clear = []
        
        # Cria uma nova peça
        self.current_piece = self.new_piece()
        
        # Verifica se o jogo acabou
        if not self.valid_move(self.current_piece):
            self.game_over = True
    
    def update(self, delta_time):
        if self.game_over:
            return
            
        if self.clearing_lines:
            self.clear_animation_time += delta_time
            
            if self.clear_animation_time >= self.clear_animation_duration:
                self.clear_lines()
            return
            
        self.fall_time += delta_time
        
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if self.valid_move(self.current_piece, 0, 1):
                self.current_piece["y"] += 1
            else:
                self.lock_piece()
    
    def draw(self):
        # Desenha o fundo
        screen.fill(BLACK)
        
        # Desenha a área do jogo
        pygame.draw.rect(screen, WHITE, (GAME_AREA_LEFT - 1, 0, 
                                       BLOCK_SIZE * GRID_WIDTH + 2, 
                                       BLOCK_SIZE * GRID_HEIGHT + 2), 1)
        
        # Desenha a grade
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(screen, GRAY, (GAME_AREA_LEFT + x * BLOCK_SIZE, 
                                              y * BLOCK_SIZE, 
                                              BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Desenha as peças fixadas
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    # Se a linha está sendo limpada, faz uma animação
                    if y in self.lines_to_clear:
                        progress = self.clear_animation_time / self.clear_animation_duration
                        # Pisca entre branco e a cor original
                        if int(progress * 10) % 2 == 0:
                            color = WHITE
                        else:
                            color = self.grid[y][x]
                        # Efeito de encolhimento
                        size = BLOCK_SIZE * (1 - progress)
                        offset = (BLOCK_SIZE - size) / 2
                        pygame.draw.rect(screen, color, 
                                       (GAME_AREA_LEFT + x * BLOCK_SIZE + offset, 
                                        y * BLOCK_SIZE + offset, 
                                        size, size))
                    else:
                        pygame.draw.rect(screen, self.grid[y][x], 
                                       (GAME_AREA_LEFT + x * BLOCK_SIZE, 
                                        y * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, WHITE, 
                                       (GAME_AREA_LEFT + x * BLOCK_SIZE, 
                                        y * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Desenha a peça atual (se não estiver limpando linhas)
        if not self.clearing_lines:
            for y, row in enumerate(self.current_piece["shape"]):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, self.current_piece["color"], 
                                       (GAME_AREA_LEFT + (self.current_piece["x"] + x) * BLOCK_SIZE, 
                                        (self.current_piece["y"] + y) * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, WHITE, 
                                       (GAME_AREA_LEFT + (self.current_piece["x"] + x) * BLOCK_SIZE, 
                                        (self.current_piece["y"] + y) * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Desenha informações do jogo
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        
        screen.blit(score_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 30))
        screen.blit(level_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 60))
        
        if self.game_over:
            game_over_font = pygame.font.SysFont(None, 50)
            game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
            restart_text = font.render("Press ESC to quit", True, WHITE)
            screen.blit(game_over_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE // 2 - 100, 
                                       GRID_HEIGHT * BLOCK_SIZE // 2 - 25))
            screen.blit(restart_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE // 2 - 80, 
                                     GRID_HEIGHT * BLOCK_SIZE // 2 + 25))

# Cria o jogo
game = Tetris()

# Loop principal
running = True
last_time = pygame.time.get_ticks()

while running:
    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000.0  # Converte para segundos
    last_time = current_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            if not game.game_over and not game.clearing_lines:
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0):
                        game.current_piece["x"] -= 1
                elif event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0):
                        game.current_piece["x"] += 1
                elif event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1):
                        game.current_piece["y"] += 1
                elif event.key == pygame.K_UP:
                    game.rotate_piece()
                elif event.key == pygame.K_SPACE:
                    # Hard drop
                    while game.valid_move(game.current_piece, 0, 1):
                        game.current_piece["y"] += 1
                    game.lock_piece()
    
    game.update(delta_time)
    game.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()