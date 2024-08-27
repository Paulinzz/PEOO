# Garante que o arquivo existe
open('ranking.txt', 'a').close()

# Daqui pra baixo vai ficar dentro do laço
# Lê do arquivo
arq = open('ranking.txt')
linhas = arq.readlines()
arq.close()
ranking = []
for i in range(0, len(linhas), 2):
     nome = linhas[i][:-1]
     pontuacao = int(linhas[i+1][:-1])
     nome_pontuacao = [pontuacao, nome]
     ranking.append(nome_pontuacao)
# Exibe a lista ordenada
# O seu trabalho é exibir os nomes e pontos bem bonitinhos
print(sorted(ranking, reverse=True))

# Pede um novo jogador e pontuação
nome = input('Jogador:')
pontuacao = input('Pontuação:')
arq = open('ranking.txt', 'a')
arq.write(nome + '\n')
arq.write(pontuacao  + '\n')
arq.close()
