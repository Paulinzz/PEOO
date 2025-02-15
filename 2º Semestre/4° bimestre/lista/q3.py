
class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Gato(Animal):
    def som(self):
        return f"{self.nome} de {self.idade} Anos, Miar, Miau "
    
def exibir(animal:Animal):
    return animal.exibir()

gato = Gato("Mew", 3)
print(gato.som()) 