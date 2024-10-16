# Faça um Programa que leia três números e mostre o maior e o menor deles.

num_min = []

for i in range(0,3):
    num = float(input(f"Digite o {i+1}° número: "))
    num_min.append(num)
print(f"O número menor dos quais você digitou é: {min(num_min):.0f}")