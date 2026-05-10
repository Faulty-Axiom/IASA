from abc import ABC, abstractmethod
from typing import List
from pee.mec_proc.no import No

'''
Classe abstrata que define a estrutura de dados para armazenar os nós a explorar
'''
class Fronteira(ABC):
    '''
    Método que inicializa a fronteira com uma lista vazia de nós
    '''
    def __init__(self):
        self._nos: List[No] = \
        [
        ]

    '''
    Propriedade de leitura que indica se a fronteira se encontra vazia
    '''
    @property
    def vazia(self) -> bool:
        return len(self._nos) == 0

    '''
    Método que limpa a fronteira, removendo todos os nós armazenados
    '''
    def iniciar(self) -> None:
        self._nos.clear()

    '''
    Método abstrato para inserir um novo nó na fronteira
    '''
    @abstractmethod
    def inserir(self, no: No) -> None:
        pass

    '''
    Método que remove e retorna o próximo nó a ser explorado (comportamento base)
    '''
    def remover(self) -> No:
        if not self.vazia:
            return self._nos.pop(0)
        return None