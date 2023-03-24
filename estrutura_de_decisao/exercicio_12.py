"""
3 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
# Entrada de dados:
valor = float(input("Digite um valor numerico: "))

# Processamento de dados:
if valor < 0:
    resposta = f"O numero {valor} é negativo!"
else:
    resposta = f"O numero {valor} é positivo!"

# Saida de dados:
print(resposta)
