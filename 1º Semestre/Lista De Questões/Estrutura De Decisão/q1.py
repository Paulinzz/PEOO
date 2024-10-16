# Faça um Programa que peça dois números e imprima o maior deles.

num = float(input("Digite um número: "))
num1 = float(input("Digite outro número: "))

if num > num1:
    print(f"O primeiro número que você digitou {num} é maior que o segundo {num1}")
elif num1 > num:
    print(f"O Segundo número que você digitou {num1} é maior que o primeiro {num}")
else:
    print(f"Tanto o primeiro número {num}, qunato o segundo número {num1} são iguais, logo nenhum é maior do que o outro.")

