class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

p1 = Produto("Produto1", 10, 5)
p2 = Produto("Produto2", 20, 3)
p3 = Produto("Produto3", 15, 2)

print(p1.calcular_total())  # 50
print(p2.calcular_total())  # 60
print(p3.calcular_total())  # 30
