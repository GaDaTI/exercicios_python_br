""""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

>>> # Teste de classe
>>> quadra_do_colegio = AreaQuadrant( )
>>> quadra_do_colegio.tamanho_do_lado
0
>>> quadra_do_colegio.mostrar_valor_do_lado()
0
>>> quadra_do_colegio.mudar_tamanho_do_lado(8)
>>> quadra_do_colegio.tamanho_do_lado
8
>>> quadra_do_colegio.mostrar_valor_do_lado()
8
>>> quadra_do_colegio.calculo_area()
64
"""


class AreaQuadrant:
    def __init__(self):
        self.area_da_quadra = 0
        self.tamanho_do_lado = 0

    def mostrar_valor_do_lado(self):
        return self.tamanho_do_lado

    def mudar_tamanho_do_lado(self, novo_valor):
        self.tamanho_do_lado = novo_valor

    def calculo_area(self):
        if self.tamanho_do_lado != 0:
            self.area_da_quadra = self.tamanho_do_lado ** 2
            return self.area_da_quadra
        else:
            return self.tamanho_do_lado

if __name__ == '__main__':
    quadra_do_colegio = AreaQuadrant( )
    print(id(quadra_do_colegio))
    print(type(quadra_do_colegio))
    # Aplicando valores : 1
    print(quadra_do_colegio.mostrar_valor_do_lado())
    quadra_do_colegio.mudar_tamanho_do_lado(8)
    print(quadra_do_colegio.mostrar_valor_do_lado())
    print(quadra_do_colegio.calculo_area())
    # Aplicando valores : 2
    quadra_do_colegio.mudar_tamanho_do_lado(12)
    print(quadra_do_colegio.mostrar_valor_do_lado())
    print(quadra_do_colegio.calculo_area())
    





