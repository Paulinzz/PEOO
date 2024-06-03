# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe 
# o tempo aproximado de download do arquivo usando este link (em minutos).

dowload = float(input("Digite em MB o tamanho do arquivo para download: "))
velocidade = float(input("Digite a velocidade da internt em Mbps: "))
tempo_aprox = dowload / velocidade

print (f"Em Média o tempo aproximado para download do arquivo específico é de {tempo_aprox:.0f} Min")
