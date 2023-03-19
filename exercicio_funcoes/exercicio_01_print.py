"""
1- Faça um programa para imprimir:
para um n informado pelo usuário. Use uma função que receba 
um valor n inteiro e imprima até a n-ésima linha.
"""
contador = 0

lista_enesima = []
# Entrada de dados
def enesima(valor:int) -> int:   
    global contador

    for index in range(valor):
        lista = []
        index += 1
        for _ in range(index):
            contador += 1
            lista.append(contador)
        
        lista_enesima.append(lista)
        contador=0   
    
        
    
    return  lista_enesima
        

print(enesima(4))      

            
        