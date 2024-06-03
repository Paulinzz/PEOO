# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo

num = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
real = float(input("Digite um número real: "))
# A)
multiplicação = (2*num) * (num2/2)
print(multiplicação)

# B)
soma = (3*num) + real
print(soma)

# C)
cubo = real ** 3
print(cubo)