from pee.mec_proc.fronteira import Fronteira
from pee.mec_proc.no import No

'''
Classe que implementa uma fronteira de exploração com política FIFO (First-In, First-Out)
'''
class FronteiraFIFO(Fronteira):
    '''
    Método que insere um nó no final da fronteira (comportamento de fila)
    '''
    def inserir(self, no: No) -> None:
        self._nos.append(no)