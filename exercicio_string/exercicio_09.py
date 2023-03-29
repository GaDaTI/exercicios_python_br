"""
09- Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos
caracteres de formatação.
"""
cpf = input("Digite o seu CPF:  ")

#Passo: Verifique se o número tem 11 dígitos. CPFs com menos ou mais dígitos são inválidos.
cpf_str = f'{cpf[:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:14]}'
quantidade_de_numeros = len(cpf_str)
print(f"{cpf_str}")
print(quantidade_de_numeros)
#Passo: Multiplique cada um dos nove primeiros dígitos por um peso decrescente, de 10 a 2. Por exemplo, o primeiro dígito é multiplicado por 10, o segundo por 9, o terceiro por 8 e assim por diante.
numeros = cpf_str[:9]

multiplicador = 10
lista = []
for cpf_numeros  in numeros :
    cpf_numero = int(cpf_numeros)
    valor = multiplicador * cpf_numero
    lista.append(valor)
    valor = 0
    multiplicador -= 1

print(lista)
#Passo: Some o resultado das multiplicações.
soma_das_multiplicações = sum(lista)
print(soma_das_multiplicações)

#Passo: Divida a soma por 11 e anote o resto da divisão.
divisao_por_11 = soma_das_multiplicações / 11
resto_divisao_por_11 = soma_das_multiplicações % 11
print(f"{divisao_por_11:.2f}")
print(f"{resto_divisao_por_11}")


#Passo: Se o resto da divisão for igual a 0 ou 1, o dígito verificador (os dois últimos dígitos do CPF) deve ser igual a 0. Se o resto da divisão for maior que 1, o dígito verificador deve ser igual a 11 menos o resto da divisão.

#Passo: Verifique se os dois últimos dígitos do CPF são iguais ao dígito verificador que você encontrou.




