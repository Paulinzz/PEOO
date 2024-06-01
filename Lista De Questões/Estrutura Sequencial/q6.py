# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print("="*15,"Programa Para Calcular A Área De Um Circulo", "="*15)

import math

pi = input("Deseja que o pi tenha valor matemático? S/N ").lower()

raio = float(input("Digite o raio do círculo: "))

if pi[0] == "s":
    pi = float("{:.2f}".format(math.pi))
    area = pi * (raio*2)
    print(f"A área do círculo é de {area:.2f}")

else:
    pi = "π"
    area = raio*2
    print(f"Área do circulo é de {area}π")
