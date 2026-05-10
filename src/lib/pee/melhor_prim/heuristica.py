from abc import ABC, abstractmethod
from pee.mod.estado import Estado

'''
Interface que define o contrato funcional para as funções heurísticas
'''
class Heuristica(ABC):
    '''
    Método abstrato que calcula e devolve a estimativa de custo do estado até ao objetivo
    '''
    @abstractmethod
    def h(self, estado: Estado) -> float:
        pass