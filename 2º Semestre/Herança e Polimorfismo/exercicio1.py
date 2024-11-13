#Modele um Banco usando classes. Requisitos do Banco:
#Uma conta tem um cliente e um saldo e aceita saques e depósitos.
#Só deve ser possível fazer um saque se houver saldo suficiente na conta.
#Uma conta pode ser comum ou especial. Contas especiais têm um limite 
#adicional em reais para saque além do saldo.
#Faça um desenho representando as classes e o relacionamento entre elas 
# como os apresentados neste slide e, em seguida, implemente seu projeto 
# em Python.

class Conta:
    def __init__(self, cliente: str):
        self.saldo = 0
        self.cliente = cliente

    def sacar(self, valor: float):
        if valor > self.saldo:
            print(f"Valor {valor} não pode ser sacado, saldo insuficiente. Saldo disponível: {self.saldo}")
        else:
            self.saldo -= valor
            print(f"Valor {valor} foi sacado com sucesso. Saldo atual: {self.saldo}")
    
    def depositar(self, valor: float):
        self.saldo += valor
        print(f"Valor {valor} foi depositado com sucesso. Saldo atual: {self.saldo}")

class Conta_Especial(Conta):
    def __init__(self, cliente, limite_especial):
        super().__init__(cliente)
        self.limite = limite_especial
    
    def sacar(self, valor: float):
        if self.saldo + self.limite < valor:
            print(f" Valor {valor} foi sacado, agora você tem {self.saldo} de saldo")
            self.saldo -= valor
        else:
            print(f"Valor {valor} nao pode ser sacado, saldo insuficiente")


    
comum = Conta("JP")
comum.depositar(100)
comum.sacar(50)


especial = Conta_Especial("JP", 1000)
especial.depositar(100)
especial.sacar()
especial.depositar(100)