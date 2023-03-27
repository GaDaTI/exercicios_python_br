"""
07 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
 (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

frase = input("Digite uma frase:  ").lower()

vogais = ['a', 'e', 'i', 'o', 'u']

quantidade_de_vogais = 0
contador_espacos_vazios = 0
item = ' '
for _, item in enumerate(frase):
    if item in frase:
        if item == ' ':
            contador_espacos_vazios += 1

        if item in vogais:
            quantidade_de_vogais += 1

print(f"Quantidade de espaços vazios: {contador_espacos_vazios}")
print(f"Quantidade de vogais:  {quantidade_de_vogais} ")