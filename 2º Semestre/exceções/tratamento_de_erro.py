premios = ['bicicleta', 'playstation', 'pirulito', 'lápis', '10pts extra']
tentativas = 0
selecionado = ''

while True:
    try:
        entrada = input(f"Escolha um prêmio secreto (0-{len(premios)-1}): ")
        indice = int(entrada)  # Aqui pode dar ValueError se o texto digitado
                               # não for um inteiro
        selecionado = premios[indice]  # Aqui pode dar IndexError se o índice
                                       # estiver fora da lista
        # Se chegou aqui, não houve lançamento de exceção, então temos um
        # prêmio selecionado e podemos encerrar o laço.
        break
    except ValueError:
        # Foi lançada uma exceção do tipo ValueError, indicando que o
        # valor digitado não pôde ser convertido porque não é um número.
        print("Ops! Isso não é um número inteiro. Tente novamente.")
    except IndexError:
        # Foi lançada uma exceção do tipo IndexError, indicando que o valor
        # digitado não pôde ser convertido porque não é um número
        print(f"Prêmio fora do intervalo. Tente algo entre 0 e {len(premios)-1}.")
    finally:
        # Executa sempre, independente de ter havido erro ou não (inclusive break!)
        tentativas += 1

print('Prêmio selecionado:', selecionado)
print('Tentativas:', tentativas)
