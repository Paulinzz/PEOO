print("="*30)
Area = 0 
def area(comp,lag):
    area = comp * lag
    return area

comprimento = float(input("Digite o comprimento(m): "))
lagura = float(input("Digite a largura(m): "))
print(f"A área do terreno com uma área:{lagura}x{comprimento} é de:", area(comprimento,lagura), "m²")
print("="*30)