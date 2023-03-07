"""
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra 
escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
# Entrada de dados:
letra = input("Digite uma letra: ").upper()

# Processamento de dados:
if letra == 'F':
    resposta = f"Foi digitado a letra '{letra}' correspondente a Feminino."
elif letra == 'M':
    resposta = f"Foi digitado a letra '{letra}' correspondente a Masculino."
else:
    resposta = f"Foi digitado a letra '{letra}'. Trata-se de um Sexo Invalido."

# Saida de dados:
print(resposta)
