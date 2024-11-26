class Dependente:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

class Pessoa:
    def __init__(self, nome: str, dependentes: list[Dependente]):
        self.nome = nome
        self.dependentes = dependentes
    def adicionar_dependentes(self, dependente: Dependente):
        self.dependentes.append(dependente)

reps1 = Pessoa("ciro" , [] )

reps1.adicionar_dependentes(Dependente("Ciro", 32))

