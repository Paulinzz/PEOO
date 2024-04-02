def trocar(i,j,valores):
    valores[i], valores[j] = valores[j],valores[i]
    return trocar

lista = [i for i in range(1, 9)]
print(f"lista atualizada: {lista}")

indice_j = int(input("Digite o índice J: "))
indice_i = int(input("Digite o índice i: "))

trocar(indice_i,indice_j,lista)
print(f"lista após as trocas: {lista}")

