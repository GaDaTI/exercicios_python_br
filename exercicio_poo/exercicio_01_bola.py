""""
01 - Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""
class Bola:

    def __init__(self, cor = 'Azul', circunferencia= None, material= None,):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cor):
        self.cor =  cor

    def mostrar_cor(self):
        return self.cor


if  __name__  ==  '__main__' :
    bola_futsal = Bola(  )
    print(f"Metodo mostra a cor : {bola_futsal.mostrar_cor()}")
    bola_futsal.trocar_cor("Vermelho")
    print(f"Metodo mostra a cor : {bola_futsal.mostrar_cor()}")
    bola_futsal.cor = "branca "
    print(f"Metodo mostra a cor : {bola_futsal.mostrar_cor()}")


