"""
06 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima
a data com o nome do mês por extenso.
"""
nascimento = input("Digite sua data de nascimento [ dd/mm/aaaa ] : ")

meses = [ "Janeiro" , "Fevereiro" , "Março" , "Abril" , "Maio" , "Junho" , "Julho" , "Agosto" , "Setembro" , "Outubro" , "Novembro", "Dezembro"]

dia = nascimento[:2]
mes = int(nascimento[3:5])
ano =  nascimento[6:]
meses_str = meses[mes-1]

print(f"Data de Nascimento: {nascimento}")
print(f"Você nasceu em  {dia} de {meses_str} de {ano}. ")

