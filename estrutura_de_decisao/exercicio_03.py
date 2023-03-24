"""
6 - Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
# Entrada de dados:
primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
terceiro_numero = float(input("Digite o terceiro numero: "))

# Processamento de dados:
if segundo_numero > primeiro_numero < terceiro_numero:
    menor_numero = primeiro_numero

    if segundo_numero < terceiro_numero:
         maior_numero = terceiro_numero
    else:
        maior_numero = segundo_numero

elif primeiro_numero > segundo_numero < terceiro_numero:
    menor_numero = segundo_numero

    if primeiro_numero > terceiro_numero:
         maior_numero = primeiro_numero
    else:
        maior_numero = terceiro_numero

else:
    menor_numero = terceiro_numero

    if primeiro_numero > segundo_numero:
         maior_numero = primeiro_numero
    else:
        maior_numero = segundo_numero

# Saida de dados:
print(f"Entre os numeros '{primeiro_numero}','{segundo_numero}' e  '{terceiro_numero}' o maior deles é o numero '{maior_numero}' e o menor deles é o numero '{menor_numero}'.")