class Cartao:
    def __init__(self, valor, parcelas):
        self.valor = valor 
        self.parcelas = parcelas  
        self.parcelas_pendentes = parcelas 
        self.valor_parcela = valor / parcelas 
    def pagar_parcela(self):
       
        if self.parcelas_pendentes > 0:
            self.parcelas_pendentes -= 1
            return self.valor_parcela
        return 0.0 

    def __str__(self):
        return f"Compra de R${self.valor:.2f} em {self.parcelas}x ({self.parcelas_pendentes} pendentes)."


class CartaoDeCredito:
    def __init__(self, proprietario, numero, limite_credito):
        self.proprietario = proprietario 
        self.numero = numero  
        self.limite_credito = limite_credito  
        self.compras = []  
    def saldo_disponivel(self):
        total_em_divida = sum(
            compra.valor_parcela * compra.parcelas_pendentes for compra in self.compras
        )
        return self.limite_credito - total_em_divida

    def comprar(self, valor, parcelas):
        if parcelas <= 0:
            print("O número de parcelas deve ser maior que 0.")
            return
        valor_parcela = valor / parcelas
        if valor_parcela * parcelas > self.saldo_disponivel():
            print("Compra negada: limite de crédito insuficiente.")
            return
        nova_compra = Cartao(valor, parcelas)
        self.compras.append(nova_compra)
        print(f"Compra aprovada: {nova_compra}")

    def gerar_fatura_mes(self):
        fatura = []
        for compra in self.compras[:]: 
            if compra.parcelas_pendentes > 0:
                fatura.append(compra.pagar_parcela())
            if compra.parcelas_pendentes == 0:
                self.compras.remove(compra)  
        return fatura

    def __str__(self):
        compras_detalhes = "\n".join(str(compra) for compra in self.compras)
        return (
            f"Cartão de Crédito - Proprietário: {self.proprietario}\n"
            f"Número: {self.numero}\n"
            f"Limite: R${self.limite_credito:.2f}\n"
            f"Saldo Disponível: R${self.saldo_disponivel():.2f}\n"
            f"Compras:\n{compras_detalhes if compras_detalhes else 'Nenhuma compra registrada.'}"
        )


cartao = CartaoDeCredito("João Silva", "1234-5678-9876-5432", 5000)

print(cartao)
print("\n--- Realizando compras ---")
cartao.comprar(1200, 6)  
cartao.comprar(300, 3)  
cartao.comprar(6000, 5)  
cartao.comprar(200, 0)  
print(cartao)

print("\n--- Gerando fatura do mês ---")
fatura = cartao.gerar_fatura_mes()
print("Fatura do mês: ", [f"R${parcela:.2f}" for parcela in fatura])
print(cartao)

print("\n--- Gerando segunda fatura ---")
fatura = cartao.gerar_fatura_mes()
print("Fatura do mês: ", [f"R${parcela:.2f}" for parcela in fatura])
print(cartao)
