class Animal():
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def som(self):
        return self.nome + " faz um som"

class Cachorro(Animal):
    def som(self):
        return self.nome + " late"

class Gato(Animal):
    def som(self):
        return f"{self.nome} Miau "  

animais = [Cachorro("Bolt", 4), Gato("Mew", 2)]
for animal in animais:
    print(animal.som())  