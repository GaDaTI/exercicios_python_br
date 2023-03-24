"""
10- Faça um Programa que leia dois vetores com 10 elementos 
cada. Gere um terceiro vetor de 20 elementos, cujos valores 
deverão ser compostos pelos elementos intercalados dos dois 
outros vetores.
"""
lista_vetor_a = []
lista_vetor_b = []
lista = []

# Entrada de dados
for indice in range(10):
    vetor_a = int(input("Digite um numero: "))
    lista_vetor_a.append(vetor_a)

    vetor_b = input("Digite uma palavra: ")
    lista_vetor_b.append(vetor_b)

for indice in range(0, 10):
    lista.append(lista_vetor_a[indice])
    lista.append(lista_vetor_b[indice])

print(lista)
