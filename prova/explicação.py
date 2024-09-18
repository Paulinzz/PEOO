# importando os modulos preciso para o código, como pygame e random 
import pygame
import random


# configurações como nome do jogo, resolução, tela, tempo de jogo aberto e inicialização. 
pygame.init() # inicar todos as funções, modulos do pygame. 
pygame.display.set_caption("Snake The Game") # nome do jogo apresentado na aba, aparti que iniciar o jogo 
largura, altura = 1200, 800 # variavel responsavel por determinar a largura e altura do game.
tela = pygame.display.set_mode((largura, altura)) # cria a tela de acordo com a largura e altura.
relogio = pygame.time.Clock() # cria um objeto para controlar o tempo do jogo (usado para definir a velocidade do jogo).


# cores
preta = (0, 0, 0) # defini a cor preta
branca = (255, 255, 255) # defini a cor branca 
vermelha = (255, 0, 0) # defini a cor vermelha
verde = (0, 255, 0) # defini a cor verde 

# parametros da cobrinha
tamanho_quadrado = 20 # defini o tamanho de cada corpinho da cobra
velocidade_jogo = 15 # velocidade que a cobrinha se mexer durante o mapa.

def gerar_comida(): # função para gerar a comida.
    # eixo x = horizontal
    # eixo y = vertical 
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado) # gera uma coordenada aleatória para a comida dentro dos limites da tela no eixo x.

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado) # gera uma coordenada aleatória para a comida dentro dos limites da tela no eixo y .
    # As coordenadas da comida são ajustadas para garantir que fiquem alinhadas na grade de movimento da cobra (dividindo pelo tamanho do quadrado).
    return comida_x, comida_y # A função retorna as coordenadas comida_x e comida_y.

def desenhar_comida(tamanho, comida_x, comida_y): # gerar uma comida de acordo com o tamanho da cobra aleatoriamente no eixo x,y. 
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels): # gerar a cobra no que é composta de vários quadrados.
    for pixel in pixels: # pixels é uma lista que armazena as coordenadas de cada parte do corpo da cobra.
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho]) # A função itera sobre cada pixel da cobra e desenha um quadrado branco no local correto (quase no meio da tela).

def desenhar_pontuacao(pontuacao): # função para desenhar a pontuação.
    fonte = pygame.font.SysFont("Helvetica", 35) # definir a fonte e tamanho dela.
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha) # armazenar o texto na variavel. 
    tela.blit(texto, [1, 1]) # desenhar o texto na cordenada [1,1] no canto superior esquerdo.

def selecionar_velocidade(tecla): # A função determina a direção da cobra com base na tecla pressionada (setinhas do teclado).
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
    return velocidade_x, velocidade_y  # Ela retorna a nova velocidade nas direções x e y de acordo com a tecla pressionada

def rodar_jogo(): # Esta é a função principal do jogo, onde ocorre a lógica do movimento da cobra, detecção de colisões e controle do jogo.
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1

    pixels = []

    comida_x, comida_y = gerar_comida()
    
    while not fim_jogo: # O laço principal (while not fim_jogo) é executado até que a cobra colida com a parede ou com seu próprio corpo, terminando o jogo.
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        
        # atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        x += velocidade_x
        y += velocidade_y

        # desenhar_cobra

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        # se a cobrinha bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # A comida é gerada e desenhada, a cobra é movida e redesenhada, e a pontuação é atualizada.

        desenhar_cobra(tamanho_quadrado, pixels)

        # desenhar_pontos

        desenhar_pontuacao(tamanho_cobra - 1)

        # atualizacao da tela


        pygame.display.update()
        # criar uma nova comida

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        relogio.tick(velocidade_jogo)


