# Garante que o arquivo existe
open('ranking.txt', 'a').close()

def eh_numero_inteiro(s):
    """Verifica se a string s pode ser convertida para um número inteiro."""
    return s.isdigit() or (s[1:].isdigit() if s[0] == '-' else False)

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

    if eh_numero_inteiro(pontuacao):
        pontuacao = int(pontuacao)
        with open('ranking.txt', 'a') as arq:
            arq.write(nome + '\n')
            arq.write(str(pontuacao) + '\n')
        
        print("Ranking atualizado.")
    else:
        print("Pontuação deve ser um número inteiro.")
    
    continuar = input("Deseja adicionar outro jogador? (s/n): ").strip().lower()
    if continuar != 's':
        break

