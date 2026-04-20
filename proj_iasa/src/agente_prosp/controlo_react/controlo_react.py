from lib.agente.accao import Accao
from lib.agente.controlo import Controlo
from lib.agente.percepcao import Percepcao
from lib.ecr.comportamento import Comportamento

'''
Classe que adapta a arquitetura reativa à interface de controlo do agente
'''
class ControloReact(Controlo):
    '''
    Método que inicializa o controlo reativo com o comportamento base a executar
    '''
    def __init__(self, comportamento: Comportamento):
        self._comportamento = comportamento

    '''
    Método que processa a perceção delegando a decisão para o comportamento base e retorna a ação gerada
    '''
    def processar(self, percepcao: Percepcao) -> Accao:
        return self._comportamento.activar(percepcao)