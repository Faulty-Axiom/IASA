from abc import ABC, abstractmethod
from lib.agente.percepcao import Percepcao

'''
Classe abstrata que define a interface para a deteção de estímulos no ambiente
'''
class Estimulo(ABC):
    '''
    Método abstrato responsável por processar uma perceção e retornar a intensidade do estímulo detetado
    '''
    @abstractmethod
    def detectar(self, percepcao: Percepcao) -> float:
        pass