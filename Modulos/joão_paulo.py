import time 
from turtle import *

shape("turtle")

speed(6)
up()
home()
setx(-500)
sety(00)  
down()

# letra J
left(90)
right(90)
forward(40)
left(90)
forward(100)
left(90)
forward(40)
right(180)
forward(70)
left(90)
right(90)
up()
forward(80)
  

# letra O
up()
setx(-400)
sety(00)  
down()
circle(50)  # Desenha um círculo com raio 50
forward(20)
up()
# letra Ã
setx(-350) # distancia
sety(100) # altura
down()
forward(80)
right(90)
forward(100)
right(180)
forward(40)
left(90)
forward(80)
left(90)
forward(40)
right(180)
forward(100)
    # "til" "~"
up()
setx(-300)  # Mesma distância da letra
sety(150)  # Altura ajustada para cima
down()
left(45)
circle(20, 90)
right(90)
circle(20, 90)
up()

# letra O
setx(-250)  # Mesma distância da letra
sety(80)  # Altura ajustada para cima
down()
circle(50)  # Desenha um círculo com raio 50
up()
forward(20)

# letra P

home()
setx(0)  # Mesma distância da letra
sety(000)  # Altura ajustada para cima
down()

# Desenha a letra P
left(90)  # Gira a tartaruga para a esquerda
forward(100)  # Anda pra frente
for i in range(3): 
   right(90)  # Gira a tartaruga para a direita
   forward(50)
up()  # Levanta a caneat

# letra A
home()
setx(70) # distancia
sety(100) # altura
down()
forward(80)
right(90)
forward(100)
right(180)
forward(40)
left(90)
forward(80)
left(90)
forward(40)
right(180)
forward(100)
up()
# letra U
up()
home()
setx(150)  # Define a posição x inicial
sety(-20)   # Define a posição y inicial
# Desenhar a letra "U"
left(90)  # Vira para cima (posição inicial)
forward(100)  # Desenha o primeiro lado vertical
down()
right(180)  # Vira para desenhar a parte inferior curva
circle(70, 180)  # Desenha uma meia-circunferência
up()
right(180)  # Vira para desenhar o segundo lado vertical
up()
# letra L
home()
setx(200)
sety(100)
down()
right(90)
forward(100)
left(90)
forward(100)
# letra O
up()
setx(250)  # Define a posição x inicial
sety(70)  # Define a posição y inicial
down()
circle(50)  # Desenha um círculo com raio 50


time.sleep(3)