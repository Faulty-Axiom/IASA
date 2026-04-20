from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.resposta import Resposta

from src.agente_prosp.accoes.rodar import Rodar

'''
Classe que define a resposta do agente para evitar obstáculos através de uma rotação
'''
class RespostaEvitar(Resposta):
    '''
    Método que inicializa a resposta para a evasão de obstáculos
    '''
    def __init__(self):
        super().__init__(None)

    '''
    Método que determina a ação de evasão, retornando uma ação de rodar com base na perceção atual
    '''
    def _obter_accao(self, percepcao: Percepcao) -> Accao:
        pass