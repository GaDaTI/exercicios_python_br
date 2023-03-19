"""
1- Faça um programa para imprimir:
para um n informado pelo usuário. Use uma função que receba 
um valor n inteiro e imprima até a n-ésima linha.
"""
contador = 0
lista = []
# Entrada de dados
def enesima(valor:int) -> int: 
    global contador   
    
    for index in range(valor):        
        for _ in range(index):
            contador += 1
            lista.append(contador)
            
    return lista

print(enesima(4))      

            
        