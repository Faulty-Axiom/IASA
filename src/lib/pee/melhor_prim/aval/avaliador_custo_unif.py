from pee.aval.avaliador import Avaliador
from pee.mec_proc.no import No

'''
Classe que implementa o avaliador para o algoritmo de Procura de Custo Uniforme
'''
class AvaliadorCustoUnif(Avaliador):
    '''
    Método que define a prioridade de um nó como sendo o seu custo acumulado
    '''
    def prioridade(self, no: No) -> float:
        return no.custo