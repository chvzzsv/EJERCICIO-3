class Jugador1:
    def __init__(self, nombreLuchador, poderLuchador):
        self.nombreLuchador= nombreLuchador
        self.poderLuchador= poderLuchador

    def caracteristicas(self):
        return 'El nombre del primer peleador se llama {} con un poder calculado de {}%'.format(self.nombreLuchador, self.poderLuchador)
    
Luchador = Jugador1('Luffy', 100)
print(Luchador.caracteristicas())