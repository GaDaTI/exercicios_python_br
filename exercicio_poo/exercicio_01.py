"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

>>> bola_futsal = Bola('Azul', 123, 'couro')
>>> bola_futsal.cor
Azul
>>> bola_futsal.circunferencia
123
>>> bola_futsal.material
couro
>>> bola_futsal.trocar_de_cor('Rosa')

>>> bola_futsal.mostrar_cor()
Rosa
>>> bola_futsal.trocar_de_cor('Amarelo')
>>> bola_futsal.mostrar_cor()
Amarelo
"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.material = material
        self.circunferencia = circunferencia

    def trocar_de_cor(self, outra_cor):
        self.cor = outra_cor

    def mostrar_cor(self):
        return self.cor


if __name__ == '__main__':
    bola_futsal = Bola('Azul', 123, 'couro')
    print(bola_futsal.cor)
