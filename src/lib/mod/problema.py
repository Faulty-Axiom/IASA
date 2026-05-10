from abc import ABC, abstractmethod
from typing import List
from mod.estado import Estado
from mod.operador import Operador

'''
Classe abstrata que define a formulação de um problema de procura
'''
class Problema(ABC):
    '''
    Método que inicializa o problema definindo o seu estado inicial e a lista de operadores aplicáveis
    '''
    def __init__(self, estado_inicial: Estado, operadores: List[Operador]):
        self._estado_inicial = estado_inicial
        self._operadores = operadores
        
    '''
    Propriedade de leitura que devolve o estado inicial configurado para o problema
    '''
    @property
    def estado_inicial(self) -> Estado:
        return self._estado_inicial

    '''
    Propriedade de leitura que devolve a lista de operadores definidos para o problema
    '''
    @property
    def operadores(self) -> List[Operador]:
        return self._operadores

    '''
    Método abstrato que avalia se um determinado estado corresponde ao objetivo do problema
    '''
    @abstractmethod
    def objectivo(self, estado: Estado) -> bool:
        pass