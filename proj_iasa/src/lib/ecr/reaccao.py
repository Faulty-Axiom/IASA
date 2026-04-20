from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.estimulo import Estimulo
from lib.ecr.resposta import Resposta
from lib.ecr.comportamento import Comportamento

'''
Classe que define uma reação, um comportamento base que liga diretamente um estímulo a uma resposta
'''
class Reaccao(Comportamento):
    '''
    Método que inicializa a reação associando-lhe o estímulo a detetar e a resposta correspondente
    '''
    def __init__(self, estimulo: Estimulo, resposta: Resposta):
        self._estimulo = estimulo
        self._resposta = resposta

    '''
    Método que processa a perceção através do estímulo e, caso a intensidade for superior a zero, ativa e devolve a resposta
    '''
    def activar(self, percepcao: Percepcao) -> Accao:
        intensidade = self._estimulo.detectar(percepcao)
        
        if intensidade > 0:
            return self._resposta.activar(percepcao, intensidade)
            
        return None