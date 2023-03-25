"""
1- Faça um programa para imprimir:
para um n informado pelo usuário. Use uma função que receba 
um valor n inteiro e imprima até a n-ésima linha.
"""
# Entrada de dados
def enesima(valor:int) -> int:
    lista_enesima = []
     
    for index in range(valor):
        i = index
        index += 1 
        numero = 0
        lista=[] 
              
        for numero in range(index):
            numero += 1
            lista.append(numero)
        lista_enesima.append(lista)
           
    return lista_enesima

resultado = enesima(int(input("Digite um valor: ")))


for item in resultado:
    print(item)
        