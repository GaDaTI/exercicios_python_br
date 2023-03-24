"""
5 - Altere o programa anterior permitindo ao usuário 
informar as populações e as taxas de crescimento
 iniciais. Valide a entrada e permita repetir a 
 operação.
"""

valor = True
contador = aumento = 0

# Processamento de dados:
while valor:
    if contador == 0:
        # Entrada de dados
        inpt_populacao_a = float(input("Digite o numero de habitantes de 'A': "))
        inpt_populacao_b = float(input("Digite o numero de habitantes de 'B': "))

        if inpt_populacao_a == 0 or inpt_populacao_b == 0:
            valor = False
        else:
            taxa_crescimento_de_a = float(input("Digite a taxa de crescimento de 'A': "))
            taxa_crescimento_de_b = float(input("Digite a taxa de crescimento de 'B': "))

        


    ano_inicio = 2023

    aumento_de_a = inpt_populacao_a * taxa_crescimento_de_a
    inpt_populacao_a += aumento_de_a

    aumento_de_b = inpt_populacao_b * taxa_crescimento_de_b
    inpt_populacao_b += aumento_de_b

    
    if inpt_populacao_a <= inpt_populacao_b:
        contador += 1
    else:
        ano_final = ano_inicio + contador
        print(f"População 'A': {inpt_populacao_a:.2f}")
        print(f"População 'B': {inpt_populacao_b:.2f}")
        print(f"Ano que ultrapassa : {ano_final}")
        inpt_populacao_a = inpt_populacao_b = taxa_crescimento_de_a = taxa_crescimento_de_b =  0
        aumento_de_a = aumento_de_b = contador = 0
    

    

