pessoa = dict()
lista = list()
res = 'S'

while True:
    if res in 'Ss':
        pessoa['nome'] = str(input('Nome: '))

        while True:
            pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
            if pessoa['sexo'] not in 'MmFf':
                print('\033[1;31mERRO! O valor digitado não esta em [M/F]... Tente novamente...\033[m')
            else:
                break

        pessoa['idade'] = int(input('Idade: '))

        while True:
            res = input('Quer continuar? [S/N] ').upper()[0]
            if res not in 'SsNn':
                print('\033[1;31mERRO! O valor digitado não esta em [S/N]... Tente novamente...\033[m')
            else:
                break

        lista.append(pessoa.copy())

    elif res in 'Nn':
        break

print('-=' * 30)
print(f' -Foram cadastradas o total de {len(lista)} pessoas')

somaidade = 0
for i, v in enumerate(lista):
    somaidade += v['idade']
print(f' -A media das idades é igual a: {somaidade / len(lista):.1f} anos')

print(f' -As mulheres cadastradas foram: ', end='')
for i, v in enumerate(lista):
    if v['sexo'] in 'Ff':
        print(v['nome'], end=' ')
print()

print(' -pessoas com idade acima da media: ')
for i, v in enumerate(lista):
    if v['idade'] > (somaidade / len(lista)):
        for k, valor in v.items():
            print(f'  -{k} é {valor} ;', end=' ')
        print()

print('-=' * 30)
print('\033[1;32mPrograma finalizado com sucesso...')
print('Volte sempre :D\033[m')  