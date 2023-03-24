"""
12 -Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do 
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que 
o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao Salário
 Bruto menos os descontos. O programa deverá pedir ao usuário o 
 valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
print()
# Entrada de dados: valor da sua hora e a quantidade de horas trabalhadas no mês
valor_da_hora = float(input("  Digite o valor da hora de trabalho: "))
numero_de_horas_trabalhadas = float(input("  Digite o numero das horas trabalhadas: "))
print()
# Processamento de dados: 
salario_bruto = valor_da_hora * numero_de_horas_trabalhadas

desconto_fgts = 0.11
valor_desconto_fgts = salario_bruto * desconto_fgts

desconto_sindical = 0.03 
valor_desconto_sindical = salario_bruto * desconto_sindical

if salario_bruto <= 900:
    """
    Salário Bruto até 900 (inclusive) - isento
    """
    desconto_ir = 0
    desconto_ir_str = ' 0%'
    valor_desconto_ir = salario_bruto * desconto_ir

elif salario_bruto <= 1500:
     """
    Salário Bruto até 1500 (inclusive) - desconto de 5%
     """
     desconto_ir = 0.05
     desconto_ir_str = ' 5%'
     valor_desconto_ir = salario_bruto * desconto_ir

elif salario_bruto <= 2500:
     """
    Salário Bruto até 2500 (inclusive) - desconto de 10%
     """
     desconto_ir = 0.1
     desconto_ir_str = '10%'
     valor_desconto_ir = salario_bruto * desconto_ir

else:
    """
    Salário Bruto acima de 2500 - desconto de 20%
    """
    desconto_ir = 0.20
    desconto_ir_str = '20%'
    valor_desconto_ir = salario_bruto * desconto_ir

valor_desconto_total = valor_desconto_fgts + valor_desconto_ir + valor_desconto_sindical
salario_liquido = salario_bruto - valor_desconto_total

# Saida de dados:
print(f" |---------------------------------------------------------------------------------|")
print(f"   Salário Bruto: [ Valor da hora  |  Numero de horas trabalhadas ]  |      R$      ")
print(f"                          {valor_da_hora}                 {numero_de_horas_trabalhadas}                        {salario_bruto} ")
print(f" |---------------------------------------------------------------------------------|")
print()
print(f" (-) IR        ({desconto_ir_str})    : R$ ", end='')
print(valor_desconto_ir)
print(f" (-) FGTS      (11%)    : R$ ", end='')
print(valor_desconto_fgts)
print(f" (-) SINDICATO ( 3%)    : R$ ", end='')
print(valor_desconto_sindical)
print(f" Total de descontos     : R$ ", end='')
print(f"{valor_desconto_total:.2f}")
print(f" Salário Liquido        : R$ ", end='')
print(f"{salario_liquido:.2f}")
print()
       