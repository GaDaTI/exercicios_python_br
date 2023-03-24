"""
6 - Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a decisão 
é sempre pelo mais barato.
"""
# Entrada de dados:
primeiro_produto = float(input("Digite o primeiro produto: "))
segundo_produto = float(input("Digite o segundo produto: "))
terceiro_produto = float(input("Digite o terceiro produto: "))

# Processamento de dados:
if segundo_produto > primeiro_produto < terceiro_produto:
    produto_mais_barato = primeiro_produto
elif primeiro_produto > segundo_produto < terceiro_produto:
    produto_mais_barato = segundo_produto
else:
    produto_mais_barato = terceiro_produto
    
# Saida de dados:
print(f"Entre os valores dos produtos : '{primeiro_produto}','{segundo_produto}' e  '{terceiro_produto}' o menor valor dentre os valores dos produtos é '{produto_mais_barato}'.")
