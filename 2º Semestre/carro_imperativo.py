# Paradigma Imperativo
def novo_carro(nova_cor):
    carro = {}
    carro['cor'] = nova_cor
    carro['ligado'] = False
    carro['velocidade'] = 0
    carro['gasolina'] = 0
    return carro

def ligar(carro):
    if carro['gasolina'] > 0:
        carro['ligado'] = True

def acelerar(carro):
    carro['velocidade'] += 10

carro1 = novo_carro('vermelho')
ligar(carro1)
acelerar(carro1)