# Faça uma classe abstrata criptografia e defina os métodos abstratos. Faça uma classe concreta que implemente a cifra de Atbash.
#A cifra de Atbash é um algoritmo que permite codificar e decodificar palavras.

#A é um tipo simples de cifra de substituição monoalfabética onde o alfabeto é invertido. Ou seja, a primeira letra do alfabeto é trocada pela última, a segunda pela penúltima e assim por diante.
#A substituição segue a seguinte regra para o alfabeto latino (A-Z):
#A ↔ Z
#B ↔ Y
#C ↔ X
#D ↔ W
#...
#M ↔ N
#Ou seja, cada letra do texto original é substituída por sua correspondente no alfabeto invertido.
#Vamos cifrar a palavra :Converter as letras para o alfabeto invertido:
#I → R
#F → U
#R → I
#N → M
#Resultado cifrado: (coincidência engraçada! 😆)

from abc import ABC, abstractmethod

class Criptografia(ABC):
    
    @abstractmethod
    def cifrar(self, texto: str):
        pass
    
    @abstractmethod
    def decifrar(self, texto: str):
        pass

class Atbash(Criptografia):
    
    def __init__(self):
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alfabeto_invertido = self.alfabeto[::-1]
    
    def cifrar(self, texto: str):
        texto_cifrado = []
        for caract in texto.upper():
            if caract in self.alfabeto:
                index = self.alfabeto.index(caract)
                texto_cifrado.append(self.alfabeto_invertido[index])
            else:
                texto_cifrado.append(caract)  
        return ''.join(texto_cifrado)
    
    def decifrar(self, texto: str):
        return self.cifrar(texto)

atbash = Atbash()

texto_original = "IFRN"
texto_cifrado = atbash.cifrar(texto_original)
print(f"Texto original: {texto_original}")
print(f"Texto codificado: {texto_cifrado}")

texto_decifrado = atbash.decifrar(texto_cifrado)
print(f"Texto decodificado: {texto_decifrado}")
