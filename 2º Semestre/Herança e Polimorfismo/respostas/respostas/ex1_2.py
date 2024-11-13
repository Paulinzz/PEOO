class Conta:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.saldo = 0
    
    def depositar(self, valor: float):
        self.saldo += valor
        print(f'Depositou {valor}. Saldo atualizado: {self.saldo}.')


class ContaComum(Conta):
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
        if self.saldo + self.limite < valor:
            print(f'Impossível sacar {valor}. Saldo insuficiente.')
            return
        self.saldo -= valor
        print(f'Sacou {valor}. Saldo atualizado: {self.saldo}.')


# Exemplos de uso
print('Conta Comum')
comum = ContaComum('Arthur')
comum.depositar(100)
comum.sacar(50) 
comum.sacar(70)  
                   
print('\nConta Especial')
especial = ContaEspecial('Bruna', 1000)
especial.depositar(500)
especial.sacar(300)   
especial.sacar(1200)  
especial.sacar(10)   
