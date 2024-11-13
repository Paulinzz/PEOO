class Conta:
    def __init__(self, cliente: str, tipo: str, limite_especial: float = 0):
        self.cliente = cliente
        self.saldo = 0
        self.tipo = tipo
        self.limite = limite_especial
    
    def depositar(self, valor: float):
        self.saldo += valor
        print(f'Depositou {valor}. Saldo atualizado: {self.saldo}.')

    def sacar(self, valor: float):
        saldo_disponivel = self.saldo
        if self.tipo == 'especial':
            saldo_disponivel += self.limite
        if saldo_disponivel < valor:
            print(f'Impossível sacar {valor}. Saldo insuficiente.')
            return
        self.saldo -= valor
        print(f'Sacou {valor}. Saldo atualizado: {self.saldo}.')


# Exemplos de uso
print('Conta Comum')
comum = Conta('Arthur', 'comum')
comum.depositar(100)
comum.sacar(50) 
comum.sacar(70)  
                   
print('\nConta Especial')
especial = Conta('Bruna', 'especial', 1000)
especial.depositar(500)
especial.sacar(300)   
especial.sacar(1200)  
especial.sacar(10)   
