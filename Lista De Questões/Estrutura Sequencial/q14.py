# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

ganho_hora = float(input("Digite quanto você ganha por hora: "))
numero_de_horas = int(input("Digite o número de horas trabalhadas no mês: "))


#A)
salario_bruto = ganho_hora * numero_de_horas
print(f"Seu salário bruto é de R$: {salario_bruto:.2f}")

#B)
inss = (salario_bruto * 0.08)
print(f"O desconto do seu salario pra o INSS foi: R${inss:.2f}")

#C)
sindicato = (salario_bruto * 0.05)
print(f"O desconto sobre o salario para o sindicato foi de R${sindicato:.2f}")

#imposto de renda
imposto = (salario_bruto * 0.11)

#D)
salario_liquido = salario_bruto - (inss + imposto + sindicato)
print(f"Seu salário líquido é de: R${salario_liquido:.2f}")
