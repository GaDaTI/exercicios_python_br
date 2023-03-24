"""
3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
#Entrada de dados
valor = 5
contador = 0
while valor > contador:
    """
    Nome: maior que 3 caracteres;
    """
    inpt_nome = input("Digite seu nome: ")
    if len(inpt_nome) > 3:
        contador += 1
        print("inpt_nome = ok")
    else:
        contador += -1
        print("inpt_nome = Falha")
    
    """
    Idade: entre 0 e 150;
    """
    inpt_idade = int(input("Digite sua idade: "))
    if 0 < inpt_idade <= 150:
        contador += 1
        print("inpt_idade = ok")
    else:
        contador += -1
        print("inpt_idade = Falha")

    """
    Salário: maior que zero;
    """
    inpt_salario = float(input("Digite o valor de seu salário: "))
    if inpt_salario > 0:
        contador += 1
        print("inpt_salario = ok")
    else:
        contador += -1
        print("inpt_salario = Falha")
    
    """
    Sexo: 'f' ou 'm';
    """
    inpt_sexo = input("Digite  ['M' : Masculino ] ou ['F' : feninino]: ").upper()
    if inpt_sexo == 'F' or inpt_sexo == 'M':
        contador += 1
        print("inpt_sexo = ok")
    else:
        contador += -1
        print("inpt_sexo = Falha")

    """
    Estado Civil: 's', 'c', 'v', 'd';
    """
    lista = ['S', 'C', 'V', 'D']
    print("['S' : Solteiro ] | ['C' : Casado] | ['V' : Viuvo ] | ['D' : Divorciado]: ")
    inpt_estado_civil = input("Digite seu estado civil: ").upper()
    if inpt_estado_civil in lista:
        contador += 1
        print("inpt_estado_civil = ok")
    else:
        contador += -1
        print("inpt_estado_civil = Falha")
    
    if contador < 5:
        print("Tente novamente!")
    else:
        contador = 6


print(f"Seu nome é {inpt_nome}")
print(f"Sua idade é {inpt_idade}")
print(f"Seu salario é {inpt_salario}")
print(f"Seu sexo é {inpt_sexo}")
print(f"Seu estado civil é {inpt_estado_civil}")