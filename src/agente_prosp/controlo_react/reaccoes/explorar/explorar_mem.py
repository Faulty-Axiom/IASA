import random
from typing import List, Tuple

from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.comportamento import Comportamento
from sae import Direccao
from sae import Posicao

from src.agente_prosp.accoes.avancar import Avancar
from src.agente_prosp.accoes.rodar import Rodar

'''
Classe que define o comportamento de exploração com memória de posições anteriores
'''
class ExplorarMem(Comportamento):
    '''
    Método que inicializa o comportamento de exploração, definindo a dimensão da memória e a ação de avanço padrão
    '''
    def __init__(self, dim_max_mem: int = 100):
        self._dim_max_mem = dim_max_mem
        self._memoria: List[Tuple[Posicao, Direccao]] = \
        [
        ]
        self._accao = Avancar()

    '''
    Método que avalia a perceção e utiliza o histórico de memória para decidir a próxima ação a tomar
    '''
    def activar(self, percepcao: Percepcao) -> Accao:
        estado_actual = (percepcao.posicao, percepcao.direccao)

        # Regista o estado atual na memória
        if estado_actual not in self._memoria:
            self._memoria.append(estado_actual)

        # Mantém a memória dentro do limite estabelecido
        if len(self._memoria) > self._dim_max_mem:
            self._memoria.pop(0)

        # Se o agente já visitou a mesma posição e direção repetidamente, assume que está num ciclo
        if self._memoria.count(estado_actual) > 2:
            direccoes_alternativas = \
            [
                d for d in Direccao if d != percepcao.direccao
            ]
            
            nova_direccao = random.choice(direccoes_alternativas)
            return Rodar(nova_direccao)

        # Se não houver repetição, prossegue com a ação por defeito
        return self._accao