"""
6 - Faça um Programa que peça as quatro notas de 
10 alunos, calcule e armazene num vetor a média 
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
# Entrada de dados
lista = []
lista_nota_alunos = []
qtd_alunos_nota_maior_que_sete = 0

for matricula in range(1, 4):    
    for index in range(4):
        nota = float(input(f"Aluno {matricula} valor da nota: "))
        lista_nota_alunos.append(nota)

        if index == 3:
            soma_das_notas = sum(lista_nota_alunos)
            media = soma_das_notas / 4
            print(f"Aluno {matricula}: {media:.2f} de media.")
            print()

            if media > 7:
                qtd_alunos_nota_maior_que_sete += 1
    
    lista.append(lista_nota_alunos)
    lista_nota_alunos = []
    nota = 0

print(f"Quantidade de alunos com média maior que 7: {qtd_alunos_nota_maior_que_sete}")
