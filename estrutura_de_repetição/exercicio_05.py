"""
2 - Faça um programa que leia um nome de usuário e a sua senha
 e não aceite a senha igual ao nome do usuário, mostrando uma 
 mensagem de erro e voltando a pedir as informações.
"""
# Entrada de dados
valor = True
while valor:
    inpt_usuario = input("Digite o nome do usuario: ")
    inpt_senha = input("Digite a senha: ")

    if inpt_usuario == inpt_senha:
        print("Senha e login invalidos!")
        print("Tente novamente!")
    else:
        print("Login executado com sucesso!")
        valor = False