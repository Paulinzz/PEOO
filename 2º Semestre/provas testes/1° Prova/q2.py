class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

end = Endereco("Rua A", 123, "Cidade X")
pessoa = Pessoa("João", end)

print(f"Nome: {pessoa.nome}, Endereço: {pessoa.endereco.rua}, {pessoa.endereco.numero}, {pessoa.endereco.cidade}")
