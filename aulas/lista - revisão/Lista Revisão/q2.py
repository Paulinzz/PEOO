# Q2 (Dicionários): Considere o dicionário produtos abaixo, que mapeia os nomes de produtos aos seus preços. 
# Mostre o estado final do dicionário após a execução do código.
produtos = {'Arroz': 5.50, 'Feijão': 7.30, 'Macarrão': 4.80}
preco_feijao = produtos['Feijão']
produtos['Morango'] = 25.00
del produtos['Arroz']

# ficara com o dicionário {"Feijão:"7.30, "Macarrão":4.80, "Morango" = 25.00}

print(produtos)