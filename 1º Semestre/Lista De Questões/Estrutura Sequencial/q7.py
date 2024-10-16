# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

from time import sleep

lado = float(input("Digite um lado desse quadrado: "))

area  = 2*(lado * 4) 
print(f"A área calculada foi de {area/2}")
sleep(1)
print(f"O dobro da área calculada foi de {area}")

