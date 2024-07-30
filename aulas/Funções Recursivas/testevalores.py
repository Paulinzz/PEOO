def imprimir_linha(caractere, comprimento=60):
   print(caractere * comprimento)


# Para chamar a função, basta informar o caractere
#imprimir_linha('=')


# Mas também é possível informar o comprimento
#imprimir_linha('=', 10)

def somar(a, b):
   return a + b


def subtrair(a, b):
   return a - b

def multiplicar(a,b):
   return a * b

def divisão(a,b):
   return a / b 

def calcular(a, b, funcao):
   return funcao(a, b)



print(calcular(2,2,multiplicar))
print(calcular(1, 2, somar))
print(calcular(5, 3, subtrair))