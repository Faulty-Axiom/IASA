from abc import ABC, abstractmethod
from pee.mec_proc.no import No

'''
Classe abstrata que define o contrato funcional para a avaliação da prioridade de um nó
'''
class Avaliador(ABC):
    '''
    Método abstrato que calcula e devolve o valor numérico de prioridade de um dado nó
    '''
    @abstractmethod
    def prioridade(self, no: No) -> float:
        pass