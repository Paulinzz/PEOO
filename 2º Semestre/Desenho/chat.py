import turtle
import time
import math

class Forma():
    def __init__(self, nome, cor, x, y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
        
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.fillcolor(self.cor)
        self.desenhar_forma(t)
        t.end_fill()

    def desenhar_forma(self, t: turtle.Turtle):
        raise Exception("Metodo Alternativo")

class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retangulo', cor, x, y)
        self.largura = largura
        self.altura = altura

    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)

class Triangulo(Forma):
    def __init__(self, lado, cor, x, y):
        super().__init__('Triangulo', cor, x, y)
        self.lado = lado

    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(3):
            t.forward(self.lado)
            t.right(120)

class Circulo(Forma):
    def __init__(self, raio, cor, x, y):
        super().__init__('Circulo', cor, x, y)
        self.raio = raio

    def desenhar_forma(self, t: turtle.Turtle):
        t.circle(self.raio)

class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y):
        super().__init__('Estrela', cor, x, y)
        self.tamanho = tamanho

    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(5):
            t.forward(self.tamanho)
            t.right(144)  # Ângulo para desenhar uma estrela de 5 pontas


#fundo 
t = turtle.Turtle()
turtle.bgcolor("darkblue")

# Criando as formas
tronco = Retangulo(50, 150, 'brown', -25, -150)  # Tronco da árvore
folha1 = Circulo(50, 'green', 0, 0)  # Folha da árvore
sol = Circulo(50, 'yellow', 200, 100)  # Sol
estrela1 = Estrela(30, 'black', -150, 150)  # Estrela
estrela2 = Estrela(20, 'black', 100, 200)  # Outra estrela

# Lista de formas para desenhar
formas = [tronco, folha1, sol, estrela1, estrela2]

# Desenhando as formas
for f in formas:
    f.desenhar()

# Mantém a janela aberta por 3 segundos antes de fechar
time.sleep(3)
turtle.done()
