# Implemente um cartão de crédito.
#O cartão tem um proprietário, um número identificador, um limite de crédito e uma lista de compras.
#Implemente o sistema de compras. O cartão deve guardar uma lista de compras e exibir o limite disponível atualmente. 
# Implemente também um método comprar, que verifica se há limite disponível e adiciona a compra à lista do cartão.

# Implemente o sistema de compras. 
# O cartão deve guardar uma lista de compras e exibir 
# o limite disponível atualmente. 
# Implemente também um método comprar, 
# que verifica se há limite disponível e 
# adiciona a compra à lista do cartão.
class Cartao:
    def __init__(self, proprietario: str, id: int, 
    limite: float, compras: list[dict] = []):
        self.propietario = proprietario
        self.id = id
        self.limite = limite  
        self.compras = compras

    def limite_disponivel(self):
        disponivel = self.limite
        for c in self.compras:
            disponivel -= c['valor']
        return disponivel

    def comprar(self, compra: dict):
        if self.limite_disponivel() >= compra['valor']:
            self.compras += [compra]
            print('Compra Realizada com Sucesso!')
        else:
            print(f'Erro, compra R${compra["valor"]} acima do limite disponível R${self.limite_disponivel()}!')

cartao1 = Cartao('Bruno', 123, 2000)
print('Limite do cartão:', cartao1.limite)
print('Limite disponível:', cartao1.limite_disponivel())
print('Compras:', cartao1.compras)

cartao1.comprar({'desc': 'tênis', 'valor': 200})
print('Limite do cartão:', cartao1.limite)
print('Limite disponível:', cartao1.limite_disponivel())
print('Compras:', cartao1.compras)

cartao1.comprar({'desc': 'PS5', 'valor': 5000})
print('Limite do cartão:', cartao1.limite)
print('Limite disponível:', cartao1.limite_disponivel())
print('Compras:', cartao1.compras)

