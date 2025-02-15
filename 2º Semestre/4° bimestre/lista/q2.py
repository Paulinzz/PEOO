class Animal():
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def som(self):
        return self.nome + " faz um som"
    
class Cachorro(Animal):
    def som(self):
        return self.nome + " late"
        
dog1 = Cachorro("Thor", 3)
print(dog1.som())  