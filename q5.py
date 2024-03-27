# Adicione o número quatro ao dicionário de números por extenso
numeros_por_extenso = {
    1 : 'Um',
    2 : 'Dois',
    3 : 'Três'
    # NÃO adicione aqui
}

valor = input("Digite por extenso o número:")
chave = len(numeros_por_extenso)+1
numeros_por_extenso[chave] = valor
# Adicione aqui usando a sintaxe dicio[chave] = valor


print(numeros_por_extenso)

# outra maneira preenchendo o dicionario: 

#n_extenso = {}

#while True:
#    numero = int(input("Digite o número: "))
#    extenso = str(input("Digite agora por extenso o número que você digitou anteriomente: "))
#    n_extenso[numero] = extenso

#    continuar = input("Deseja adicionar mais números? s/n: ")
#    if continuar.lower() == "n":
#        break

#n_extenso["4"] = "quatro" 

#print("\n===Lista Atualizada:===")

#for numero, extenso in n_extenso.items():
#    print(f"{numero}: {extenso}")