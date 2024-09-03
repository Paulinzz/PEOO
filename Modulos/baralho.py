"""Jogo de Baralho"""

import colorama

# Inicialização do módulo colorama
colorama.init()
colorama.just_fix_windows_console()


# CONSTANTES

SIMBOLOS = [' A', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K']

# Naipes
COPAS = '♥️'
ESPADAS = '♠️'
OURO = '♦️'
PAUS = '♣️'


# FUNÇÕES

def formatar_carta(simbolo, naipe):
    cor = colorama.Fore.BLACK
    fundo = colorama.Back.WHITE
    if naipe in [COPAS, OURO]:
        cor = colorama.Fore.RED
    return fundo + cor + simbolo + naipe + ' ' + colorama.Style.RESET_ALL

def exibir_baralho():
        for naipe in [COPAS, ESPADAS, OURO, PAUS]:
            print((colorama.Back.WHITE + '    ' + colorama.Style.RESET_ALL + '   ')*len(SIMBOLOS))
            for simbolo in SIMBOLOS:
                print(formatar_carta(simbolo, naipe), end='   ')
            print()
            print((colorama.Back.WHITE + '    ' + colorama.Style.RESET_ALL + '   ')*len(SIMBOLOS))
            print('\n')


# PROGRAMA PRINCIPAL

if __name__ == '__main__':
    exibir_baralho()