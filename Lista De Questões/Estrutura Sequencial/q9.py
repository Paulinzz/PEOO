# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperatura = float(input("Digite a temperatura em Fahrenheit: "))

temperatura = (temperatura - 32)/1.8
print(f"Em Celsius essa temperatura é de {temperatura:.1f}C°")