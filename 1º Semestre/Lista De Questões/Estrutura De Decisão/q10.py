# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite o turno que você estuda: ").lower()

if turno[0] == "m":
    print("Bom Dia!")
elif turno[0] == "v":
    print("Boa Tarde!")
else:
    print("Boa Noite!")
