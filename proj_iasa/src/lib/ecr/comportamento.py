from abc import ABC, abstractmethod
from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao

'''
Classe abstrata que serve de interface estrutural para todos os comportamentos do sistema reativo
'''
class Comportamento(ABC):
    '''
    Método abstrato responsável por receber uma perceção e gerar uma ação correspondente
    '''
    @abstractmethod
    def activar(self, percepcao: Percepcao) -> Accao:
        pass