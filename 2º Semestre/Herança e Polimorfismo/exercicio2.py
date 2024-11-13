'''represente uma pessoa com uma classe.
uma pessoa tem um nome e uma idade
para testar, crie 3 pessoas
 - Ciro, 43 anos
 - Mickeias - 96
 - Ricaom - 204 anos'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola, eu sou {self.nome} e tenho {self.idade} anos")


Ciro = Pessoa("Ciro", 43)

Mickeias = Pessoa("Mickeias", 96)

Ricaom = Pessoa("Ricaom", 204)

Ciro.apresentar()

Mickeias.apresentar()

Ricaom.apresentar()