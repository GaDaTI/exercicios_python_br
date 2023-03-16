"""
6 - Faça um Programa que peça as quatro notas de 
10 alunos, calcule e armazene num vetor a média 
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
# Entrada de dados
lista = []
lista_nota_alunos = []

for index in range(3):    
    for index in range(4):
        nota = float(input("Digite o valor da nota: "))
        lista_nota_alunos.append(nota)
    
    nota = 0
    lista.append(lista_nota_alunos)

print(lista)