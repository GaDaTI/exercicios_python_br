"""
13 - Faça um Programa que leia um número e exiba o dia correspondente
 da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor
  deve aparecer valor inválido.
"""
# Entrada de dados:
indice = int(input("Digite um numero referente ao dia da semana: "))

dia_da_semana = ['1 - Domingo','2 - Segunda', '3 - Terça', '4 - Quarta', '5 - Quinta', '6 - Sexta', '7 - Sabado']

if indice != 0 and indice in range(len(dia_da_semana)+1):
    print(f"Você digitou {dia_da_semana[indice-1]}. ")   

else:
    print("Valor inválido !")
    