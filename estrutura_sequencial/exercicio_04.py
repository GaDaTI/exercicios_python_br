"""
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
# Entrada de dados:
import math
tamanho_da_area = float(input("Digite o tamanho da area a ser pintada em metros quadrados: "))

# Processamento de dados:
quantidade_de_litros_de_tinta = tamanho_da_area / 6

latas_de_tinta = quantidade_de_litros_de_tinta // 18
quantidade_de_latas_de_tinta = quantidade_de_litros_de_tinta / 18

sobra_da_tinta = quantidade_de_litros_de_tinta % 18

completar_com_galoes = sobra_da_tinta / 3.6
completar_com_galoes = math.ceil(completar_com_galoes)

quantidade_de_galoes_de_tinta = quantidade_de_litros_de_tinta / 3.6

apenas_de_latas_de_tinta = math.ceil(quantidade_de_latas_de_tinta)
apenas_de_galoes_de_tinta = math.ceil(quantidade_de_galoes_de_tinta)

custo_com_latas_de_tinta = quantidade_de_latas_de_tinta * 80.00
custo_com_galoes_de_tinta = quantidade_de_galoes_de_tinta * 25.00
custo_completar_galoes = completar_com_galoes * 25
custo_total = custo_com_latas_de_tinta + custo_completar_galoes

# Saida de dados:
print()
print()
print(f"Comprar apenas latas de 18 litros:   ")
print(f"Quantidade de latas de 18 litros {apenas_de_latas_de_tinta}.")
print(f"Custo com {apenas_de_latas_de_tinta} latas de 18 litros é de {custo_com_latas_de_tinta} reais.")
print()
print()
print(f"Comprar apenas galões de 3,6 litros ")
print(f"Quantidade de galões de 3,6 litros {apenas_de_galoes_de_tinta}.")
print(f"Custo com {apenas_de_galoes_de_tinta} latas de 18 litros é de {custo_com_galoes_de_tinta} reais.")
print()
print()
print(f"Comprar latas de tintas de 18 litros  e galões de 3,6 litros ")
print(f"Quantidade de galões de 3,6 litros {completar_com_galoes}.")
print(f"O custo com galões de 3,6 litros {custo_completar_galoes} reais.")
print(f"Quantidade de latas de 18 litros {latas_de_tinta}.")
print(f"O custo com latas de 18 litros {custo_com_latas_de_tinta} reais.")
print(f"Custo total com latas e galões é de {custo_total} reais.")
