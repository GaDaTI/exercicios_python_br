"""
4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
# Entrada de dados: Notas bimestrais
nota_1 = float(input("Digite a nota do primeiro bimestre: "))
nota_2 = float(input("Digite a nota do segundo bimestre: "))
nota_3 = float(input("Digite a nota do terceiro bimestre: "))
nota_4 = float(input("Digite a nota do terceiro semestre: "))

# Processaento de dados: Media da Soma das 4 notas bimestrais
soma_das_notas = nota_1 + nota_2 + nota_3 + nota_4
media_das_notas_bimestrais = soma_das_notas / 4


# Saida de dados: Apresentação da media 
print(f"A media é {media_das_notas_bimestrais}.")

