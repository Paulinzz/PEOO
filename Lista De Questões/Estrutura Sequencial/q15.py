# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Digite em metros quadrados a área a ser pintada: "))

litros = area / 3

latas_necessarias = -(-litros // 18)  

preco = latas_necessarias * 80

print(f"Quantidade de latas de tinta a serem compradas: {int(latas_necessarias)}")
print(f"Preço total: R$ {preco:.2f}")
