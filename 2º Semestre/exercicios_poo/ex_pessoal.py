class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade}!")

ricaom = (Pessoa("Ricaom", 20))

ricaom.boas_vindas()

zepla = (Pessoa("zepla", 16))

zepla.boas_vindas()

zender = (Pessoa("zender", 17))

zender.boas_vindas()