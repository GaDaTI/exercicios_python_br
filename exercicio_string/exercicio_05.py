"""
05 - Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
"""
nome = input("Digite seu nome: ")

index = 0
for _ in nome:
    print(nome[   : len(nome) - index])
    index += 1

