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
    for ip_str in lista:
        print(type(ip_str))
        ip_numero = int(ip_str)
        print(type(ip_numero))
        #tamanho = len(ip_str.split('.'))
        #if tamanho == 4:
        #    if ip_numero >= 0 or ip_numero < 255:
        #        arquivo.writelines(ip_str)

        #print(tamanho)
        #print(len(tamanho))
        #print(type(tamanho))



