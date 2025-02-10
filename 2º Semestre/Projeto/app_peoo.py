import pygame
import random
from abc import ABC, abstractmethod

# Inicializa o Pygame
pygame.init()

# Constantes globais
largura_tela = 800
altura_tela = 700
largura_jogo = 300
altura_jogo = 600
tamanho_bloco = 30

topo_esquerdo_x = (largura_tela - largura_jogo) // 2
topo_esquerdo_y = altura_tela - altura_jogo

class PecaBase(ABC):
    @abstractmethod
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotacao = 0
        self.cor = (0, 0, 0)

    @property
    @abstractmethod
    def formatos(self):
        pass

    @staticmethod
    def criar_peca_aleatoria():
        return random.choice([S, Z, I, O, J, L, T])(5, 0)

    def get_posicoes(self):
        posicoes = []
        formato = self.formatos[self.rotacao % len(self.formatos)]

        for i, linha in enumerate(formato):
            linha = list(linha)
            for j, coluna in enumerate(linha):
                if coluna == '0':
                    posicoes.append((self.x + j, self.y + i))

        for i, pos in enumerate(posicoes):
            posicoes[i] = (pos[0] - 2, pos[1] - 4)

        return posicoes

    def rotacionar(self):
        self.rotacao = (self.rotacao + 1) % len(self.formatos)

