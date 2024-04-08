def trocar(a,b):
    c = a
    a = b
    b = c     
    print(f"os valores antes de A = {c} e B = {a} agora são respcetivamente: " "A = ", a, "B = ", b )
    return trocar

trocar(9,1)
