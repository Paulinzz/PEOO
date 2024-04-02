string = True

def validar(string,nummin,nummax):
    tamanho = len(string)
    return nummin <=tamanho <= nummax

string = input("Digite a palavra")
minimo = int(input("Digite a quantidade minima"))
maximo =  int(input("Digite a quantidade maxima:"))

resultado = (validar(string,minimo,maximo))

print(resultado)