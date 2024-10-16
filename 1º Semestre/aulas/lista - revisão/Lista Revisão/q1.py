#Q1 (Listas): Dada a lista abaixo, 
# qual será o resultado após a execução das operações? Mostre o estado final da lista numeros.
numeros = [2, 4, 6, 8, 10]
numeros.append(12)
numeros.remove(4)
numeros[2] = 14

# A lista ficara [2,6,14,10,12]

print(numeros)