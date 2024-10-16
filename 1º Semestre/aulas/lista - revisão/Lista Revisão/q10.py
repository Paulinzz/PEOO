#Q10 (Funções com Listas e Dicionários): Escreva uma função chamada contar_frequencia que receba uma lista de palavras e retorne um dicionário onde as chaves são as palavras e os valores são o número de ocorrências de cada palavra na lista.
#Exemplo de Entrada:
palavras = ['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']

#Exemplo de Saída:
{
    'maçã': 3,
    'banana': 2,
    'laranja': 1
}

def contar_frequencia(lista):
    aux = {}
    for item in lista:
        if item in aux:
            aux[item] += 1
        else:
            aux[item] = 1
    return aux

print(contar_frequencia(palavras))