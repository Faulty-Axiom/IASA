from pee.aval.avaliador import Avaliador
from pee.aval.heuristica import Heuristica

'''
Classe abstrata base para avaliadores que dependem de uma função heurística
'''
class AvaliadorHeur(Avaliador):
    '''
    Método que inicializa o avaliador heurístico sem uma heurística pré-definida
    '''
    def __init__(self):
        self._heuristica: Heuristica = None

    '''
    Propriedade de leitura/escrita que permite injetar a função heurística a utilizar
    '''
    @property
    def heuristica(self) -> Heuristica:
        return self._heuristica

    @heuristica.setter
    def heuristica(self, heuristica: Heuristica) -> None:
        self._heuristica = heuristica