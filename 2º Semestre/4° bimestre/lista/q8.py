from abc import ABC, abstractmethod

class Calculadora():
    @staticmethod
    def soma(a,b):
        return a + b
    
    @classmethod
    def subtrair (cls,a,b):
        return a - b

print(Calculadora.soma(10,5))
print(Calculadora.subtrair(10,5))  