from lib.ecr.reaccao import Reaccao

from src.agente_prosp.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst
from src.agente_prosp.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar

'''
Classe que define a reação do agente para evitar obstáculos
'''
class EvitarObst(Reaccao):
    '''
    Método que inicializa a reação instanciando o estímulo e a resposta associados à evasão de obstáculos
    '''
    def __init__(self):
        estimulo = EstimuloObst()
        resposta = RespostaEvitar()
        
        super().__init__(estimulo, resposta)