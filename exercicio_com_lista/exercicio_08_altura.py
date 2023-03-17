"""
8 - Faça um Programa que peça a idade e a altura de 
5 pessoas, armazene cada informação no seu 
respectivo vetor. Imprima a idade e a altura na 
ordem inversa a ordem lida.
"""
lista = []
lista_pessoa = []
# Entrada de dados
for _ in range(1, 5):
    for index in range(2):
        if index == 0:
            idade = int(input("Digite a sua idade:"))
            lista.append(idade)
            idade=0
        else:
            altura = float(input("Digite sua altura: "))
            lista.append(altura)
            lista_pessoa.append(lista)
            lista=0
    print()

for dados in lista:
    contador += 1
    for idade, altura in enumerate(dados):
        pessoa = f"A pessoa {contador} posui a idade de {idade} anos e altura de {altura:.2f} metros."

    print(pessoa)
    

