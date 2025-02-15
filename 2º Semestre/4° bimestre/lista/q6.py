class Contabacaria():
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Quebrou né pai")

    def get_saldo(self):
        return self.saldo
    
conta = Contabacaria()
conta.depositar(1000)
conta.sacar(200)
print(conta.get_saldo()) 
        