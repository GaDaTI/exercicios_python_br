"""
13- Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso:
1 – Janeiro, 2 – Fevereiro, . . . ).
"""
lista_meses_do_ano  = [ 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
lista_media_temperatura = [ ]
for  indice in range(len(lista_meses_do_ano)):
    temperatura = float(input(f"Digite a  temperatura media do mês de  {lista_meses_do_ano[indice]}: "))
    lista_media_temperatura.append(temperatura)

soma_das_temperaturas = sum(lista_media_temperatura)
media_temperatura_anual = soma_das_temperaturas / 12
print(f"Média da temperatura anual  é de {media_temperatura_anual:.2f} graus")
for indice, temperatura in enumerate(lista_media_temperatura):
    if  temperatura > media_temperatura_anual:
        print(f"{lista_meses_do_ano[indice]}")