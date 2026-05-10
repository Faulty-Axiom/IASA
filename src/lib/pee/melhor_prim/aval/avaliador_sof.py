from pee.aval.avaliador_heur import AvaliadorHeur
from pee.mec_proc.no import No

'''
Classe que implementa o avaliador para o algoritmo de Procura Sôfrega (Greedy)
'''
class AvaliadorSof(AvaliadorHeur):
    '''
    Método que calcula a prioridade usando exclusivamente a estimativa heurística (h)
    '''
    def prioridade(self, no: No) -> float:
        return self.heuristica.h(no.estado)