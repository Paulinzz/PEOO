class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

c = ContaBancaria("Maria", 0)
c.depositar(500)
c.sacar(600)  # Saldo insuficiente!
c.sacar(400)
print(f"Saldo final: {c.saldo}")  # Saldo final: 100
