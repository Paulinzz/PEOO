# Q2 (5pts) – Se o usuário apertar as teclas ENTER, espaço ou borracha (backspace), seu jogo lança um erro. 
# Conserte esse problema para essas teclas e quaisquer outras que possam vir a dar defeito.
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

# parâmetros da cobrinha

tamanho_quadrado = 20

velocidade_jogo = 15

def gerar_comida(): # corrigi faznedo as seguintes alterações:
    # troquei as variaveis largura e altura, por números proximos a resolução do jogo (altura e largura) menos 100.
    # outra forma de resolver esse problema é apenas fazendo inves de número, uma subtração com o valor da variavel.
    # Ex: comida_x = round(random.randrange(0, (largura - 100) - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_x = round(random.randrange(0, 1100 - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, 700 - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
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
        return 0, tamanho_quadrado
    elif tecla == pygame.K_UP:
        return 0, -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        return tamanho_quadrado, 0
    elif tecla == pygame.K_LEFT:
        return -tamanho_quadrado, 0
    return None  # retorna None se a tecla não for uma seta

# verifica se a tecla pressionada não é uma das setas
def tecla_errada(tecla):
    if tecla not in [pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT]:
        return True
    return False #se a tecla digitada não umas das teclas para se mover a cobrinha, ela ignorar por completo

def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1

    pixels = []
    comida_x, comida_y = gerar_comida()
    
    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                # chamo a função para verificar a tecla e n dár esse "glitch no game."
                if tecla_errada(evento.key):
                    continue
                nova_velocidade = selecionar_velocidade(evento.key)
                if nova_velocidade:
                    velocidade_x, velocidade_y = nova_velocidade

        # atualizar a posição da cobra
        x += velocidade_x
        y += velocidade_y

        # checa se a cobra saiu dos limites da tela
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # adiciona a nova posição da cabeça da cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        # verifica se a cobra bateu no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # desenha elementos na tela
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)

        # atualiza a tela
        pygame.display.update()

        # verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()
pygame.quit()