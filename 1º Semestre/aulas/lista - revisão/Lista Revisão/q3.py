# Q3 (Funções): Explique o que faz a função func abaixo e qual o valor de resultado quando n for igual a 5.
def func1(n):
    aux = 0
    for i in range(1, n + 1):
        aux += i
    return aux

resultado = func1(5)

# o resultado sera 15, devido ao somatorio 

