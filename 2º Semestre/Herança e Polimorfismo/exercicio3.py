'''Represente uma pessoa como uma classe
uma pessoa tem um nome e uma idade
a pessoa sabe:
 - Fazer uma saudação
 - Ex: oi, sou fulano e tenho "x" anos'''


class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola, eu sou {self.nome} e tenho {self.idade} anos")

    def envelhecer(self,anos):
        self.idade += anos


pessoa = Pessoa("Ciro", 43)

pessoa.apresentar()

pessoa.envelhecer(5)

pessoa.apresentar()