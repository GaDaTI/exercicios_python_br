"""
5 - Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
# Entrada de dados:
primeira_nota = float(input("Digite o valor da primeira nota: "))
segunda_nota = float(input("Digite o valor da segunda nota: "))

# Processamento de dados:
media = ( primeira_nota + segunda_nota ) / 2

if media == 10:
    resposta = f"Sua média foi '{media}'. Você foi Aprovado com Distinção!"
elif media >= 7:
    resposta = f"Sua média foi '{media}'. Você foi Aprovado!"
else:
    resposta = f"Sua média foi '{media}'. Você foi Reprovado!"

# Saida de dados:
print(resposta)
