"""
11 - Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
# Entarda de dados:
primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite um valor: "))
terceiro_valor = float(input("Digite um valor: "))

# Processamento de dados:
metade_do_segundo = segundo_valor / 2
dobro_do_primeiro = primeiro_valor * 2 
produto  = dobro_do_primeiro * metade_do_segundo
triplo_do_primeiro_valor = primeiro_valor * 3
soma = triplo_do_primeiro_valor + terceiro_valor
cubo = terceiro_valor ** 3

# Saida de dados:
print(f"O produto do dobro do primeiro = '{dobro_do_primeiro}' com metade do segundo = '{metade_do_segundo}' é igual a {produto}.")
print(f"A soma do triplo do primeiro = '{triplo_do_primeiro_valor}' com o terceiro = '{terceiro_valor}' é igual a '{soma}'.")
print(f"O terceiro = '{terceiro_valor}' elevado ao cubo é igual a '{cubo}'.")


