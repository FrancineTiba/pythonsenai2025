import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca - Dicas nos Erros")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Fontes
font = pygame.font.SysFont('Arial', 32)
small_font = pygame.font.SysFont('Arial', 24)
dica_font = pygame.font.SysFont('Arial', 20)
categoria_font = pygame.font.SysFont('Arial', 28, bold=True)

# Banco de palavras por categoria com dicas progressivas
categorias = {
    "FRUTAS": [
        {
            "palavra": "BANANA", 
            "dicas": [
                "É uma fruta tropical",
                "Tem casca amarela quando madura",
                "Rica em potássio",
                "Forma de meia-lua",
                "Nome científico: Musa spp",
                "Muito usada em vitaminas"
            ]
        },
        {
            "palavra": "MORANGO", 
            "dicas": [
                "Fruta vermelha com sementes externas",
                "Tem formato de coração",
                "Muito usada em sobremesas",
                "Planta rasteira da família Rosaceae",
                "Tem um aroma característico",
                "É na verdade um pseudofruto"
            ]
        }
    ],
    "ANIMAIS": [
        {
            "palavra": "ELEFANTE", 
            "dicas": [
                "Maior mamífero terrestre",
                "Tem uma tromba característica",
                "Vive em manadas",
                "Tem presas de marfim",
                "Pode viver mais de 60 anos",
                "Espécie ameaçada de extinção"
            ]
        },
        {
            "palavra": "TUCANO", 
            "dicas": [
                "Ave tropical com bico grande",
                "Bico colorido e leve",
                "Vive nas florestas da América",
                "Alimenta-se de frutas",
                "Bico ajuda a regular temperatura",
                "Aparece em comerciais de cereal"
            ]
        }
    ],
    "PAÍSES": [
        {
            "palavra": "BRASIL", 
            "dicas": [
                "Maior país da América do Sul",
                "Fala português",
                "Conhecido pelo carnaval",
                "Tem a maior floresta tropical",
                "Capital é Brasília",
                "País do futebol"
            ]
        },
        {
            "palavra": "JAPAO", 
            "dicas": [
                "País insular no Pacífico",
                "Terra do sol nascente",
                "Conhecido por sushi e anime",
                "Capital é Tóquio",
                "Tem o Monte Fuji",
                "Tecnologia avançada"
            ]
        }
    ]
}

def selecionar_palavra():
    categoria = random.choice(list(categorias.keys()))
    palavra_data = random.choice(categorias[categoria])
    return categoria, palavra_data

def desenhar_forca(erros):
    pygame.draw.line(screen, BLACK, (100, 500), (300, 500), 5)
    pygame.draw.line(screen, BLACK, (200, 500), (200, 100), 5)
    pygame.draw.line(screen, BLACK, (200, 100), (350, 100), 5)
    pygame.draw.line(screen, BLACK, (350, 100), (350, 150), 5)
    
    if erros >= 1: pygame.draw.circle(screen, BLACK, (350, 180), 30, 2)
    if erros >= 2: pygame.draw.line(screen, BLACK, (350, 210), (350, 330), 2)
    if erros >= 3: pygame.draw.line(screen, BLACK, (350, 240), (310, 280), 2)
    if erros >= 4: pygame.draw.line(screen, BLACK, (350, 240), (390, 280), 2)
    if erros >= 5: pygame.draw.line(screen, BLACK, (350, 330), (310, 380), 2)
    if erros >= 6: pygame.draw.line(screen, BLACK, (350, 330), (390, 380), 2)

def desenhar_palavra(palavra, letras_adivinhadas):
    display_palavra = " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
    texto = font.render(display_palavra, True, BLACK)
    screen.blit(texto, (400, 200))

def desenhar_letras_erradas(letras_erradas):
    if letras_erradas:
        texto = small_font.render("Letras erradas: " + ", ".join(letras_erradas), True, RED)
        screen.blit(texto, (400, 250))

def mostrar_categoria(categoria):
    texto = categoria_font.render(f"Categoria: {categoria}", True, ORANGE)
    screen.blit(texto, (400, 100))

def mostrar_dicas(dicas, erros):
    y_pos = 300
    for i in range(min(erros, len(dicas))):
        texto = dica_font.render(f"Dica {i+1}: {dicas[i]}", True, PURPLE)
        screen.blit(texto, (400, y_pos))
        y_pos += 25

def mostrar_mensagem(mensagem, cor):
    texto = font.render(mensagem, True, cor)
    screen.blit(texto, (WIDTH//2 - texto.get_width()//2, HEIGHT//2 + 100))

def tela_fim_jogo(mensagem, cor, palavra, categoria):
    screen.fill(WHITE)
    texto = font.render(mensagem, True, cor)
    screen.blit(texto, (WIDTH//2 - texto.get_width()//2, HEIGHT//2 - 50))
    
    texto_categoria = small_font.render(f"Categoria: {categoria}", True, ORANGE)
    screen.blit(texto_categoria, (WIDTH//2 - texto_categoria.get_width()//2, HEIGHT//2 - 20))
    
    texto_palavra = font.render(f"A palavra era: {palavra}", True, BLACK)
    screen.blit(texto_palavra, (WIDTH//2 - texto_palavra.get_width()//2, HEIGHT//2 + 20))
    
    texto_reiniciar = small_font.render("Pressione N para nova palavra ou S para sair", True, BLUE)
    screen.blit(texto_reiniciar, (WIDTH//2 - texto_reiniciar.get_width()//2, HEIGHT//2 + 80))
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    return True
                elif event.key == pygame.K_s:
                    pygame.quit()
                    sys.exit()

def main():
    jogando = True
    
    while jogando:
        categoria, dados_palavra = selecionar_palavra()
        palavra = dados_palavra["palavra"].upper()
        dicas = dados_palavra["dicas"]
        
        letras_adivinhadas = set()
        letras_erradas = set()
        erros = 0
        max_erros = 6
        
        rodando = True
        
        while rodando:
            screen.fill(WHITE)
            
            desenhar_forca(erros)
            mostrar_categoria(categoria)
            desenhar_palavra(palavra, letras_adivinhadas)
            desenhar_letras_erradas(letras_erradas)
            mostrar_dicas(dicas, erros)
            
            if erros >= max_erros:
                mostrar_mensagem("Você errou!", RED)
                pygame.display.update()
                pygame.time.delay(1000)
                rodando = False
                jogando = tela_fim_jogo("Você errou!", RED, palavra, categoria)
                break
            
            if all(letra in letras_adivinhadas for letra in palavra):
                mostrar_mensagem("Você acertou!", GREEN)
                pygame.display.update()
                pygame.time.delay(1000)
                rodando = False
                jogando = tela_fim_jogo("Você acertou!", GREEN, palavra, categoria)
                break
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key >= pygame.K_a and event.key <= pygame.K_z:
                        letra = chr(event.key).upper()
                        
                        if letra not in letras_adivinhadas and letra not in letras_erradas:
                            if letra in palavra:
                                letras_adivinhadas.add(letra)
                            else:
                                letras_erradas.add(letra)
                                erros += 1  # Incrementa erros (que agora controlam as dicas)

if __name__ == "__main__":
    main()