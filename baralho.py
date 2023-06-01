import random
from carta import Carta
from constantes import carta_valores, carta_nipes

class Baralho:
    """ Classe que define um baralho de cartas. """
    def __init__(self):
        self.cartas = self.novodeque()

    def novodeque(self):
        """ Método de geração das cartas de forma ordenada. """
        cartas = [Carta(v, n) for v in list(carta_valores) for n in list(carta_nipes)]
        return self.embaralhar(cartas)

    def embaralhar(self, cartas):
        random.shuffle(cartas)
        return cartas
    
    def virar(self):
        """ Retira a carta do topo e remove do baralho... """
        return self.cartas.pop()
    
    def esvaziar_baralho(self):
        for idx, item in enumerate(self.cartas):
            self.cartas.pop(idx)
            print(f'Carta {item} removida com sucesso')
