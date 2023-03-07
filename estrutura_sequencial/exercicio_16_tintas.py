"""
16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
 em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
 de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
  a serem compradas e o preço total.
"""
# Entrada de dados:
import math
tamanho_da_area = float(input("Digite o tamanho da area a ser pintada em metros quadrados: "))

# Processamento de dados:
quantidade_de_litros_de_tinta = tamanho_da_area / 3
quantidade_de_latas_de_tinta = quantidade_de_litros_de_tinta / 18
quantidade_de_latas_de_tinta = math.ceil(quantidade_de_latas_de_tinta)
custo_com_tinta = quantidade_de_latas_de_tinta * 80.00

# Saida de dados:
print(f"Serão compradas a quantidade de {quantidade_de_latas_de_tinta} latas de tinta. ")
print(f"O preço total {custo_com_tinta} reais. ")


