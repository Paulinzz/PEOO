class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_salario_total(self):
        return self.salario + self.bonus

g = Gerente("João", 5000, 1500)
print(g.calcular_salario_total())  # 6500
