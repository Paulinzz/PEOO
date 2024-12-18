class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print("O animal está emitindo som")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro está latindo")

a = Animal("Genérico", "Desconhecida")
c = Cachorro("Rex", "Cão")

a.emitir_som()
c.emitir_som()
