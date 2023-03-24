"""
07 -Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a 
multiplicação e os número
"""
# Entrada de dados 
lista = []
soma_dos_numeros = 0
multiplicacao_numeros = 1

for _ in range(1, 6):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

for item in lista:
    soma_dos_numeros += int(item)
    multiplicacao_numeros *= int(item)

print()
print(f"A soma dos numeros {lista} é igual a {soma_dos_numeros}")
print(f"A smutiplicação dos numeros {lista} é igual a {multiplicacao_numeros}")
