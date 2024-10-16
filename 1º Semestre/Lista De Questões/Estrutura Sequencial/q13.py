# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso do peixe: "))

if peso > 50:
    peso_excedente = peso - 50
    multa = peso_excedente * 4 
    print(f"Devido ao peso do peixe excede 50 KG com {peso}KG, devera pagar RS{multa} em multa por quilo excedente. ")
    print("Encerrado...")

else:
    print(f"com o peso de {peso}KG não excesso, logo não pagaram acrescimo. ")   
    print("Encerrado...")