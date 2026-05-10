from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.mec_proc.fronteira_prioridade import FronteiraPrioridade
from pee.aval.avaliador import Avaliador
from pee.mec_proc.no import No

'''
Classe que implementa o mecanismo base para algoritmos de procura Melhor-Primeiro
'''
class ProcuraMelhorPrim(ProcuraGrafo):
    '''
    Método que inicializa a procura configurando a fronteira de prioridade com o avaliador especificado
    '''
    def __init__(self, avaliador: Avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
        self._avaliador = avaliador

    '''
    Método protegido que sobrepõe a validação de nós mantidos, permitindo a reexploração de um estado caso o novo caminho tenha um custo inferior
    '''
    def _manter(self, no: No) -> bool:
        # Mantém se o estado ainda não foi explorado, oU se o novo nó tem um custo menor do que o previamente registado
        return super()._manter(no) or no.custo < self._explorados[no.estado.id_valor()].custo