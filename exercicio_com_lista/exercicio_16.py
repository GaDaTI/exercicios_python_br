"""
16- Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas
brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando
um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
"""
lista = [ ]
for _ in range(5):
    vlr_venda_bruta = float(input("Digite o valor da venda: "))
    lista.append(vlr_venda_bruta)

contador_faixa_1 = 0
contador_faixa_2 = 0
contador_faixa_3 = 0
contador_faixa_4 = 0
contador_faixa_5 = 0
contador_faixa_6 = 0
contador_faixa_7 = 0
contador_faixa_8 = 0
contador_faixa_9 = 0

for valor in lista:
    comissao = int(( 0.09 * valor ) + 200)
    if 200 < comissao  < 299:
        contador_faixa_1 += 1
    elif comissao < 399:
        contador_faixa_2 += 1
    elif comissao < 499:
        contador_faixa_3 += 1
    elif comissao < 599:
        contador_faixa_4 += 1
    elif comissao < 699:
        contador_faixa_5 += 1
    elif comissao < 799:
        contador_faixa_6 += 1
    elif comissao < 899:
        contador_faixa_7 += 1
    elif comissao < 999:
        contador_faixa_8 += 1
    else:
        contador_faixa_9 += 1

print(f"{contador_faixa_1 } vendedores receberam salários nos intervalos de $200 - $299:")
print(f"{contador_faixa_2 } vendedores receberam salários nos intervalos de $300 - $399:")
print(f"{contador_faixa_3 } vendedores receberam salários nos intervalos de $400 - $499")
print(f"{contador_faixa_4 } vendedores receberam salários nos intervalos de $500 - $599")
print(f"{contador_faixa_5 } vendedores receberam salários nos intervalos de $600 - $699")
print(f"{contador_faixa_6} vendedores receberam salários nos intervalos de $700 - $799:")
print(f"{contador_faixa_7} vendedores receberam salários nos intervalos de $800 - $899")
print(f"{contador_faixa_8 } vendedores receberam salários nos intervalos de $900 - $999:")
print(f"{contador_faixa_9 } vendedores receberam salários  de $1000 em diante:")







