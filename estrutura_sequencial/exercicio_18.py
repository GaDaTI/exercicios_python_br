"""
8 - Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total do 
seu salário no referido mês.
"""
# Entrada de dados:
horas_trabalhadas = float(input("Horas trabalhadas: "))
valor_da_hora_trabalhada = float(input("Valor da hora trabalhada: "))

# Processamento de dados:
salario = horas_trabalhadas * valor_da_hora_trabalhada

# Saida de dados:
print(f"O valor do salario é de {salario}.")