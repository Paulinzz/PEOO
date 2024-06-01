# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura = float(input("Digite a temperatura em Celsius: "))

temperatura = (temperatura * 1.8)+32
print(f"Em Fahrenheit essa temperatura é de {temperatura:.1f}F°")