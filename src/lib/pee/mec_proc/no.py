from pee.mod.estado import Estado
from pee.mod.operador import Operador

'''
Classe que representa um nó na árvore de procura, encapsulando um estado e o histórico de como foi alcançado
'''
class No:
    '''
    Método que inicializa um nó com o seu estado, operador, antecessor e custo acumulado
    '''
    def __init__(self, estado: Estado, operador: Operador = None, antecessor: 'No' = None, custo: float = 0.0):
        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor
        self._custo = custo
        self.prioridade = 0
        
        # A profundidade é inferida a partir do antecessor
        if antecessor is not None:
            self._profundidade = antecessor.profundidade + 1
        else:
            self._profundidade = 0

    '''
    Propriedade de leitura que devolve a profundidade do nó na árvore
    '''
    @property
    def profundidade(self) -> int:
        return self._profundidade

    '''
    Propriedade de leitura que devolve o custo acumulado desde a raiz até este nó
    '''
    @property
    def custo(self) -> float:
        return self._custo

    '''
    Propriedade de leitura que devolve o estado associado ao nó
    '''
    @property
    def estado(self) -> Estado:
        return self._estado

    '''
    Propriedade de leitura que devolve o operador que gerou o nó
    '''
    @property
    def operador(self) -> Operador:
        return self._operador

    '''
    Propriedade de leitura que devolve o nó antecessor na árvore
    '''
    @property
    def antecessor(self) -> 'No':
        return self._antecessor

    '''
    Método de comparação de instâncias (<<comparable>>) com base no valor de prioridade
    '''
    def __lt__(self, outro: 'No') -> bool:
        return self.prioridade < outro.prioridade