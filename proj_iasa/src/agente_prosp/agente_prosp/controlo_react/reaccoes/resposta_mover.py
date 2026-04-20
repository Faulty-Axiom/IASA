from lib.ecr.resposta import Resposta
from sae import Direccao

from src.agente_prosp.accoes.mover import Mover

'''
Classe que define a resposta de movimento do agente numa dada direção
'''
class RespostaMover(Resposta):
    '''
    Método que inicializa a resposta de movimento, criando a ação de mover caso a direção seja fornecida
    '''
    def __init__(self, direccao: Direccao = None):
        accao = Mover(direccao) if direccao is not None else None
        super().__init__(accao)