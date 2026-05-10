from abc import ABC, abstractmethod
from mod.estado import Estado

'''
Classe abstrata que define um operador responsável por transitar entre estados no problema
'''
class Operador(ABC):
    '''
    Método abstrato que aplica o operador a um estado, gerando e retornando o estado sucessor
    '''
    @abstractmethod
    def aplicar(self, estado: Estado) -> Estado:
        pass

    '''
    Método abstrato que calcula e devolve o custo de transição entre um estado e o seu sucessor
    '''
    @abstractmethod
    def custo(self, estado: Estado, estado_suc: Estado) -> float:
        pass