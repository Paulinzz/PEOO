class Forma:
    def __init__(self, nome, cor, x, y):
        self.nome = nome
        self.cor = cor
        self.x = x
        self.y = y
 


class Retangulo(Forma):
    def __init__(self, largura, altura, cor, x, y):
        super().__init__('Retângulo', cor, x, y)
        self.largura = largura
        self.altura = altura


class Triangulo(Forma):
    def __init__(self, lado, cor, x, y):
        super().__init__('Triângulo', cor, x, y)
        self.lado = lado




class Circulo(Forma):
    def __init__(self, raio, cor, x, y):
        super().__init__('Círculo', cor, x, y)
        self.raio = raio


ret = Retangulo(75, 100, 'red', 50,50)
print("Nome:", ret.nome)
print("Altura", ret.altura)