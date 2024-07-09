# Q9 (Listas e Dicionários): Dada uma lista de dicionários onde cada dicionário representa um produto com seu nome e preço, 
# escreva uma função chamada produto_mais_caro que receba essa lista e retorne o nome do produto mais caro.
# Exemplo de Entrada:
produtos = [
    {'nome': 'Arroz', 'preco': 5.50},
    {'nome': 'Feijão', 'preco': 7.30},
    {'nome': 'Macarrão', 'preco': 4.80},
]

# Exemplo de Saída:
'Feijão'

def produto_mais_caro(produtos):
    mais_caro = 0
    