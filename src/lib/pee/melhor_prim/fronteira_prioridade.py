import heapq
from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No
from pee.aval.avaliador import Avaliador

'''
Classe que implementa uma fronteira de exploração ordenada por prioridade (Min-Heap)
'''
class FronteiraPrioridade(Fronteira):
    '''
    Método que inicializa a fronteira associando-lhe o avaliador que ditará a ordem dos nós
    '''
    def __init__(self, avaliador: Avaliador):
        super().__init__()
        self._avaliador = avaliador

    '''
    Método que avalia a prioridade do nó, atribui-lhe esse valor e insere-o de forma ordenada na fronteira
    '''
    def inserir(self, no: No) -> None:
        no.prioridade = self._avaliador.prioridade(no)
        heapq.heappush(self._nos, no)

    '''
    Método que remove e retorna o nó com a prioridade mais elevada (menor valor numérico associado)
    '''
    def remover(self) -> No:
        if not self.vazia:
            return heapq.heappop(self._nos)
            
        return None