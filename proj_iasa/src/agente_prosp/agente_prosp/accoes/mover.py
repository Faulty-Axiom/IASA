from lib.ecr.accao import Accao
from sae import Direccao

'''
Classe que define a ação de mover o agente numa direção específica
'''
class Mover(Accao):
    '''
    Método que inicializa a ação de mover com a direção pretendida
    '''
    def __init__(self, direccao: Direccao):
        super().__init__()
        self._direccao = direccao