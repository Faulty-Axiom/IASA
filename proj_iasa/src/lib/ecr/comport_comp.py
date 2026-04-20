from typing import List
from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.comportamento import Comportamento

'''
Classe que define um comportamento composto, agregando múltiplos comportamentos
'''
class ComportComp(Comportamento):
    '''
    Método que inicializa o comportamento composto com uma lista de comportamentos dependentes
    '''
    def __init__(self, comportamentos: List[Comportamento]):    
        self._comportamentos = comportamentos

    def activar(self, percepcao: Percepcao) -> Accao:
        pass

    def seleccionar_accao(self, accoes: List[Accao]) -> Accao:
        pass