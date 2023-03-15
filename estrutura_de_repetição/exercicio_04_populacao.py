"""
4 - Supondo que a população de um país A seja da ordem 
de 80000 habitantes com uma taxa anual de crescimento 
de 3% e que a população de B seja 200000 habitantes com 
uma taxa de crescimento de 1.5%. Faça um programa que 
calcule e escreva o número de anos necessários para que 
a população do país A ultrapasse ou iguale a população 
do país B, mantidas as taxas de crescimento.
"""
# Entrada de dados
populacao_a = 8000
populacao_b = 200000
valor = True
contador = aumento = 0

# Processamento de dados:
while valor:
    ano_inicio = 2023

    aumento_de_a = populacao_a * 0.03
    populacao_a += aumento_de_a

    aumento_de_b = populacao_b * 0.015
    populacao_b += aumento_de_b

    if populacao_a <= populacao_b:
        contador += 1
    else:
        ano_final = ano_inicio + contador
        print(f"População 'A': {populacao_a:.2f}")
        print(f"População 'B': {populacao_b:.2f}")
        print(f"Ano que ultrapassa : {ano_final}")
        valor = False
    
