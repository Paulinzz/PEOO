class Conta:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.saldo = 0
    
    def depositar(self, valor: float):
        self.saldo += valor
        print(f'Depositou {valor}. Saldo atualizado: {self.saldo}.')

    def sacar(self, valor: float):
        if self.saldo < valor:
            print(f'Impossível sacar {valor}. Saldo insuficiente.')
            return
        self.saldo -= valor
        print(f'Sacou {valor}. Saldo atualizado: {self.saldo}.')


class ContaEspecial(Conta):
    def __init__(self, cliente: str, limite_especial: float):
        super().__init__(cliente)
        self.limite = limite_especial

    def sacar(self, valor: float):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(f'Sacou {valor}. Saldo atualizado: {self.saldo}.')
        else:
            print(f'Impossível sacar {valor}. Saldo insuficiente.')


# Exemplos de uso
print('Conta Comum')
comum = Conta('Arthur')
comum.depositar(100)
comum.sacar(50) 
comum.sacar(70)  
                   
print('\nConta Especial')
especial = ContaEspecial('Ze', 1000)
especial.sacar(500)
especial.depositar(500)
