def eh_par(n):
    return n % 2 == 0

quantas = int(input("Deseja quantas vezes?"))

for i in range(0, quantas):
    print(eh_par(int(input("Digite o número para ver se é par: "))))
