"""
5 - Faça um Programa que leia 20 números inteiros e 
armazene-os num vetor. Armazene os números pares no 
vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""
# Entrada de dados
lista = lista_par = lista_impar = []
for _ in range(20):
    numero_inteiros = int(input("Digite um numero: "))
    if numero_inteiros % 2 == 0:
        lista_par.append(numero_inteiros)
    else:
        lista_impar.append(numero_inteiros)

print(lista)
print(lista_par)
print(lista_impar)