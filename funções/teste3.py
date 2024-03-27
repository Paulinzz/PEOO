def encontrar(n,lista):
    for i in range(len(lista)):
        if lista[i] == n:
            return i 
    
    return -1 

lista = [4,5,6]
pos = encontrar(4,lista)
print(pos)