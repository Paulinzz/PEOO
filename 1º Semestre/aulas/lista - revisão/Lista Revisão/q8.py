# Q8 (Funções): Escreva uma função chamada fatorial que receba um número inteiro não negativo e retorne o fatorial desse número. 
# O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n 
# (ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120).
#Exemplo de Entrada:
numero = 5

# Exemplo de Saída:
120

import math 
def fatorial(n):
    fat = 1
    for i in range(2, n+1):
         fat *= i
    return fat


print(fatorial(numero))

