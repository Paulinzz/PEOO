# (30 pts) Verificação de Anagramas: Anagramas são palavras que podem ter suas letras rearranjadas para transformarem-se em outra. 
# Ex.: "padre" e "pedra" são anagramas uma da outra. Dadas duas palavras, verifique se são anagramas uma da outra e exiba "Sim" ou "Não". Use dicionários (obrigatoriamente) 
# para contar a frequência das letras em cada palavra e compare-os no final.
import time

palavra1 = str(input("Digite uma palavra: "))
palavra2 = str(input("Digite outra palavra: "))

print("vejamos se são Anagramas!")
time.sleep(1)
print("1")
time.sleep(1)
print("2")
print("="*30)


freq1 = {}
freq2 = {}


for letra in palavra1:
    # se a letra não foicontada ainda, a chave não existe
    # então eu crio a chave e coloco 0
    if letra not in freq1:
        freq1[letra] = 0
    freq1[letra] += 1    

for letra in palavra2:
    # se a letra não foicontada ainda, a chave não existe
    # então eu crio a chave e coloco 0
    if letra not in freq2:
        freq2[letra] = 0
    freq2[letra] += 1

if freq1 == freq2:
    print("São Anagramas!!")
else:
    print("Não São Anagramas!")
     
print(freq1)