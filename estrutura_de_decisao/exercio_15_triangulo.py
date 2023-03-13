"""
15 - Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer
 dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""
# Entrada de dados
lado_a = float(input("Valor do lado 'A' do triangulo: "))
lado_b = float(input("Valor do lado 'B' do triangulo: "))
lado_c = float(input("Valor do lado 'C' do triangulo: "))

# Processamento de dados
if lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
    print("Triângulo Escaleno")
elif lado_a == lado_b and lado_b == lado_c and lado_a == lado_c:
    print("Triângulo Equilátero")
else:
    print("Triângulo Isósceles")



