# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
from time import sleep
from termcolor import colored

Aluno = input("Digite o nome do aluno: ")
acumulo_das_notas = 0

for i in range(0,4):
    notas = float(input(f"Insira a nota do aluno no {i+1} Bimestre: "))
    acumulo_das_notas += notas

media = acumulo_das_notas / 4
print(f"A média do aluno foi {media}, com isso ele foi... ", end="") 

sleep(1)

if media >= 6:
    print(colored("Aprovado!!","green" ))
if media < 6:
    print(colored("Reprovado","red" ))