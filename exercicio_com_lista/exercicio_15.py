"""
15- Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for
 informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
lista = [ ]
while True:
    valor = int(input("Digite um valor: "))

    if valor == 1:
        break
    else:
        lista.append(valor)

# Mostre a quantidade de valores que foram lidos;
quantidade_de_valores_lidos = len(lista)
print(f"Quantidade de valores que foram lidos: {quantidade_de_valores_lidos}")

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
for numero in lista:
    print(f"{numero}", end=', ')

print()
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print()
lista.reverse()
for numero in lista:
    print(f"{numero}")

# Calcule e mostre a soma dos valores;
print()
soma_da_lista = sum(lista)
print(soma_da_lista)
print()
# Calcule e mostre a média dos valores;
print()
media = soma_da_lista / ( len(lista) + 1)
print(f"{media:.2f}")
print()
# Calcule e mostre a quantidade de valores acima da média calculada;
print()
for numero in lista:
    if numero > media:
        print(numero)
print()
# Calcule e mostre a quantidade de valores abaixo de sete;
print()
for numero in lista:
    if numero < 7:
        print(numero)
print()
# Encerre o programa com uma mensagem;
print()
print("Programa encerrado !")
print()