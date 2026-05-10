from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No

'''
Classe que implementa uma fronteira de exploração com política LIFO (Last-In, First-Out)
'''
class FronteiraLIFO(Fronteira):
    '''
    Método que insere um nó no início da fronteira (comportamento de pilha)
    '''
    def inserir(self, no: No) -> None:
        self._nos.insert(0, no)