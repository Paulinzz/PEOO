#1 - Crie uma classe abstrata chamada FormaGeometrica que tenha:
#Um método abstrato area() que deve retornar a área da forma.
#Um método abstrato perimetro() que deve retornar o perímetro da forma.

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def descricao(self):
        pass

#2 - Baseando-se na classe abstrata FormaGeometrica, crie duas classes concretas:
#Retangulo, com os atributos largura e altura.
#Circulo, com o atributo raio.
#Cada classe deve implementar os métodos area e perimetro.

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def descricao(self):
        return f'Sou um retângulo de largura {self.largura} e altura {self.altura}'

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio**2

    def perimetro(self):
        return 2 * 3.14 * self.raio
    
    def descricao(self):
        return f'Sou um círculo de raio {self.raio}'

#3 - Crie uma função chamada descrever_forma que:
#Aceita como argumento um objeto do tipo FormaGeometrica.
#Retorna a área e o perímetro da forma.
#Teste a função com instâncias das classes Retangulo e Circulo.

def descrever_forma(forma: FormaGeometrica):
    return forma.area(), forma.perimetro()

#4 - Adicione um método abstrato chamado descricao() na classe FormaGeometrica, que retorna
#uma string com a descrição da forma. Implemente o método nas classes concretas:

# No Retangulo, o método deve retornar algo como: "Sou um retângulo de largura X e altura Y."
#No Circulo, o método deve retornar: "Sou um círculo de raio R."

# 5 - Crie uma lista de objetos do tipo FormaGeometrica contendo instâncias de Retangulo e
#Circulo com diferentes dimensões. Em seguida, itere sobre a lista, chamando os métodos
#descricao, area e perimetro de cada objeto, e exiba os resultados no console.

objetos = [Circulo(2), Retangulo(4,5)]

for objeto in objetos:
    print(objeto.descricao())
    print(objeto.area())
    print(objeto.perimetro())



