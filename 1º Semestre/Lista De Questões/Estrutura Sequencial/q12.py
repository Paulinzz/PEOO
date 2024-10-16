# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

while True:
    sexo = input("Qual o seu sexo? M/F ").lower()
    if sexo[0] == "m":
        altura = float(input("qual a sua altura em metros? "))
        peso_ideal = (72.7*altura) - 58 
        print(f"Para sua altura de {altura}M no sexo Masculino, seu peso ideal seria de {peso_ideal:.2f}KG")
        break
    elif sexo[0] == "f": 
        altura = float(input("qual a sua altura em metros? "))
        peso_ideal = (62.1*altura) - 44.7
        print(f"Para sua altura de {altura}M no sexo Feminino, seu peso ideal seria de {peso_ideal:.2f}KG")
        break
    else:
        print("Digite novamente...")