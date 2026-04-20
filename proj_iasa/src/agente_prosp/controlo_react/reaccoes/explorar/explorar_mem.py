from typing import List, Tuple

from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.comportamento import Comportamento
from sae import Direccao
from sae import Posicao

from src.agente_prosp.accoes.avancar import Avancar

'''
Classe que define o comportamento de exploração com memória de posições anteriores
'''
class ExplorarMem(Comportamento):
    '''
    Método que inicializa o comportamento de exploração, definindo a dimensão da memória e a ação de avanço padrão
    '''
    def __init__(self, dim_max_mem: int = 100):
        self._dim_max_mem = dim_max_mem
        self._memoria: List[Tuple[Posicao, Direccao]] = []
        self._accao = Avancar()

    '''
    Método que avalia a perceção e utiliza o histórico de memória para decidir a próxima ação a tomar
    '''
    def activar(self, percepcao: Percepcao) -> Accao:
        pass