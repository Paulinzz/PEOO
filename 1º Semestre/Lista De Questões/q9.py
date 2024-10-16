# (10 pts) Dicionário com Lista: Dado um responsável e uma lista de dependentes, 
# crie um dicionário onde a única chave é o nome do responsável e o valor é a lista de dependentes. 
# O usuário deve digitar primeiro o nome do responsável e em seguida o nome dos dependentes até que digite "parar". 
# Exiba o dicionário sem formatação, apenas com print(dicio).

dicio = {}

while True:
    nome = str(input("Digite o nome: (digite PARAR para o programa parar): " ))
    if nome.lower() == "parar":
        break
    dependente = str(input("Digite o seu dependente: (digite PARAR para o programa parar): " ))
    if dependente.lower() == "parar":
        break
    dicio[nome] = dependente

print(dicio)

