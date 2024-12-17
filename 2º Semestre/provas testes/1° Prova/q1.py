class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}")

p = Pessoa("Ana", 25, 1.68)
p.cumprimentar()
