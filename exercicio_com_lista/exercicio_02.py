"""
8 - Faça um Programa que peça a idade e a altura de 
5 pessoas, armazene cada informação no seu 
respectivo vetor. Imprima a idade e a altura na 
ordem inversa a ordem lida.
"""
lista = []
lista_pessoa = []
# Entrada de dados
for _ in range(0, 5):
    for index in range(2):
        if index == 0:
            idade = int(input("Digite a sua idade:"))
            lista.append(idade)
            idade=0
        else:
            altura = float(input("Digite sua altura: "))
            lista.append(altura)
            lista_pessoa.append(lista)
            lista=[]
    print()

contador = 0
for index, dados in enumerate(lista_pessoa):
    index += 1 
    for _ in dados:
        contador += 1
        if contador == 1:
            pessoa = f"A {index}º pessoa posui a idade de {dados[0]} anos e altura de {dados[1]} metros."
            print(pessoa)
        else:
            contador=0
            pass
    
    

