"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
"""

with open('relatorio.txt', 'r') as arquivo:
    lista = arquivo.readlines()
    #print(type(lista))
    #print(lista)

with open('relatorio_editado', 'w') as arquivo :
    cabecalho = '[Endereços válidos:]'
    arquivo.writelines(f'{cabecalho:}\n')
    for indice, ips  in enumerate(lista):
        ips = ips.split('.')
        for numero in ips:
            numero = int(numero)
            if  0 < numero > 255 and contador < 4:








