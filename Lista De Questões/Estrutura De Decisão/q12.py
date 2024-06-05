# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor = float(input("Digite a quanto você ganha por hora: "))
quantidade_de_horas = int(input("Digite a quantidade horas trabalhadas no mês: "))
salario_bruto = valor * quantidade_de_horas

if salario_bruto <= 900:
    salario_liquido = salario_bruto
    print(f"Com o valor por horas de: R${valor} e de horas no mês {quantidade_de_horas}")    
    print(f"Seu salário Bruto é de: R${salario_bruto}\n Seu salário Líquido é de: R${salario_liquido}")
elif 900 < salario_bruto <= 1500:
    imposto = salario_bruto * 0.05
    salario_liquido = salario_bruto - imposto
    print(f"Com o valor por horas de: R${valor} e de horas no mês {quantidade_de_horas}")
    print(f"Seu salário Bruto é de: R${salario_bruto}\n Seu salário Líquido é de: R${salario_liquido} devido ao imposto de renda")
elif 1500 < salario_bruto <= 2500:
    imposto = salario_bruto * 0.1
    salario_liquido = salario_bruto - imposto
    print(f"Com o valor por horas de: R${valor} e de horas no mês {quantidade_de_horas}")
    print(f"Seu salário Bruto é de: R${salario_bruto}\n Seu salário Líquido é de: R${salario_liquido} devido ao imposto de renda")
elif salario_bruto > 2500:
    imposto = salario_bruto * 0.2
    salario_liquido = salario_bruto - imposto
    print(f"Com o valor por horas de: R${valor} e de horas no mês {quantidade_de_horas}")
    print(f"Seu salário Bruto é de: R${salario_bruto}\n Seu salário Líquido é de: R${salario_liquido} devido ao imposto de renda") 

# devo atualiza algumas coisas ainda