# Faça um desenho com formas geométricas utilizando a biblioteca turtle.
# Reveja a
# aula sobre herança para ter uma noção de como desenhar formas
#geométricas com turtle.
#Mas atenção: as classes no arquivo formas.py
#possuem linhas repetidas no método desenhar.
#Seu trabalho aqui é justamente usar seus conhecimentos de orientação a objetos para evitar repetição de código.

#Requisitos do desenho:
#Represente cada forma geométrica como uma classe.
#Ex.: Retangulo, Trialgulo, etc.
#Crie objetos da mesma classe para representar formas semelhantes. Use mais de um objeto de pelo menos uma classe.
#Ex.: Se há dois retângulos no desenho, não crie uma classe para cada, reutilize a mesma classe criando objetos diferentes.
#Desenhe pelo menos 3 tipos de formas geométricas diferentes (com suas respectivas classes).
#Ex.: Três retângulos, um círculo, um triângulo.
#Use seus conhecimentos de herança e/ou composição de classes para evitar repetir código.
#Faça um desenho que tenha algum sentido: uma casa, uma bandeira de um país, etc.
#Critérios de avaliação:
#+30 pontos pela ausência de linhas repetidas, sendo aplicada uma penalização de -5pts por cada linha repetida.
#+5 pontos avaliação subjetiva do código. Serão avaliados pontos como nome de classes, tipagem, etc.

import turtle
import time
import math

class Forma():
    def __init__(self, nome, cor, x,y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
        
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)
        self.desenhar_forma(t)
        t.end_fill()

    def desenhar_forma(self, t: turtle.Turtle):
        raise Exception("Metodo Alternativo")
    

# criando as classes das formas: retangulo, triangulo, circulo

class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retangulo', cor, x, y)
        self.largura = largura
        self.altura = altura
        

    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)
        t.end_fill()

class Triangulo(Forma):
    def __init__(self, lado, cor, x, y):
        super().__init__('Triangulo', cor, x, y)
        self.lado = lado

    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        for _ in range(3):
            t.forward(self.lado)
            t.right(120)
        t.end_fill()

class Circulo(Forma):
    def __init__(self, raio, cor, x, y):
        super().__init__('Circulo', cor, x, y)
        self.raio = raio

    def desenhar_forma(self, t: turtle.Turtle):
        t.begin_fill()
        t.circle(self.raio)
        t.end_fill()

class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y):
        super().__init__('Estrela', cor, x, y)
        self.tamanho = tamanho
    
    def desenhar(self):
        t = turtle.Turtle()
        t.hideturtle()  # Oculta a tartaruga para um desenho mais limpo
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.fillcolor(self.cor)
        t.begin_fill()
        
        # Desenhando a estrela com 5 pontas
        for _ in range(5):
            t.forward(self.tamanho)


tronco = Retangulo(50, 150, 'brown', -25, -150)  # Tronco da árvore
folha1 = Circulo(50, 'green', 0, 0)  # Sol
sol = Circulo(50, 'yellow', 200, 100)  # Sol
estrela1 = Estrela(30, 'black', -150, 150)  # Estrela
estrela2 = Estrela(20, 'black', 100, 200)  # Outra estrela

# Lista de formas para desenhar
formas = [tronco, folha1, sol, estrela1, estrela2]

# Desenhando as formas e imprimindo as áreas
for f in formas:
    f.desenhar()

time.sleep(3)