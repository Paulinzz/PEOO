# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ["A","O","I","E","U"]

letra = input("Digite uma letra: ").upper()

if letra in vogal:
    print("Vogal")
else:
    print("Consoante")