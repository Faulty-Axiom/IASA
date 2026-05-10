from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No

'''
Classe abstrata que implementa a base metodológica para procuras em grafo, gerindo a memória de estados explorados
'''
class ProcuraGrafo(MecanismoProcura):
    '''
    Método que inicializa o mecanismo, recebendo a fronteira a utilizar e instanciando o dicionário de explorados
    '''
    def __init__(self, fronteira: Fronteira):
        super().__init__(fronteira)
        self._explorados = {}

    '''
    Método protegido que reinicia a fronteira e limpa a memória de estados explorados
    '''
    def _iniciar_memoria(self) -> None:
        super()._iniciar_memoria()
        self._explorados.clear()

    '''
    Método protegido que regista um nó como explorado, utilizando a identificação única do seu estado
    '''
    def _memorizar(self, no: No) -> None:
        self._explorados[no.estado.id_valor()] = no

    '''
    Método protegido que avalia se um nó deve ser mantido, verificando se o seu estado já foi previamente explorado
    '''
    def _manter(self, no: No) -> bool:
        return no.estado.id_valor() not in self._explorados