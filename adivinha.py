import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

# Fontes
font_large = pygame.font.SysFont('Arial', 48)
font_medium = pygame.font.SysFont('Arial', 36)
font_small = pygame.font.SysFont('Arial', 24)

# Banco de palavras e dicas
palavras_dicas = {
    "python": ["Linguagem de programação", "Nome de uma cobra", "Usada em inteligência artificial"],
    "jogo": ["Forma de entretenimento", "Pode ser eletrônico ou de tabuleiro", "Tem regras"],
    "computador": ["Máquina eletrônica", "Processa informações", "Tem CPU e memória"],
    "programacao": ["Criação de software", "Envolve algoritmos", "Escrever código"],
    "openai": ["Empresa de IA", "Criadora do ChatGPT", "Fundada por Elon Musk e outros"],
    "futebol": ["Esporte com bola", "Jogado em times de 11", "Copa do Mundo"],
    "musica": ["Arte dos sons", "Tem ritmo e melodia", "Pode ser instrumental ou vocal"],
    "livro": ["Fonte de conhecimento", "Tem páginas", "Pode ser físico ou digital"]
}

# Variáveis do jogo
palavra_atual = ""
dicas = []
tentativas = 0
max_tentativas = 3
acertou = False
jogando = True
input_text = ""
input_active = False
mensagem = ""
pontuacao = 0.0  # Pontuação como float para armazenar decimais

def escolher_palavra():
    global palavra_atual, dicas, tentativas, acertou, mensagem
    palavra_atual = random.choice(list(palavras_dicas.keys()))
    dicas = palavras_dicas[palavra_atual]
    tentativas = 0
    acertou = False
    mensagem = ""

def desenhar_botao(texto, x, y, width, height, cor_normal, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, cor_hover, (x, y, width, height))
        if clique[0] == 1 and acao is not None:
            acao()
    else:
        pygame.draw.rect(screen, cor_normal, (x, y, width, height))
    
    texto_surf = font_small.render(texto, True, BLACK)
    texto_rect = texto_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(texto_surf, texto_rect)

def desenhar_input():
    pygame.draw.rect(screen, WHITE, (WIDTH//2 - 150, HEIGHT//2 + 50, 300, 40))
    texto_surf = font_small.render(input_text, True, BLACK)
    screen.blit(texto_surf, (WIDTH//2 - 140, HEIGHT//2 + 55))
    
    # Mostrar "Digite aqui..." quando estiver vazio
    if not input_text and not input_active:
        dica_surf = font_small.render("Digite seu palpite aqui...", True, GRAY)
        screen.blit(dica_surf, (WIDTH//2 - 140, HEIGHT//2 + 55))

def verificar_palpite():
    global input_text, tentativas, acertou, mensagem, pontuacao
    if input_text.lower() == palavra_atual:
        acertou = True
        pontuacao += 1.0  # +1 ponto por acerto
        mensagem = "Parabéns! Você acertou!"
    else:
        tentativas += 1
        pontuacao -= 0.33  # -0.33 por erro (arredondado para 2 casas decimais)
        pontuacao = round(pontuacao, 2)  # Arredonda para evitar números como 0.3300000004
        
        if tentativas >= max_tentativas:
            mensagem = f"Game over! A palavra era: {palavra_atual}"
        else:
            mensagem = f"Errado! Tentativa {tentativas} de {max_tentativas}"
    input_text = ""

def reiniciar_jogo():
    global input_text, mensagem
    escolher_palavra()
    input_text = ""
    mensagem = ""

def sair_do_jogo():
    global jogando
    jogando = False

# Escolhe a primeira palavra
escolher_palavra()

# Loop principal do jogo
while jogando:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se clicou na área de input
            if WIDTH//2 - 150 < event.pos[0] < WIDTH//2 + 150 and HEIGHT//2 + 50 < event.pos[1] < HEIGHT//2 + 90:
                input_active = True
            else:
                input_active = False
        
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    if input_text and not acertou and tentativas < max_tentativas:
                        verificar_palpite()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
    
    # Título
    titulo = font_large.render("Adivinhe a Palavra", True, BLUE)
    screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 50))
    
    # Mostra pontuação
    score_text = f"Pontuação: {pontuacao}"
    score_surf = font_medium.render(score_text, True, YELLOW)
    screen.blit(score_surf, (WIDTH - score_surf.get_width() - 20, 20))
    
    # Mostra dica atual
    if tentativas < len(dicas):
        dica_texto = f"Dica {tentativas + 1}: {dicas[tentativas]}"
    else:
        dica_texto = "Sem mais dicas disponíveis"
    
    dica_surf = font_medium.render(dica_texto, True, BLACK)
    screen.blit(dica_surf, (WIDTH//2 - dica_surf.get_width()//2, 150))
    
    # Mostra tentativas restantes
    tentativas_texto = f"Tentativas: {tentativas}/{max_tentativas}"
    tentativas_surf = font_small.render(tentativas_texto, True, BLACK)
    screen.blit(tentativas_surf, (WIDTH//2 - tentativas_surf.get_width()//2, 200))
    
    # Área de input
    desenhar_input()
    
    # Mensagem de feedback
    if mensagem:
        mensagem_surf = font_medium.render(mensagem, True, GREEN if acertou else RED)
        screen.blit(mensagem_surf, (WIDTH//2 - mensagem_surf.get_width()//2, HEIGHT//2 + 120))
    
    # Botões quando o jogo termina
    if acertou or tentativas >= max_tentativas:
        desenhar_botao("Nova Palavra", WIDTH//2 - 220, HEIGHT - 100, 200, 50, GREEN, (100, 255, 100), reiniciar_jogo)
        desenhar_botao("Sair", WIDTH//2 + 20, HEIGHT - 100, 200, 50, RED, (255, 100, 100), sair_do_jogo)
    
    pygame.display.flip()

pygame.quit()
sys.exit()