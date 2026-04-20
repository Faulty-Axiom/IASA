from lib.agente.percepcao import Percepcao
from lib.ecr.estimulo import Estimulo
from sae import Direccao

'''
Classe que define o estímulo para detetar um alvo numa direção específica
'''
class EstimuloAlvo(Estimulo):
    '''
    Método que inicializa o estímulo com a direção a avaliar e um fator de decaimento gama
    '''
    def __init__(self, direccao: Direccao, gama: float = 0.9):
        self._direccao = direccao
        self._gama = gama

    '''
    Método que calcula e retorna a intensidade do estímulo com base na perceção atual
    '''
    def detectar(self, percepcao: Percepcao) -> float:
        pass