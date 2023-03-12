"""
1 - Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
"""

# Entrada de dados
valor = True
inpt_nota = float(input("Digite o valor da nota entre zero e dez: "))

while valor:
    if not (0 < inpt_nota <= 10):   
        print("Valor da nota invalido !")
        inpt_nota = float(input("Digite o valor da nota entre zero e dez: "))
    else:
        valor = False

    


