#n = int(input("Digite um número"))

def fatorial(n):
    fat = 1 
    for i in range(2, n+1):
        fat *= i
    return fat

print(fatorial(n = int(input("Digite um número: "))))