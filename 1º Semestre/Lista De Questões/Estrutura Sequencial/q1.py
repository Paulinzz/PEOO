# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

from time import sleep
from termcolor import colored

print(colored ("Progama iniciado...", "green"))
sleep(0.5)

for i in range(1):
    nome = input(colored("Seu nome? ","blue"))
    print("Aguarde...")
    sleep(0.7)
    impressão = (f"Hello World, {nome}")

print(colored(impressão,"white","on_blue"))