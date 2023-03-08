"""
11 - As Organizações Tabajara resolveram dar um aumento de salário 
aos seus colaboradores e lhe contraram para desenvolver o programa 
que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o 
reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
# Entrada de dados: Recebe o salário de um colaborador
salario = float(input("Digite o valor do salário: "))

# Processamento de dados: Reajuste salarial
if salario > 1500:
    """
    salários de R$ 1500,00 em diante : aumento de 5% 
    """  
    percentual = 5  
    percentual_de_aumento_aplicado = 1.05
    novo_salario = percentual_de_aumento_aplicado * salario
    valor_do_aumento = novo_salario - salario 
elif salario >= 700:
    """
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    """
    percentual = 10  
    percentual_de_aumento_aplicado = 1.1
    novo_salario = percentual_de_aumento_aplicado * salario
    valor_do_aumento = novo_salario - salario
elif salario > 280:
    """
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    """
    percentual = 15  
    percentual_de_aumento_aplicado = 1.15
    novo_salario = percentual_de_aumento_aplicado * salario
    valor_do_aumento = novo_salario - salario
else:
    """
    salários até R$ 280,00 (incluindo) : aumento de 20%
    """
    percentual = 20
    percentual_de_aumento_aplicado = 1.2
    novo_salario = percentual_de_aumento_aplicado * salario
    valor_do_aumento = novo_salario - salario

# Saida de dados: Salario inicial, Novo Salario, Percentual de aumento, valor do aumento
print(f"O valor salário antes do reajuste era de {salario} reais.")
print(f"O percentual de aumento aplicado foi de {percentual} %")
print(f"O valor do aumento foi de {valor_do_aumento} reais")
print(f"O novo salário, após o aumento é de {novo_salario} reais")
