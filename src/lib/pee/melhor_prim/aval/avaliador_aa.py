from pee.aval.avaliador_heur import AvaliadorHeur
from pee.mec_proc.no import No

'''
Classe que implementa o avaliador para o algoritmo A*
'''
class AvaliadorAA(AvaliadorHeur):
    '''
    Método que calcula a prioridade somando o custo acumulado (g) à estimativa heurística (h)
    '''
    def prioridade(self, no: No) -> float:
        return no.custo + self.heuristica.h(no.estado)