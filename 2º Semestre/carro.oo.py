class Carro:
    def __init__(self, nova_cor):
        self.cor = nova_cor
        self.ligado = False
        self.velocidade = 50
        self.gasolina = 100

    def ligar(self):
        if self.gasolina > 0:
            print("Vruuuuuu")
            self.ligado = True
        else:
            print("Sem gasolina!")


    def acelerar(self):
        if self.ligado:
            print('danrandrannn')
        else:
            print("brunn...")
        self.velocidade += 10


carro1 = Carro('vermelho')
carro1.ligar()
carro1.acelerar()
carro1 = Carro('vermelho')
carro1.ligado = True


# Crie 3 objetos Carro: um vermelho com tanque vazio; um preto com 20L de gasolina; um cinza com tanque cheio, ligado e andando.
