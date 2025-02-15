from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Quad(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

q = Quad(4)
print(q.area()) 

c = Circulo(2)
print(c.area())  