#Q5 (Funções com Listas e Dicionários): Considere a função abaixo. 
#Descreva o que a função faz e qual será a saída quando a lista palavras for 
#['gato', 'cachorro', 'gato', 'passaro', 'gato'].
def func2(lista):
    aux = {}
    for item in lista:
        if item in aux:
            aux[item] += 1
        else:
            aux[item] = 1
    return aux

resultado = func2(['gato', 'cachorro', 'gato', 'passaro', 'gato'])

# o resultado sera quantas vezes a palavra repetiu

