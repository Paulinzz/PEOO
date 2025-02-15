from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod

    def ligar(self):
        pass

    def desligar(self):
        return "Veiculo Desligado"

class Carro(Veiculo):
    def ligar(self):
        return "Carro ligado"

c = Carro()
print(c.ligar())  
print(c.desligar())

