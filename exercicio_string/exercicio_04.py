"""
04 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

"""
nome = input("Digite um nome : ")

for contador, _  in enumerate(nome):
    print(f'{nome[:contador+1]}')