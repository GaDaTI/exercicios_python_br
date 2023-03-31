"""
14- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
quantidade = 0
lista_resposta = [ ]
lista_perguntas = [ "Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]
for index, pergunta in  enumerate(lista_perguntas):
    print(f"{pergunta}", end='')
    resposta = input(' ')
    lista_resposta.append(resposta)

quantidade = lista_resposta.count('sim')

if quantidade < 3:
    print("Suspeita")
elif quantidade < 5:
    print("Cúmplice" )
else:
    print("Assassino")


