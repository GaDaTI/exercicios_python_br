"""
09 - Faça um Programa que leia um vetor A com 10 números 
inteiros, calcule e mostre a soma dos quadrados dos elementos 
do vetor.
"""
# Entrada de dados
#vetor = list(range(23, 34))
lista_soma = []
lista = []
quadrado_numero = 0
# Processamento de dados
for index in range(1, 11):
    numero = int(input(f"Digite o {index}º numero:"))
    quadrado_numero = numero ** 2
    lista.append(quadrado_numero)
    quadrado_numero = 0

# Saida de dados
print()
print(lista)
print()
soma_do_quadrado_dos_numeros = sum(lista)
print(soma_do_quadrado_dos_numeros)
    
