# Represente uma pessoa como uma classe.
#A pessoa deve ter nome e idade.
#Crie 3 pessoas diferentes.
#Implemente um método fazer_saudacao, que imprime uma mensagem como "Olá, eu sou Fulano e tenho X anos.". 
# Chame esse método nas 3 pessoas criadas.
#Implemente um método envelhecer, que recebe uma quantidade de anos e soma à idade da pessoa. 
# Após executar o método, a idade daquela pessoa deve ter sido alterada. Chame esse método em uma das pessoas e imprima a idade dela antes e depois de envelhecer.

class Pesosa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def saudação(self):
        print(f"Ola, eu sou {self.nome} e tenho {self.idade} anos")
    
    def envelhecer(self):
        self.idade += 1
        print(f"Você agora tem {self.idade} anos")

jp = Pesosa("jp", 22)

jp.saudação()
jp.envelhecer()

# cria mais 2 pessoas ...                                                                       