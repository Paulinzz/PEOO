def maior(idade):
    if idade >= 18:
        return "Maior"
    return "Menor"

print(maior(float(input("Digite sua idade: "))))