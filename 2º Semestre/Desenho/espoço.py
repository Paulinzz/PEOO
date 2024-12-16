# importação dos módulos
import turtle
import time
import random

# configuração da janela
class Forma():
    # criando o construdor
    def __init__(self, nome, cor, x, y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
    
    # criando o metodo desenhar 
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.fillcolor(self.cor)
        self.desenhar_forma(t)
        t.end_fill()
    # modo abstrado de desenhar forma
    def desenhar_forma(self, t: turtle.Turtle):
        raise Exception('Metodo Alternativo')

# criando a classe retangulo como figura geometrica
class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y): # criando construdor
        super().__init__('Retangulo', cor, x, y) # trazendo do construdor original dados, para otmizar o codigo
        self.largura = largura # defini largura
        self.altura = altura # defini altura

# metodo para desenhar retangulo
    def desenhar_forma(self, t: turtle.Turtle): 
        t.begin_fill()
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)
        t.end_fill()

# criando a classe circulo como figura geometrica
class Circulo(Forma):
    def __init__(self, raio, cor, x, y): # criando construdor
        super().__init__('Circulo', cor, x, y) # trazendo do construdor original dados, para otmizar o codigo
        self.raio = raio

# metodo para desenhar circulo
    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        t.circle(self.raio)
        t.end_fill()

# criando a classe retangulo como figura geometrica
class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y): # criando construdor
        super().__init__('Estrela', cor, x, y)
        self.tamanho = tamanho

# metodo para desenhar estrela
    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(5):
            t.forward(self.tamanho)
            t.right(144)  


t = turtle.Turtle() # variavel global definida
turtle.bgcolor('darkblue') # defino o fundo para auzl escuro

# criação dos objetos
grama = Retangulo(800, 400, 'green', -400, -300)  
tronco = Retangulo(50, 150, 'brown', -25, -150) 
folhas = Circulo(50, 'green', 0, -160)  
lua = Circulo(50, 'lightyellow', 200, 100) 

# criação da lista para amazenar os objetos
formas = [grama, tronco, folhas, lua]

# desenho das estrelas, criando o total de 30 estrelas, sendo definida no eixo x e y, tendo um tamanho de 5 a 15 px, 
# na cor branca, sendo espalhado em todo o céu. 
for _ in range(31):  
    x = random.randint( -300, 300)  
    y = random.randint( 100, 300)  
    tamanho = random.randint(5, 15)  
    estrela = Estrela(tamanho, 'black', x, y)
    formas.append(estrela)

# laço de repetição para desenhar as formas que estão na "[]", com o espaço de um 1s entre o desenho e preenchimento das forrmas.
for f in formas:
    f.desenhar()
    time.sleep(1)
time.sleep(3)
turtle.done()


# utilização de três formas geometricas, sendo o ciruclo, o retângulo e a estrela. 
# A ideia foi cria uma simples paisegem com uma lua, uma árvore e estrekas no céu.
# espero que tenha gostado professor, simples mas espero que tenha sido agradavel!! boa sorte na sua jornada Ciro <3!