from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao

'''
Classe que define a resposta a um dado estímulo através duma ação a ser executada
'''
class Resposta:
    '''
    Método que inicializa a resposta com a ação predefinida
    '''
    def __init__(self, accao: Accao):
        self._accao = accao

    def _obter_accao(self, percepcao: Percepcao) -> Accao:
        return self._accao

    '''
    Método que ativa a resposta, ajustando a prioridade da ação de acordo com a intensidade do estímulo
    '''
    def activar(self, percepcao: Percepcao, intensidade: float = 0.0) -> Accao:
        accao = self._obter_accao(percepcao)
        
        if accao is not None:
            accao.prioridade = intensidade
            
        return accao