# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for i in range(0,3):
    num = float(input("Digite um número "))
    numeros.append(num)

numeros.sort(reverse=True)
print(numeros)