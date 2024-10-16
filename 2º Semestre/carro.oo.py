# Paradigma Orientado a Objetos
class Carro:
    def __init__(self, nova_cor):
        self.cor = nova_cor
        self.ligado = False
        self.velocidade = 0
        self.gasolina = 0

    def ligar(self):
        if self.gasolina > 0:
            self.ligado = True

    def acelerar(self):
        self.velocidade += 10


carro1 = Carro('vermelho')
carro1.ligar()
carro1.acelerar()