class S(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (0, 255, 0)

    @property
    def formatos(self):
        return [
            ['.....',
             '.....',
             '..00.',
             '.00..',
             '.....'],
            ['.....',
             '..0..',
             '..00.',
             '...0.',
             '.....']
        ]

class Z(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (255, 0, 0)

    @property
    def formatos(self):
        return [
            ['.....',
             '.....',
             '.00..',
             '..00.',
             '.....'],
            ['.....',
             '..0..',
             '.00..',
             '.0...',
             '.....']
        ]

class I(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (0, 255, 255)

    @property
    def formatos(self):
        return [
            ['..0..',
             '..0..',
             '..0..',
             '..0..',
             '.....'],
            ['.....',
             '0000.',
             '.....',
             '.....',
             '.....']
        ]

class O(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (255, 255, 0)

    @property
    def formatos(self):
        return [
            ['.....',
             '.....',
             '.00..',
             '.00..',
             '.....']
        ]

class J(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (255, 165, 0)

    @property
    def formatos(self):
        return [
            ['.....',
             '.0...',
             '.000.',
             '.....',
             '.....'],
            ['.....',
             '..00.',
             '..0..',
             '..0..',
             '.....'],
            ['.....',
             '.....',
             '.000.',
             '...0.',
             '.....'],
            ['.....',
             '..0..',
             '..0..',
             '.00..',
             '.....']
        ]

class L(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (0, 0, 255)

    @property
    def formatos(self):
        return [
            ['.....',
             '...0.',
             '.000.',
             '.....',
             '.....'],
            ['.....',
             '..0..',
             '..0..',
             '..00.',
             '.....'],
            ['.....',
             '.....',
             '.000.',
             '.0...',
             '.....'],
            ['.....',
             '.00..',
             '..0..',
             '..0..',
             '.....']
        ]

class T(PecaBase):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cor = (128, 0, 128)

    @property
    def formatos(self):
        return [
            ['.....',
             '..0..',
             '.000.',
             '.....',
             '.....'],
            ['.....',
             '..0..',
             '..00.',
             '..0..',
             '.....'],
            ['.....',
             '.....',
             '.000.',
             '..0..',
             '.....'],
            ['.....',
             '..0..',
             '.00..',
             '..0..',
             '.....']
        ]

def criar_grade(posicoes_travadas={}):
    grade = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for (x, y) in posicoes_travadas:
        grade[y][x] = posicoes_travadas[(x, y)]
    return grade

def espaco_valido(peca, grade):
    posicoes_aceitas = [[(j, i) for j in range(10) if grade[i][j] == (0, 0, 0)] for i in range(20)]
    posicoes_aceitas = [j for sub in posicoes_aceitas for j in sub]
    posicoes_peca = peca.get_posicoes()

    for pos in posicoes_peca:
        if pos not in posicoes_aceitas:
            if pos[1] > -1:
                return False
    return True

def verificar_perda(posicoes):
    for pos in posicoes:
        x, y = pos
        if y < 1:
            return True
    return False

def desenhar_texto_centralizado(texto, tamanho, cor, superficie):
    fonte = pygame.font.SysFont('comicsans', tamanho, bold=True)
    label = fonte.render(texto, 1, cor)
    superficie.blit(label, (topo_esquerdo_x + largura_jogo / 2 - (label.get_width() / 2),
                        topo_esquerdo_y + altura_jogo / 2 - label.get_height() / 2))

def desenhar_grade(superficie, linhas, colunas):
    sx = topo_esquerdo_x
    sy = topo_esquerdo_y
    for i in range(linhas):
        pygame.draw.line(superficie, (128, 128, 128), (sx, sy + i * tamanho_bloco),
                         (sx + largura_jogo, sy + i * tamanho_bloco))
        for j in range(colunas):
            pygame.draw.line(superficie, (128, 128, 128), (sx + j * tamanho_bloco, sy),
                             (sx + j * tamanho_bloco, sy + altura_jogo))

def limpar_linhas(grade, posicoes_travadas):
    global pontuacao
    incremento = 0
    for i in range(len(grade) - 1, -1, -1):
        linha = grade[i]
        if (0, 0, 0) not in linha:
            incremento += 1
            indice = i
            for j in range(len(linha)):
                try:
                    del posicoes_travadas[(j, i)]
                except:
                    continue
    if incremento > 0:
        pontuacao += incremento * 100
        for chave in sorted(list(posicoes_travadas), key=lambda x: x[1])[::-1]:
            x, y = chave
            if y < indice:
                nova_chave = (x, y + incremento)
                posicoes_travadas[nova_chave] = posicoes_travadas.pop(chave)

def desenhar_proxima_peca(peca, superficie):
    fonte = pygame.font.SysFont('comicsans', 30)
    label = fonte.render('Próxima Peça', 1, (255, 255, 255))

    sx = topo_esquerdo_x + largura_jogo + 50
    sy = topo_esquerdo_y + altura_jogo / 2 - 100
    formato = peca.formatos[peca.rotacao % len(peca.formatos)]

    for i, linha in enumerate(formato):
        linha = list(linha)
        for j, coluna in enumerate(linha):
            if coluna == '0':
                pygame.draw.rect(superficie, peca.cor, (sx + j * tamanho_bloco, sy + i * tamanho_bloco, tamanho_bloco, tamanho_bloco), 0)

    superficie.blit(label, (sx + 10, sy - 30))

def desenhar_janela(superficie):
    superficie.fill((0, 0, 0))
    fonte = pygame.font.SysFont('comicsans', 60)
    label = fonte.render('TETRIS', 1, (255, 255, 255))
    superficie.blit(label, (topo_esquerdo_x + largura_jogo / 2 - (label.get_width() / 2), 30))

    fonte = pygame.font.SysFont('comicsans', 30)
    label = fonte.render(f'Pontuação: {pontuacao}', 1, (255, 255, 255))
    sx = topo_esquerdo_x + largura_jogo + 50
    sy = topo_esquerdo_y + altura_jogo / 2 - 100
    superficie.blit(label, (sx, sy + 200))

    for i in range(len(grade)):
        for j in range(len(grade[i])):
            pygame.draw.rect(superficie, grade[i][j], (topo_esquerdo_x + j * tamanho_bloco, topo_esquerdo_y + i * tamanho_bloco, tamanho_bloco, tamanho_bloco), 0)

    desenhar_grade(superficie, 20, 10)
    pygame.draw.rect(superficie, (255, 0, 0), (topo_esquerdo_x, topo_esquerdo_y, largura_jogo, altura_jogo), 5)

def main():
    global grade, pontuacao
    posicoes_travadas = {}
    grade = criar_grade(posicoes_travadas)
    mudar_peca = False
    rodando = True
    peca_atual = PecaBase.criar_peca_aleatoria()
    proxima_peca = PecaBase.criar_peca_aleatoria()
    relogio = pygame.time.Clock()
    tempo_queda = 0
    pontuacao = 0

    while rodando:
        velocidade_queda = 0.27
        grade = criar_grade(posicoes_travadas)
        tempo_queda += relogio.get_rawtime()
        relogio.tick()

        if tempo_queda / 1000 >= velocidade_queda:
            tempo_queda = 0
            peca_atual.y += 1
            if not espaco_valido(peca_atual, grade) and peca_atual.y > 0:
                peca_atual.y -= 1
                mudar_peca = True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.display.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    peca_atual.x -= 1
                    if not espaco_valido(peca_atual, grade):
                        peca_atual.x += 1

                elif evento.key == pygame.K_RIGHT:
                    peca_atual.x += 1
                    if not espaco_valido(peca_atual, grade):
                        peca_atual.x -= 1

                elif evento.key == pygame.K_UP:
                    peca_atual.rotacionar()
                    if not espaco_valido(peca_atual, grade):
                        peca_atual.rotacao = (peca_atual.rotacao - 1) % len(peca_atual.formatos)

                elif evento.key == pygame.K_DOWN:
                    peca_atual.y += 1
                    if not espaco_valido(peca_atual, grade):
                        peca_atual.y -= 1

                elif evento.key == pygame.K_SPACE:
                    while espaco_valido(peca_atual, grade):
                        peca_atual.y += 1
                    peca_atual.y -= 1

        posicoes_formato = peca_atual.get_posicoes()

        for i in range(len(posicoes_formato)):
            x, y = posicoes_formato[i]
            if y > -1:
                grade[y][x] = peca_atual.cor

        if mudar_peca:
            for pos in posicoes_formato:
                p = (pos[0], pos[1])
                posicoes_travadas[p] = peca_atual.cor
            peca_atual = proxima_peca
            proxima_peca = PecaBase.criar_peca_aleatoria()
            mudar_peca = False
            limpar_linhas(grade, posicoes_travadas)

        desenhar_janela(janela)
        desenhar_proxima_peca(proxima_peca, janela)
        pygame.display.update()

        if verificar_perda(posicoes_travadas):
            desenhar_texto_centralizado("Você Perdeu", 40, (255, 255, 255), janela)
            pygame.display.update()
            pygame.time.delay(2000)
            rodando = False

    menu_principal()

def menu_principal():
    rodando = True
    while rodando:
        janela.fill((0, 0, 0))
        desenhar_texto_centralizado('Pressione qualquer tecla para começar.', 60, (255, 255, 255), janela)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                main()
    pygame.quit()

janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tetris')
menu_principal()