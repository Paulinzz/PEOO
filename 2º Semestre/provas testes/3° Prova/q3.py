class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f"Veículo {self.marca} {self.modelo}")

class Carro(Veiculo):
    def descrever(self):
        print(f"Carro: {self.marca} {self.modelo}")

class Moto(Veiculo):
    def descrever(self):
        print(f"Moto: {self.marca} {self.modelo}")

def mostrar_detalhes(veiculo):
    veiculo.descrever()

carro = Carro("Toyota", "Corolla")
moto = Moto("Honda", "CB500")

mostrar_detalhes(carro)
mostrar_detalhes(moto)
