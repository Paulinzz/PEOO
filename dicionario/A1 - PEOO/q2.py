# Veja a resposta anterior, você já sabe como preencher a agenda

# (20 pts) Agenda Telefônica (busca ao contrário): Dada uma agenda telefônica representada como um dicionário 
# (pares nome→telefone), encontre o nome de uma pessoa, dado o seu telefone (assuma que só haverá uma pessoa com aquele número). 
# Caso o número não esteja na agenda, exiba a mensagem "Não encontrado(a)

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
buscar = (input("telefone para buscar: "))

encontrado = False
#for nome, telefone in agenda.items():
#    if buscar in agenda.values():
#        print("telefone:", agenda[nome])
#    else: 
#        print("Não encontrado!!")

for chave in agenda.keys():
    if buscar in agenda.values():
        if agenda[chave] == buscar:
            print("telefone:", chave)
    else:
        print("Não encontrado!")
    
