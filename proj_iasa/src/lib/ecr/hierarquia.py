from typing import List
from lib.ecr.accao import Accao
from lib.ecr.comport_comp import ComportComp

'''
Classe que define um comportamento composto que seleciona ações com base numa ordem estrita
'''
class Hierarquia(ComportComp):
    
    '''
    Método que seleciona a primeira ação da lista, respeitando a ordem hierárquica dos comportamentos
    '''
    def seleccionar_accao(self, accoes: List[Accao]) -> Accao:
        if accoes:
            return accoes[0]
        return None