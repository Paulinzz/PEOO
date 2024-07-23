
def contar(n):
    if n >= 0:
        print(n)
        contar(n-1)
contar(1)