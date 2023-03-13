"""
14 - Faça um programa que lê as duas notas parciais obtidas por 
um aluno numa disciplina ao longo de um semestre, e calcule a 
sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, 
o conceito correspondente e a mensagem “APROVADO” 
se o conceito for A, B ou C ou “REPROVADO” se o 
conceito for D ou E.

"""
# Entrada de dados
primeira_nota = float(input("Digite o valor da primeira nota: "))
segunda_nota = float(input("Digite o valor da segunda nota: "))

conceito = ''
conceito_aprovado = ['A', 'B', 'C']

# Processamento de dados
media = ( primeira_nota + segunda_nota ) / 2

if media > 9:
    conceito = 'A'
elif media > 7.5:
    conceito = 'B'
elif media > 6:
    conceito = 'C'
elif media > 4:
    conceito = 'D'
else:
    conceito = 'E'

# Saida de dados
if conceito in conceito_aprovado:
    print("APROVADO!")
else:
    print("REPROVADO!")

