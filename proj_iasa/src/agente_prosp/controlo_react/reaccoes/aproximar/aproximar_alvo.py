from lib.ecr.prioridade import Prioridade
from sae import Direccao

from src.agente_prosp.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir

'''
Classe que define o comportamento composto de aproximação ao alvo, selecionando a direção com maior prioridade
'''
class AproximarAlvo(Prioridade):
    '''
    Método que inicializa a aproximação ao alvo agregando as reações de aproximação para as quatro direções cardeais
    '''
    def __init__(self):
        comportamentos = \
        [
            AproximarDir(Direccao.NORTE),
            AproximarDir(Direccao.SUL),
            AproximarDir(Direccao.ESTE),
            AproximarDir(Direccao.OESTE)
        ]
        
        super().__init__(comportamentos)