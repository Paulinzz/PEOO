# configurações iniciais

import pygame

import random

pygame.init()

pygame.display.set_caption("Snake The Game")

largura, altura = 1200, 800

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

# cores

preta = (0, 0, 0)

branca = (255, 255, 255)

vermelha = (255, 0, 0)

verde = (0, 255, 0)

# parametros da cobrinha

tamanho_quadrado = 20

velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def verificar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return True  # Sinaliza que o jogo deve terminar
    return False


def rodar_jogo():
    # Inicializar parâmetros do jogo
    fim_jogo = False
    posicao_x, posicao_y = largura // 2, altura // 2  # Começa no centro da tela
    velocidade_x, velocidade_y = 0, 0  # Velocidade inicial (parada)
    corpo_cobra = [[posicao_x, posicao_y]]  # Lista de posições do corpo da cobra
    tamanho_cobra = 1

    comida_x, comida_y = gerar_comida()  # Gerar a primeira comida
    
    while not fim_jogo:
        fim_jogo = verificar_eventos()  # Verificar se o jogo deve ser encerrado
        
        # Atualizar movimento da cobra com base nas teclas
        velocidade_x, velocidade_y = atualizar_velocidade(velocidade_x, velocidade_y)
        posicao_x, posicao_y = mover_cobra(posicao_x, posicao_y, velocidade_x, velocidade_y)

        # Verificar colisões
        if verificar_colisao_parede(posicao_x, posicao_y) or verificar_colisao_corpo(corpo_cobra):
            fim_jogo = True

        # Desenhar os elementos do jogo
        tela.fill(preta)  # Limpar a tela
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        corpo_cobra = atualizar_cobra(corpo_cobra, posicao_x, posicao_y, tamanho_cobra)
        desenhar_cobra(tamanho_quadrado, corpo_cobra)
        desenhar_pontuacao(tamanho_cobra - 1)

        # Verificar se a cobra comeu a comida
        if posicao_x == comida_x and posicao_y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()  # Gerar nova comida

        # Atualizar a tela
        pygame.display.update()
        relogio.tick(velocidade_jogo)  # Controlar a velocidade do jogo

def atualizar_velocidade(velocidade_x, velocidade_y):
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_UP] and velocidade_y == 0:
        return 0, -tamanho_quadrado
    elif teclas[pygame.K_DOWN] and velocidade_y == 0:
        return 0, tamanho_quadrado
    elif teclas[pygame.K_LEFT] and velocidade_x == 0:
        return -tamanho_quadrado, 0
    elif teclas[pygame.K_RIGHT] and velocidade_x == 0:
        return tamanho_quadrado, 0
    
    return velocidade_x, velocidade_y

def mover_cobra(posicao_x, posicao_y, velocidade_x, velocidade_y):
    posicao_x += velocidade_x
    posicao_y += velocidade_y
    return posicao_x, posicao_y

def verificar_colisao_parede(x, y):
    return x < 0 or x >= largura or y < 0 or y >= altura

def verificar_colisao_corpo(corpo_cobra):
    for parte_corpo in corpo_cobra[:-1]:  # Verifica colisão com todas as partes, exceto a última
        if parte_corpo == corpo_cobra[-1]:  # Compara com a cabeça
            return True
    return False

def atualizar_cobra(corpo_cobra, x, y, tamanho_cobra):
    corpo_cobra.append([x, y])
    if len(corpo_cobra) > tamanho_cobra:
        del corpo_cobra[0]  # Remove a cauda
    return corpo_cobra

rodar_jogo()
