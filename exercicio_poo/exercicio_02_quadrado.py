"""
02 - Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class MetroQuadrado:

    def __init__(self,  lado):
        self.tamanho_lado = lado

    def mudar_valor_de_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def calcular_area(self,  lado):
        self.resultado = lado * lado
        return  self.resultado

    def retornar_valor_lado(self,):
        return  self.tamanho_lado


if  __name__   ==  ' __main__' :
    quadra_escolar=MetroQuadrado(  )
    quadra_escolar.tamanho_lado(5)
    print(quadra_escolar.__dict__)
