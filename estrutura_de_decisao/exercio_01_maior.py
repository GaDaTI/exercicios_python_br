"""
1 - Faça um Programa que peça dois números e imprima o maior deles.
"""
# Entrada de dados:
primeiro_numero = float(input("Digite um numero: "))
segundo_numero = float(input("Digite outro numero: "))

# Processamento de dados:
if primeiro_numero > segundo_numero:
    maior_numero = primeiro_numero
else:
    maior_numero = segundo_numero

# Saida de dados:
print(f"Entre o numero {primeiro_numero} e o numero {segundo_numero} o maior deles é o numero {maior_numero}")
