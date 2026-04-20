from lib.ecr.accao import Accao
from sae import Direccao

'''
Classe que define a ação de rodar o agente para uma direção específica
'''
class Rodar(Accao):
    '''
    Método que inicializa a ação de rodar com a direção pretendida
    '''
    def __init__(self, direccao: Direccao):
        super().__init__()
        self._direccao = direccao