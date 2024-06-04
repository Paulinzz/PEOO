# Faça um Programa que leia três números e mostre o maior deles.

num_max = []

for i in range(0,3):
    num = float(input(f"Digite o {i+1}° número: "))
    num_max.append(num)

print(f"O número maior dos quais você digitou é: {max(num_max):.0f}")