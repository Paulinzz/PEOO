# (10 pts) Agenda Telefônica: Dada uma agenda telefônica representada como um dicionário 
#(pares nome→telefone), encontre o telefone de uma pessoa, dado o seu nome. Caso o nome não esteja na agenda, exiba a mensagem "Não encontrado(a)".

agenda = {}  # Cria a agenda como um dicionário

# Preenche a agenda
continuar = True
while continuar:
    nome = input('Nome (ou digite "parar"): ')
    continuar = nome != 'parar'
    if continuar:
        telefone = input('Telefone: ')
        agenda[nome] = telefone
    

# Aqui a agenda está preenchida
# Seu trabalho é completar a resposta
        
print("Agenda", [agenda])
buscar = input("Nome para buscar: ")
if nome in agenda:
    print("telefone:", agenda[buscar])
else:
    print("Não encontrado!")
    
