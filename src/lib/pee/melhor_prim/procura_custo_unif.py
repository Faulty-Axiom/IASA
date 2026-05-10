from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.aval.avaliador_custo_unif import AvaliadorCustoUnif

'''
Classe que implementa o algoritmo de Procura de Custo Uniforme num espaço de estados
'''
class ProcuraCustoUnif(ProcuraMelhorPrim):
    '''
    Método que inicializa o mecanismo instanciando e associando o avaliador de custo uniforme
    '''
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())