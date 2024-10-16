print("Digite os produtos do primeiro estoque (0 para parar):")

estoque1 = {}

while True:
    id_produto = int(input("ID: "))
    if id_produto == 0:
        break
    nome_produto = input("Nome: ")
    quantidade_produto = int(input("Quantidade: "))
    estoque1[id_produto] = {'nome': nome_produto, 'quantidade': quantidade_produto}

print("\nDigite os produtos do segundo estoque (0 para parar):")

estoque2 = {}

while True:
    id_produto = int(input("ID: "))
    if id_produto == 0:
        break
    nome_produto = input("Nome: ")
    quantidade_produto = int(input("Quantidade: "))
    estoque2[id_produto] = {'nome': nome_produto, 'quantidade': quantidade_produto}

estoque_final = {}

for id_produto, produto in estoque1.items():
    estoque_final[id_produto] = produto

for id_produto, produto in estoque2.items():
    if id_produto in estoque_final:
        estoque_final[id_produto]['quantidade'] += produto['quantidade']
    else:
        estoque_final[id_produto] = produto

print("\nEstoque final:")
print(estoque_final)