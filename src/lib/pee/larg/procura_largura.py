from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira_fifo import FronteiraFIFO

'''
Classe que implementa o algoritmo de Procura em Largura (Breadth-First Search) num formato de grafo
'''
class ProcuraLargura(ProcuraGrafo):
    '''
    Método que inicializa o mecanismo com uma fronteira FIFO (fila)
    '''
    def __init__(self):
        super().__init__(FronteiraFIFO())