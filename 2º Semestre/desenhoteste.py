import turtle
import time
import math

class Forma:
    def __init__(self, nome, cor, x, y):
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
        t.begin_fill()   
        self.desenhar_forma(t)
        t.end_fill()  
    
    def desenhar_forma(self, t: turtle.Turtle):
        raise Exception('Método abstrado. Sobrescreva-o nas subclasses.')
    
class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retângulo', cor, x, y)
        self.largura = largura
        self.altura = altura

    def desenhar_forma(self, t: turtle.Turtle):
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)

class Triangulo(Forma):
    def __init__(self, lado, cor, x, y):
        super().__init__('Triângulo', cor, x, y)
        self.lado = lado
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor) 
        t.begin_fill()   
        t.left(60)
        for _ in range(3):
            t.right(120)
            t.forward(self.lado)
        t.end_fill()  
    def area(self):
        return ((self.lado**2) * (3**(1/2))) / 4

class Circulo(Forma):
    def __init__(self, raio, cor, x, y):
        super().__init__('Círculo', cor, x, y)
        self.raio = raio
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  
        t.begin_fill()  
        t.left(180) 
        t.circle(self.raio)
        t.end_fill()  

    def area(self):
        return 2 * math.pi * self.raio

class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y):
        super().__init__('Estrela', cor, x, y)
        self.lado = tamanho
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  #
        t.begin_fill()   # Inicia o preenchimento
        t.left(72)
        for _ in range(5):
            t.right(144)
            t.forward(self.lado)
        t.end_fill()  


# add estrela

class Estrela(Forma):
    def __init__(self, tamanho, cor, x, y):
        super().__init__('Estrela', cor, x, y)
        self.lado = tamanho
    
    def desenhar(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)  # Escolhe a cor do preenchimento
        t.left(72)
        for _ in range(5):
            t.right(144)
            t.forward(self.lado)

ret = Retangulo(800 , 500 , 'green' , -400 , -100)
ret2 = Retangulo(250 , -200 , 'lightblue' , 100 , -100)
ret3 = Retangulo(50 , -105 , 'red' , 140 , -100 )
tri = Triangulo(260 , 'brown' , 225, 320) 
tri2 = Triangulo(75 , 'yellow' , -150 , -150)
tri3 = Triangulo(85 , 'yellow' , -200 , -141)
circ = Circulo(20 , 'yellow' , -150 , -120)
circ2 = Circulo(25 , 'yellow' , - 200 , -100)
lua = Circulo(50, "lightyellow", -220, 200)
est = Estrela(50 , 'black' , -300 , 300)
est2 = Estrela(50 , 'black' , -250 , 270)
est3 = Estrela(50 , 'black' , -200 , 250)
est4 = Estrela(50 , 'black' , -150 , 200)
est5 = Estrela(50, "black", -100, 150 )
est6 = Estrela(50 , 'black' , 0 , 100)
est7=  Estrela(50, "black", 100, 225)



formas = [ret , ret2 , ret3 , tri , tri2 , circ, tri3 , circ2, lua, est, est2, est3, est4, est5, est6, est7]

turtle.Screen().bgcolor("Dark Blue")

for f in formas:
    f.desenhar()

time.sleep(5)