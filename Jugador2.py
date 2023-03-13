class Jugador2:
    def __init__(self, nombreLuchador2, poderLuchador2):
        self.nombreLuchador2= nombreLuchador2
        self.poderLuchador2= poderLuchador2

    def caracteristicas(self):
        return 'El nombre del segundo peleador que es el contrincante se llama {} con un poder calculado de {}%'.format(self.nombreLuchador2, self.poderLuchador2)
    
Luchador2 = Jugador2('Broly', 100)
print(Luchador2.caracteristicas())