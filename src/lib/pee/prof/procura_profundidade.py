from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.no import No

'''
Classe que implementa o algoritmo de Procura em Profundidade (Depth-First Search) num formato de árvore
'''
class ProcuraProfundidade(MecanismoProcura):
    '''
    Método que inicializa o mecanismo com uma fronteira LIFO (pilha)
    '''
    def __init__(self):
        super().__init__(FronteiraLIFO())

    '''
    Método que concretiza a memorização, não efetuando qualquer registo por ser uma procura em árvore
    '''
    def _memorizar(self, no: No) -> None:
        pass