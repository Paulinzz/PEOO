class Carro():
    def __init__(self, cor, marca, modelo, ano):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f'Cor: {self.cor}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')

carro1 = Carro("Preto", "Honda", "Civic", "2024")
carro1.exibir()  