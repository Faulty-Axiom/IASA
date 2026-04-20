import random
from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.comportamento import Comportamento
from sae import Direccao

from src.agente_prosp.accoes.rodar import Rodar
from src.agente_prosp.accoes.avancar import Avancar

'''
Classe que define o comportamento de exploração do agente através de movimentos aleatórios
'''
class Explorar(Comportamento):
    '''
    Método que inicializa o comportamento de exploração com uma probabilidade de rotação definida
    '''
    def __init__(self, prob_rotacao: float = 0.7):
        self._prob_rotacao = prob_rotacao

    '''
    Método que gera uma ação aleatória, decidindo entre rodar para uma direção ao acaso ou avançar, com base na probabilidade de rotação
    '''
    def activar(self, percepcao: Percepcao) -> Accao:
        if random.random() < self._prob_rotacao:
            direccao = random.choice(list(Direccao))
            return Rodar(direccao)
        
        return Avancar()