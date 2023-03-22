""""
01 - Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""
class Bola:

    def __init__(self, cor= None, circunferencia= None, material= None,):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self,):
        self.cor = None

    def mostrar_cor(self):
        return self.cor


if   __name__  ==  '__main__' :
    bola_futsal = Bola(  )
    print(bola_futsal.__dict__)

