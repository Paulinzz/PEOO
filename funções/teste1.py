def eh_par(n):
    return n % 2 == 0

def par_ou_impar(n):
    if eh_par(n):
        return "par"
    else:
        return "ímpar"
    
quantas = int(input("Deseja quantas vezes?"))

for i in range(0, quantas):
    print(par_ou_impar(int(input("Digite o número para ver se é par: "))))
