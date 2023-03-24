"""
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
# Entrada de dados:
letra = input("Digite uma letra: ").upper()
lista = ['A','E','I','O','U']

# Processamento de dados:
if letra in lista:
    resposta = f"A letra digitada '{letra}' é uma vogal."
else:
    resposta = f"A letra digitada '{letra}' não é uma vogal."

# Saida de dados:
print(resposta)
