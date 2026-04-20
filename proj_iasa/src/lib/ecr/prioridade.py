from typing import List
from lib.ecr.accao import Accao
from lib.ecr.comport_comp import ComportComp

'''
Classe que define um comportamento composto que seleciona a ação com o maior nível de prioridade
'''
class Prioridade(ComportComp):
    
    '''
    Método que avalia uma lista de ações e retorna aquela que possui a prioridade mais elevada
    '''
    def seleccionar_accao(self, accoes: List[Accao]) -> Accao:
        if not accoes:
            return None
            
        return max(accoes, key=lambda a: a.prioridade)