"""
13 - Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
# Entrada de dados:
altura = float(input("Digite sua altura: "))

# Processamento de dados:
peso_ideal_homens =  72.7 * altura - 58
peso_ideal_mulheres = 62.1 * altura  - 44.7

# Saida de dados:
print(f"""Par uma pessoa do sexo masculino com altura de 
{altura} o é = '{peso_ideal_homens} kg'""")
print(f"""Par uma pessoa do sexo feminino com altura de {altura} 
o é = '{peso_ideal_mulheres} kg'""")
