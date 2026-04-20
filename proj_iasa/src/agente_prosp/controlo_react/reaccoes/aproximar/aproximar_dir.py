from lib.ecr.reaccao import Reaccao
from sae import Direccao

from src.agente_prosp.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from src.agente_prosp.controlo_react.reaccoes.resposta_mover import RespostaMover

'''
Classe que define a reação do agente para se aproximar de um alvo numa dada direção
'''
class AproximarDir(Reaccao):
    '''
    Método que inicializa a reação instanciando o estímulo e a resposta correspondentes à direção especificada
    '''
    def __init__(self, direccao: Direccao):
        estimulo = EstimuloAlvo(direccao)
        resposta = RespostaMover(direccao)
        
        super().__init__(estimulo, resposta)