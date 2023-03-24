"""
14 - oão Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido
 pelo regulamento de pesca do estado de São Paulo (50 quilos) deve 
 pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
  você faça um programa que leia a variável peso (peso de peixes) e
   calcule o excesso. Gravar na variável excesso a quantidade de 
   quilos além do limite e na variável multa o valor da multa que 
   João deverá pagar. Imprima os dados do programa com as mensagens 
   adequadas.
"""
# Entrada de dados:
import math
peso = float(input("Quantos quilos pesa o peixe: "))

# Processamento de dados: 
peso_excedente = 50 - peso
valor_pago = abs(peso_excedente) * 4


# Saida de dados:
print(f"O valor a ser pago é de = '{valor_pago}'")