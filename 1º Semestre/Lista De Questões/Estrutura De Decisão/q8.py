# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

coleção = []

for i in range(0,3):
    produtos = float(input(f"Digite o {i+1}° Produto: "))
    coleção.append(produtos)
    print("Adicionado.")

minimo = min(coleção)
posição = coleção.index(minimo)
print(f"O {posição+1}° Produto é o mais barato, com o valor de: R${minimo} ")
    