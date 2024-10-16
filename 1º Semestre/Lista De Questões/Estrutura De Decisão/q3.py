# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o seu sexo: M/F ").lower()
if sexo[0] == "m":
    print("Masculino")
elif sexo == "f":
    print("Feminino")
else:
    print("Sexo invalido")