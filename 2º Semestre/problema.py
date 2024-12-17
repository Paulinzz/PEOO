'''Este exemplo mostra por que não devemos usar listas vazias como valor padrão de funções ou métodos.

O problema, entretanto, vai além de listas, estendendo-se a qualquer objeto complexto do Python, como dicionários e objetos de classes quaisquer.
O recomendado é atribuir valores padrão apenas se forem de tipos primitivos (int, bool, str, float) ou None.
'''

class Errada:
    def __init__(self, lista = []):
        '''Ao definirmos o valor padrão do parâmetro lista, o Python cria uma lista vazia e a guarda na memória para usos futuros.
        Assim, todas os objetos que forem criados com o valor padrão compartilharão a referência para *a mesma* lista vazia.'''
        self.lista = lista

class Certa:
    def __init__(self, lista):
        '''Se não definirmos um valor padrão para o parâmetro lista, deixamos a responsabilidade de criá-la para quem está criando o objeto.'''
        self.lista = lista

# Aqui, a lista de e1 e e2 é a mesma
e1 = Errada()
# Logo, alterar e1.lista também altera e2.lista
e1.lista.append('Adicionado a e1.lista')
e2 = Errada()
print('e2.lista =', e2.lista)

# Aqui, criamos duas listas vazias distintas
c1 = Certa([])
# Logo, alterar c1.lista não altera c2.lista
c1.lista.append('Adicionado a c1.lista')
c2 = Certa([])
print('c2.lista =', c2.lista)