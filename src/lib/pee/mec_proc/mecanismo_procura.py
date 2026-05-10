from abc import ABC, abstractmethod
from typing import List
from pee.mod.problema import Problema
from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

'''
Classe abstrata que define o motor base para os algoritmos de procura
'''
class MecanismoProcura(ABC):
    '''
    Método que inicializa o mecanismo associando-lhe uma fronteira de exploração
    '''
    def __init__(self, fronteira: Fronteira):
        self._fronteira = fronteira

    '''
    Método protegido que reinicia as estruturas de memória do mecanismo
    '''
    def _iniciar_memoria(self) -> None:
        self._fronteira.iniciar()

    '''
    Método abstrato protegido para memorizar um nó gerado
    '''
    @abstractmethod
    def _memorizar(self, no: No) -> None:
        pass

    '''
    Método principal que executa o algoritmo de procura para um dado problema
    '''
    def procurar(self, problema: Problema) -> Solucao:
        self._iniciar_memoria()
        no_inicial = No(problema.estado_inicial)
        self._fronteira.inserir(no_inicial)

        while not self._fronteira.vazia:
            no = self._fronteira.remover()

            if problema.objectivo(no.estado):
                return Solucao(no)

            self._memorizar(no)

            for no_suc in self._expandir(problema, no):
                # Caso seja uma procura em grafo, filtra através do _manter
                if hasattr(self, '_manter') and not self._manter(no_suc):
                    continue
                    
                self._fronteira.inserir(no_suc)

        return None

    '''
    Método protegido que expande um nó, gerando e devolvendo a lista dos seus nós sucessores
    '''
    def _expandir(self, problema: Problema, no: No) -> List[No]:
        sucessores = \
        [
        ]
        
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            
            if estado_suc is not None:
                custo_suc = no.custo + operador.custo(no.estado, estado_suc)
                no_suc = No(estado_suc, operador, no, custo_suc)
                sucessores.append(no_suc)
                
        return sucessores