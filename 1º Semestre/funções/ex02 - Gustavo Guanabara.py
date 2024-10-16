def escreva(palavra):
    print((len(palavra)+4)*"=")
    print(palavra.center(len(palavra)+4))
    print((len(palavra)+4)*"=")
    return escreva

print(escreva("palavra"))