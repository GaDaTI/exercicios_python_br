"""
01- Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem
o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""

frase_1 = input("Digite a primeira frase: ")
frase_2= input("Digite a segunda frase: ")
tamanho_frase_1 = len(frase_1)
tamanho_frase_2= len(frase_2)

if  tamanho_frase_1 == frase_2:
    print(f"O tamanho da frase 1 é de {tamanho_frase_1} caracteres.")
    print(f"O tamanho da frase 2 é de {tamanho_frase_2} caracteres.")
    print("As duas strings são de tamanhos iguais")
else:
    print(f"O tamanho da frase 1 é de {tamanho_frase_1} caracteres.")
    print(f"O tamanho da frase 2 é de {tamanho_frase_2} caracteres.")
    print("As duas strings são de tamanhos diferentes ")


