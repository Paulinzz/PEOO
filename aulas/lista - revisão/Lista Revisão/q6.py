# Q6 (Listas): Escreva uma função chamada filtrar_pares que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares dessa lista.
#Exemplo de Entrada:
numeros = [10, 24, 31, 4, 5, 60, 7, 8, 9, 10]

#Exemplo de Saída:
[10, 24, 4, 60, 8, 10]


def filtrar_pares(lista):
    lista_nova = []
    lista = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista.append(lista_nova[lista])
