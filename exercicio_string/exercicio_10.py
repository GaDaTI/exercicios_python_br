"""
10 - Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e
imprima-o na tela por extenso.
"""
numero = input(int("Digite um numero: "))

lista_unidade = [ 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
lista_10_a_19 = ['dez','onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
lista_20_a_90 = ['vinte', 'trinta','quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta','noventa']

if numero < 10:
    print(lista_unidade[numero])
elif numero < 20:
    indice = numero - 10
    print(lista_10_a_19[indice])
else:
    indice = ( numero / / 10 ) - 2
    resto = numero % 10
    decimal = resto * 10

    if decimal  != 0:
        print(f"{lista_20_a_90[indice]} {lista_unidade[]}")
