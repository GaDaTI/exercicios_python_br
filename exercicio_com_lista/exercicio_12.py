"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
 13 anos possuem altura inferior à média de altura desses alunos.
"""
lista_pessoa = [ ]
lista_dados = [ ]
for _ in range(5):
    for indice in range(2):
        if indice == 0:
            valor = 'sua altura'
        else:
            valor = 'sua idade'

        dados = float(input(f"Digite  {valor} : "))
        lista_dados.append(dados)

    lista_pessoa.append(lista_dados)
    lista_dados = [ ]

contagem = 0
soma_altura = 0
for indice in range(len(lista_pessoa)):
    altura, idade = lista_pessoa[indice]
    soma_altura += altura
    media_das_alturas = soma_altura / 5
    if idade > 13 and  altura < media_das_alturas:
        contagem += 1

print(f"Foram {contagem} alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.")