open('ranking.txt', 'a').close()

while True:
    with open('ranking.txt', 'r') as arq:
        linhas = arq.readlines()

    ranking = []
    for i in range(0, len(linhas), 2):
        nome = linhas[i].strip()
        pontuacao = int(linhas[i+1].strip())
        ranking.append([pontuacao, nome])

    ranking_ordenado = sorted(ranking, reverse=True)

    print("Ranking:")
    for pontuacao, nome in ranking_ordenado:
        print(f"{nome}: {pontuacao}")

    nome = input('Jogador: ').strip()
    pontuacao = input('Pontuação: ').strip()

    try:
        pontuacao = int(pontuacao)
    except ValueError:
        print("Pontuação deve ser um número inteiro.")
        continue

    with open('ranking.txt', 'a') as arq:
        arq.write(nome + '\n')
        arq.write(str(pontuacao) + '\n')

    print("Ranking atualizado.")

    continuar = input("Deseja adicionar outro jogador? (s/n): ").strip().lower()
    if continuar != 's':
        break
