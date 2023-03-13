from Jugador1 import Jugador1
from Jugador2 import Jugador2
from Jugador1 import Luchador
from Jugador2 import Luchador2

class Juego(Jugador1, Jugador2):
    pass
    def pelear():
        return 'El Peleador {} tiene un poder de {}% y su rival llamado {} su poder es {}%'.format(Luchador.nombreLuchador, Luchador.poderLuchador, Luchador2.nombreLuchador2, Luchador2.poderLuchador2)
    
Luchadores = Juego
print(Luchadores.pelear())
print('El peleador ' + Luchador.nombreLuchador + ' acaba de lanzar un ataque a su enemigo')
print('El peleador ' + Luchador2.nombreLuchador2 + ' acaba de recibir un ataque restandole 30% de vida')
print('El nivel de vida de ' + Luchador2.nombreLuchador2 + ' ha bajado al 70%')