"""Jogo de Xadrez"""

import colorama

# Inicialização do módulo colorama
colorama.init()
colorama.just_fix_windows_console()


# CONSTANTES

PECAS: dict[str, str] = {
    'X': '♚',  # Rei
    'R': '♛',  # Rainha
    'T': '♜',  # Torre
    'B': '♝',  # Bispo
    'C': '♞',  # Cavalo
    'P': '♟',  # Peão
    ' ': ' '   # Vazio
}


# FUNÇÕES

def criar_tabuleiro():
    return [
        ['Tp', 'Cp', 'Bp', 'Rp', 'Xp', 'Bp', 'Cp', 'Tp'],
        ['Pp', 'Pp', 'Pp', 'Pp', 'Pp', 'Pp', 'Pp', 'Pp'],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
        ['Tb', 'Cb', 'Bb', 'Rb', 'Xb', 'Bb', 'Cb', 'Tb'],
    ]

def pintar_peca(codigo: str) -> str:
    peca_ = PECAS[codigo[0]]
    cor = colorama.Style.BRIGHT
    cor += colorama.Fore.BLACK if codigo[1] == 'p' else colorama.Fore.WHITE
    return cor + peca_

def exibir_indices():
    print(' ' * 3, end='')
    for j in range(1, 9):
        n = '  ' + str(j) + '   '
        print(n, end='')
    print()

def indice_letra(i: int):
    return chr(i+97)

def exibir_tabuleiro(tabuleiro):
    exibir_indices()
    for i, linha in enumerate(tabuleiro):
        completar_altura_da_linha(i, tabuleiro)
        print(indice_letra(i), end=' ')
        for j in range(len(linha)):
            bg = colorama.Back.YELLOW
            if (i + j) % 2 == 0:
                bg = colorama.Back.RED
            peca = pintar_peca(linha[j])
            print(f'{bg}  {peca}   {colorama.Style.RESET_ALL}', end='')
        print('', indice_letra(i))
        exibir_linha_com_posicoes(i, tabuleiro)
    exibir_indices()    

def completar_altura_da_linha(indice, tabuleiro):
    linha = tabuleiro[indice]
    print('  ', end='')
    for j in range(len(linha)):
        bg = colorama.Back.YELLOW
        if (indice + j) % 2 == 0:
            bg = colorama.Back.RED
        print(f'{bg}      {colorama.Style.RESET_ALL}', end='')
    print()

def exibir_linha_com_posicoes(indice, tabuleiro):
    linha = tabuleiro[indice]
    letra = indice_letra(indice)
    print('  ', end='')
    for j in range(len(linha)):
        bg = colorama.Back.YELLOW
        if (indice + j) % 2 == 0:
            bg = colorama.Back.RED
        print(f'{bg}  {letra}{j+1}  {colorama.Style.RESET_ALL}', end='')
    print()

# PROGRAMA PRINCIPAL

if __name__ == '__main__':
    tabuleiro = criar_tabuleiro()
    exibir_tabuleiro(tabuleiro)