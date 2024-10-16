# Crie 3 objetos Carro: um vermelho com tanque vazio; um preto com 20L de gasolina; um cinza com tanque cheio, ligado e andando.

class Carro:
    def __init__(self, nova_cor):
        self.cor = nova_cor
        self.ligado = False
        self.velocidade = 50
        self.gasolina = 50 
        
    def ligar(self):        
        if self.gasolina > 0:
            print("Vruuuuuu")
            self.ligado = True
        else:
            print("Sem gasolina!")


    def acelerar(self):
        if self.ligado:
            print('danrandrannn')
            self.velocidade += 10
        else:
            print("brunn...")
    def abastecer(self, qtd):
        if self.gasolina + qtd > 50:
            excedente = (self.gasolina + qtd - 50)
            print (f"Abastecido com {qtd}L. Excedente de {excedente}")
            
carro1 = Carro("vermelho")
carro1.ligar()
carro1.acelerar()
carro1.abastecer(10)