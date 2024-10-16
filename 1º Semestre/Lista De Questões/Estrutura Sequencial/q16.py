# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
#tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Digite em metros quadrados a área a ser pintada: "))
litros = area / 6

situações = input("Deseja Galões ou Latas? Deseja mistura as duas? Se caso deseja misturar ").lower()

if situações[0] == "l":
    quantidades = -(-litros // 18)
    preço = quantidades * 80
    print(f"Com apenas o uso de latas o preço foi de R${preço}")
elif situações[0] == "g":
    quantidades = -(-litros // 3.6)
    preço = quantidades * 25
    print(f"Com apenas o uso de galões o preço foi de R${preço:.2f}")
else:
    quantidades = -(-litros // 18)
    resto = quantidades - litros
    preço = -(quantidades * 80 +(resto * 25)) 
    print(f"Com o a mistura da latas e galões o preço foi de R${preço:.2f}")
