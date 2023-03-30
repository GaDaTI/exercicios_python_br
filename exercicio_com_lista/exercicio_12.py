"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
 13 anos possuem altura inferior à média de altura desses alunos.
"""
lista_idade = [ ]
lista_altura = [ ]
for _ in range(11):
    altura = float(input("Digite sua altura: "))
    idade = int(input("Digite sua idade: "))
    lista_altura.append(altura)
    lista_idade.append(idade)

soma_das_alturas = sum(lista_altura)
media_de_altura = soma_das_alturas / 10
print(f"Altura média dos alunos é de {media_de_altura:.2f}")
contador = 0
for index, idade in enumerate(lista_idade):
    altura = lista_altura[index]
    if idade > 13 and altura > media_de_altura:
        contador += 1

print(f"Foram {contador} alunos com mais de13 anos possuem altura inferior à média de altura desses alunos")