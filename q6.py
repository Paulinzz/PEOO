# Adicione o número 3 do dicionário de números por extenso
numeros_por_extenso = {
    1 : 'Um',
    2 : 'Dois',
    3 : 'Três' # NÃO remova daqui
}

valor = input("Digite por extenso o numero que deseja retirar: ")
chave = len(numeros_por_extenso)
del numeros_por_extenso[chave] 

# Remova aqui usando a sintaxe `del dicio[chave]`


print(numeros_por_extenso)

