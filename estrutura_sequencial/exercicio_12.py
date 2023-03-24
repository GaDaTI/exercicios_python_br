"""
15 - Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre o 
total do seu salário no referido mês, sabendo-se que são 
descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela 
abaixo:
"""
# Entrada de dados:
print()
valor_da_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Dige o numero de horas trabalhadas: "))

# Processamento de dados: Calcule e mostre o total do seu salário no referido mês
salario_bruto = valor_da_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
desconto_total = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - desconto_total

# Saida de dados:
print()
print(f"O salario bruto é {salario_bruto} reais")
print(f"O desconto de imposto de renda é {desconto_ir} reais")
print(f"O desconto inss é {desconto_inss} reais")
print(f"O desconto sindical é {desconto_sindicato} reais")
print(f"O total de desconto é de {desconto_total} reais")
print(f"O salario liquido é {salario_liquido} reais")
