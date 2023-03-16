"""
3 - Faça um Programa que leia 4 notas, mostre as notas 
e a média na tela.
"""
# Entrada de dados
lista = []
for _ in range(4):
    nota = float(input("Digite o valor da nota: "))
    lista.append(nota)

# Processamento de dados
soma_das_notas = sum(lista)
media = soma_das_notas / 4

# Saida de dados
print()
contador=0
for item in lista:
    contador += 1
    print(f"Nota {contador}: {item}")

print(f"A sua media foi {media:.2f}")