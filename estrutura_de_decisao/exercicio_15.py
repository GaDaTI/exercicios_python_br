"""
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
# Entrada de dados:
primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
terceiro_numero = float(input("Digite o terceiro numero: "))

# Processamento de dados:
if segundo_numero < primeiro_numero > terceiro_numero:    
    maior_numero = primeiro_numero

    if segundo_numero > terceiro_numero:
        meio_numero = segundo_numero
        menor_numero = terceiro_numero
    else:
        meio_numero = terceiro_numero
        menor_numero = segundo_numero

elif primeiro_numero < segundo_numero > terceiro_numero:    
    maior_numero = segundo_numero

    if primeiro_numero > terceiro_numero:
        meio_numero = primeiro_numero
        menor_numero = terceiro_numero
    else:
        meio_numero = terceiro_numero
        menor_numero = primeiro_numero

else:
    maior_numero = terceiro_numero

    if primeiro_numero > segundo_numero:
        meio_numero = primeiro_numero
        menor_numero = segundo_numero
    else:
        meio_numero = segundo_numero
        menor_numero = primeiro_numero

# Saida de dados:
print(f"{maior_numero} maior numero ; {meio_numero} numero do meio ; {menor_numero} menor numero")
