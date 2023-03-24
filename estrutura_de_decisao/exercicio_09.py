"""
6 - Faça um Programa que leia três números e mostre o maior deles.
"""
# Entrada de dados:
primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
terceiro_numero = float(input("Digite o terceiro numero: "))

# Processamento de dados:
if segundo_numero < primeiro_numero > terceiro_numero:
    maior_numero = primeiro_numero
elif segundo_numero > terceiro_numero:
    maior_numero = segundo_numero
else:
    maior_numero = terceiro_numero

# Saida de dados:
print(f"Entre os numeros '{primeiro_numero}','{segundo_numero}' e  '{terceiro_numero}' o maior deles é o numero {maior_numero}")
