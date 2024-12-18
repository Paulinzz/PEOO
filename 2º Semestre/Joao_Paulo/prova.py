# Crie uma classe Acai que representa uma tigela de açaí. A tigela deve ter os seguintes atributos:
#Tamanho: "P", "M" ou "G".
#Base: "Açaí Puro", "Açaí com Guaraná", etc.
#Crie 2 instâncias de tigelas diferentes, de acordo com a tabela abaixo:

#  Implemente um método exibir_detalhes() que imprime a seguinte mensagem:
# "Tigela de [base], Tamanho [tamanho]".
# Execute o método exibir_detalhes() em cada uma delas.


# Questão 1:

class Acai:
    def __init__(self, tamanho: str, base: str):
        self.base = base
        self.tamanho = tamanho


    def exibir_detalhes(self):
        print(f"Tigela de {self.tamanho}, Tamanho {self.base}")

açaí = Acai("Açaí Puro", "M")
açaí.exibir_detalhes()

açaí2 = Acai("Açaí com Guaraná", "G")
açaí2.exibir_detalhes()

# Questão 2:

# (5 de 20pts) Crie uma classe Ingrediente que 
# representa um ingrediente de açaí.
#O ingrediente deve ter os seguintes atributos:
#● Nome: Nome do ingrediente (ex: "Granola", "Morango", "Calda de
#Chocolate").
#● Preço: Preço em reais.
#Altere a classe Acai para conter uma lista de ingredientes:
#● Tamanho: Tamanho da tigela.
#● Base: Tipo de base do açaí.
#● Ingredientes: Uma lista de objetos da classe Ingrediente.
#Implemente o método adicionar_ingrediente(ingrediente:
#Ingrediente) que adiciona um ingrediente à tigela. Adicione ingredientes às
#tigelas criadas na questão anterior de acordo com as tabelas a seguir:

class Ingrediente:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def exibir_detalhes(self):
        print(f"Ingrediente: {self.nome}, Preço: {self.preco} R$")

class Acai:
    def __init__(self, tamanho: str, base: str):
        self.base = base
        self.tamanho = tamanho
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def exibir_detalhes(self):
        print(f"Tigela de {self.tamanho}, Tamanho {self.base}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            ingrediente.exibir_detalhes()

açaí = Acai("Açaí Puro", "M")
açaí.adicionar_ingrediente(Ingrediente("Granola", 2.0))
açaí.adicionar_ingrediente(Ingrediente("Morango", 3.0))
açaí.adicionar_ingrediente(Ingrediente("Calda de Chocolate", 1.5))
print("-"*50)
açaí.exibir_detalhes()

print("-"*50)

açaí2 = Acai("Açaí com Guaraná", "G")
açaí2.adicionar_ingrediente(Ingrediente("Granola", 2.0))
açaí2.adicionar_ingrediente(Ingrediente("Morango", 3.0))
açaí2.adicionar_ingrediente(Ingrediente("Calda de Chocolate", 1.5))
print("-"*50)
açaí2.exibir_detalhes()

# Questão 3

#Represente pedidos como classes. Pedidos de tigelas podem ser para consumo
#local (na loja) ou entregues em um endereço.
#  Pedidos para consumo local possuem
#um número de mesa. Pedidos para entrega possuem um endereço.
#(10 de 20pts) Represente os diferentes tipos de pedidos usando classes 
# distintas.
#Use seus conhecimentos de herança para evitar a repetição de código.

#  Implemente um método entregar() que imprime:
#● "Servido na mesa [mesa]", se for um pedido para consumo local.
#● "Enviado para o endereço [endereco]", se for um pedido para
#entrega.

class Pedido:
    def __init__(self, mesa: int, endereco: str):
        self.mesa = mesa
        self.endereco = endereco

    def exibir_detalhes(self):
        if self.mesa is not None:
            print(f"Servido na mesa {self.mesa}")
        else:
            print(f"Enviado para o endereço {self.endereco}")

class PedidoLocal(Pedido):
    def __init__(self, mesa: int):
        super().__init__(mesa, None)

class PedidoEntrega(Pedido):
    def __init__(self, endereco: str):
        super().__init__(None, endereco)

pedido_local = PedidoLocal(1)
pedido_local.exibir_detalhes()

print("-"*50)

pedido_entrega = PedidoEntrega("Rua dos Bobos, 0")
pedido_entrega.exibir_detalhes()

print("-"*50)

pedido_local = PedidoLocal(2)
pedido_local.exibir_detalhes()

print("-"*50)
