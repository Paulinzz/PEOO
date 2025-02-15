class Motor():
    def __init__(self, cavalos):
        self.cavalos = cavalos
    
    def ligar(self):
        return "Moto Ligado"
    
class Carro():
    def __init__(self,marca,modelo,motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    
    def ligar(self):
        return self.motor.ligar()

Cavalos = Motor(550)
Carro1 = Carro("Fiat", "Uno-Escadinha", Cavalos)
print(Carro1.ligar())
        