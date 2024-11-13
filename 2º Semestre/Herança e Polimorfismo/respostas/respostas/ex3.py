class Conta:
    def __init__(self, cliente: str):
        self.cliente = cliente
        self.historico = []
    
    def saldo(self) -> float:
        s = 0
        for movimentacao in self.historico:
            if movimentacao['tipo'] == 'Saque':
                s -= movimentacao['valor']
            elif movimentacao['tipo'] in ['Depósito', 'Rendimento']:
                s += movimentacao['valor']
        return s

    def depositar(self, valor: float):
        self.historico.append({'tipo':'Depósito', 'valor': valor})
        print(f'Depositou {valor}. Saldo atualizado: {self.saldo()}.')

    def sacar(self, valor: float):
        if self.saldo() >= valor:
            self.historico.append({'tipo':'Saque', 'valor': valor})
            print(f'Sacou {valor}. Saldo atualizado: {self.saldo()}.')
        else:
            print(f'Impossível sacar {valor}. Saldo insuficiente.')

    def exibir_historico(self):
        print('Histórico de Movimentação de Conta')
        print('----------------------------------')
        for movimentacao in self.historico:
            print(movimentacao["tipo"], '-', movimentacao["valor"])


class ContaEspecial(Conta):
    def __init__(self, cliente: str, limite_especial: float):
        super().__init__(cliente)
        self.limite = limite_especial

    def sacar(self, valor: float):
        if self.saldo() + self.limite >= valor:
            self.historico.append({'tipo':'Saque', 'valor': valor})
            print(f'Sacou {valor}. Saldo atualizado: {self.saldo()}.')
        else:
            print(f'Impossível sacar {valor}. Saldo insuficiente.')


class ContaPoupanca(Conta):
    def __init__(self, cliente: str, limite_por_saque: float):
        super().__init__(cliente)
        self.limite_por_saque = limite_por_saque

    def sacar(self, valor: float):
        if valor > self.limite_por_saque:
            print(f'Impossível sacar {valor}. Limite de {self.limite_por_saque} por saque.')
            return
        if valor > self.saldo():
            print(f'Impossível sacar {valor}. Saldo insuficiente.')
            return
        self.historico.append({'tipo':'Saque', 'valor': valor})
        print(f'Sacou {valor}. Saldo atualizado: {self.saldo()}.')
    
    def render(self, meses):
        rendimento = self.saldo() * 0.005 * meses  # Juros simples
        self.historico.append({'tipo': 'Rendimento', 'valor': rendimento})
        print(f'Rendeu {rendimento} em {meses} meses. Saldo atualizado: {self.saldo()}.')

# Exemplos de uso
print('Conta Comum')
comum = Conta('Arthur')
comum.depositar(100)
comum.sacar(50) 
comum.sacar(70)  
                   
print('\nConta Especial')
especial = ContaEspecial('Bruna', 1000)
especial.depositar(500)
especial.sacar(300)
especial.sacar(1200)
especial.sacar(10)

print('\nConta Poupança')
poupanca = ContaPoupanca('Cícero', 1000)
poupanca.depositar(1500)
poupanca.sacar(1100)
poupanca.sacar(700)
poupanca.sacar(900)
poupanca.render(6)
poupanca.exibir_historico()