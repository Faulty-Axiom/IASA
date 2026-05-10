from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.aval.avaliador_heur import AvaliadorHeur
from pee.mod.problema import Problema
from pee.aval.heuristica import Heuristica
from pee.mec_proc.solucao import Solucao

'''
Classe abstrata que estende a procura Melhor-Primeiro para suportar algoritmos informados
'''
class ProcuraInformada(ProcuraMelhorPrim):
    '''
    Método que inicializa a procura retendo uma referência para o avaliador heurístico específico
    '''
    def __init__(self, avaliador: AvaliadorHeur):
        super().__init__(avaliador)
        self._avaliador_heur = avaliador

    '''
    Método que executa a procura, injetando a heurística no avaliador antes de iniciar a exploração
    '''
    def procurar(self, problema: Problema, heuristica: Heuristica) -> Solucao:
        self._avaliador_heur.heuristica = heuristica
        return super().procurar(problema)