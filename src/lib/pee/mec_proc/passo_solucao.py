from pee.mod.estado import Estado
from pee.mod.operador import Operador

'''
Classe que representa um passo individual dentro de uma solução encontrada
'''
class PassoSolucao:
    '''
    Método que inicializa um passo com o respetivo estado e o operador que lhe deu origem
    '''
    def __init__(self, estado: Estado, operador: Operador):
        self._estado = estado
        self._operador = operador

    '''
    Propriedade de leitura que devolve o estado associado a este passo
    '''
    @property
    def estado(self) -> Estado:
        return self._estado

    '''
    Propriedade de leitura que devolve o operador associado a este passo
    '''
    @property
    def operador(self) -> Operador:
        return self._operador