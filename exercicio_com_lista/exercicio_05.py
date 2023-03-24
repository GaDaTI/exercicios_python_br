"""
4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.
"""

vetor_de_caracteres = ['a', 'L', 'j', 'P', 'A', 'e']
lista = ['a', 'e', 'i', 'o', 'u']

for item in vetor_de_caracteres:
    item.lower()
    if item not in lista:
        print(item,end=", ")



