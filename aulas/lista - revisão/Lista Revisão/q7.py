# Q7 (Dicionários): Crie um dicionário que mapeia os nomes de cinco alunos para suas respectivas notas. 
# Em seguida, escreva uma função chamada media_notas que receba esse dicionário e retorne a média das notas dos alunos.
# Exemplo de Dicionário:
notas_alunos = {
    'Alice': 8.5,
    'Bruno': 7.0,
    'Carla': 9.0,
    'Daniel': 6.5,
    'Elisa': 8.0
}

# Exemplo de Saída:
7.8

def media_notas(alunos):
    qnt_alunos = len(alunos)
    soma = 0 
    for i in alunos.values():
        soma += i
    print (soma / qnt_alunos)
    
media_notas(notas_alunos)