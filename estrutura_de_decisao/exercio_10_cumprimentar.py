"""
10 - Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
"Valor Inválido!", conforme o caso.
"""
# Entrada de dados:
turno = input("Digite [ M-matutino | V-Vespertino | N- Noturno ] :  ").upper()

# Processamento de dados:
if turno == 'M':
    resposta = f"Digitou '{turno}'. Bom Dia!"
elif turno == 'V':
    resposta = f"Digitou '{turno}'. Boa Tarde!"
else:
    resposta = f"Digitou '{turno}'. Boa Noite!"

# Saida de dados:
print(resposta)
