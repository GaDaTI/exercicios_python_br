"""
9 - Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
# Entrada de dados:
farenheit = float(input("Digite o valor da temperatura em Farenheit: "))

# Processamento de dados:
valor_em_graus_celsius = 5 * ((farenheit-32) / 9)

# Saida de dados:
print(f"O valor de {farenheit} corresponde ao valor de {valor_em_graus_celsius} graus celsius.")