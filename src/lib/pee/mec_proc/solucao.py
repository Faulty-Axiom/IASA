from typing import Iterator
from pee.mec_proc.no import No
from pee.mec_proc.passo_solucao import PassoSolucao

'''
Classe iterável que representa a sequência de passos desde o estado inicial até ao objetivo
'''
class Solucao:
    '''
    Método que inicializa a solução a partir do nó final encontrado
    '''
    def __init__(self, no_final: No):
        self._passos = \
        [
        ]
        self._custo_total = no_final.custo
        
        no_actual = no_final
        while no_actual is not None and no_actual.antecessor is not None:
            passo = PassoSolucao(no_actual.estado, no_actual.operador)
            self._passos.insert(0, passo)
            no_actual = no_actual.antecessor

    '''
    Propriedade de leitura que devolve a dimensão (número de passos) da solução
    '''
    @property
    def dimensao(self) -> int:
        return len(self._passos)

    '''
    Propriedade de leitura que devolve o custo total da solução
    '''
    @property
    def custo(self) -> float:
        return self._custo_total

    '''
    Método que permite iterar sobre os passos da solução
    '''
    def __iter__(self) -> Iterator[PassoSolucao]:
        return iter(self._passos)