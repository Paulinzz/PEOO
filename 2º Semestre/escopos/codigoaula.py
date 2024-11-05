# Definição de classes e funções


def alterar(x):
    x = x + 1
    print(f'{x} (alterado na função)')


class MinhaClasse:
    def __init__(self, x):
        self.x = x
        print(f'{self.x} (criei self.x)')
        self.x = x + 1
        print(f'{self.x} (alterei self.x)')
        x = self.x + 1
        print(f'{x} (alterei x na classe)')
        alterar(x)
        print(f'{x} (chamei alterar(x) na classe)')

# Programa principal


x = 1
print(f'{x} (no começo)')


alterar(x)
print(f'{x} (voltei do alterar(x))')


meu_obj = MinhaClasse(x)
print(f'{meu_obj.x} (exibição do meu_obj)')


print(f'{x} (fim)')