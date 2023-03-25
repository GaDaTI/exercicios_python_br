""""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

>>> bola_futsal = Bola()
>>> bola_futsal.mostrar_cor()
'Azul'
>>> bola_futsal.circunferencia
150
>>> bola_futsal.material
'Couro'
>>> bola_futsal.troca_cor('Verde')
>>> bola_futsal.nova_cor
'Verde'
>>> bola_futsal.mostrar_cor()
'Verde'

"""


class Bola:

    def __init__(self):
        self.cor = 'Azul'
        self.nova_cor = 'Verde'
        self.material = 'Couro'
        self.circunferencia = 150


    def mostrar_cor(self):
        if self.cor != self.nova_cor:
            return self.nova_cor
        else:
            return self.cor

    def troca_cor(self, nova_cor):
        self.nova_cor = nova_cor




    

