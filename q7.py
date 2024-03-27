import time

numeros_por_extenso = {
    1 : 'Um',
    2 : 'Doiz'  # Não altere aqui
}

print(f"Dicionário antes da atualização: \n{numeros_por_extenso}")
time.sleep(1)
print("atualizado...")
time.sleep(1)
print("quase lá...")
time.sleep(1)
# Atualize aqui o texto da chave 2 para 'Dois'

del numeros_por_extenso[2]
numeros_por_extenso[2] = "Dois"

print("===Dicionario Atualizado===")
print(numeros_por_extenso)