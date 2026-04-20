from lib.agente.accao import Accao as AccaoAgente

'''
Classe que estende a ação base do agente, introduzindo a ideia de prioridade pna arquitetura reativa atual
'''
class Accao(AccaoAgente):
    '''
    Método que inicializa a ação com uma dada prioridade, assumindo o valor 0 por omissão
    '''
    def __init__(self, prioridade: float = 0.0):
        self._prioridade = prioridade

    '''
    Propriedade que devolve a prioridade atual da ação
    '''
    @property
    def prioridade(self) -> float:
        return self._prioridade

    '''
    Método que permite definir ou atualizar a prioridade da ação
    '''
    @prioridade.setter
    def prioridade(self, valor: float) -> None:
        self._prioridade = valor