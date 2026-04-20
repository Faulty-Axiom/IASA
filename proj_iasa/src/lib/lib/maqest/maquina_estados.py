from typing import List, Tuple, TypeVar

EST = TypeVar('EST')
EV = TypeVar('EV')
AC = TypeVar('AC')

'''
Classe que implementa uma máquina de estados
'''
class MaquinaEstados():
    '''
    Método que inicializa a máquina de estados com um estado inicial e um conjunto opcional de transições
    '''
    def __init__(self, estado_inicial, transicoes: List[Tuple] = None):
        self.__estado: EST = estado_inicial
        
        # tte: Mapeia (Estado Atual, Evento) -> Estado Seguinte
        self.__tte = {}
        
        # tae: Mapeia (Estado Atual, Evento) -> Accao
        self.__tae = {}
        
        if transicoes:
            for transicao in transicoes:
                estado_ant, evento, evento_suc, accao = transicao if len(transicao) == 4 else transicao + (None,)
                self.definir_transicao(estado_ant, evento, evento_suc, accao)

    '''
    Propriedade que devolve o estado atual da máquina de estados
    '''
    @property
    def estado(self) -> EST:
        return self.__estado

    '''
    Método que define uma nova transição, mapeando um estado anterior e um evento para um estado sucessor e uma ação opcional
    '''
    def definir_transicao(self, estado_ant: EST, evento: EV, estado_suc: EST, accao: AC = None) -> None:
        self.__tte[(estado_ant, evento)] = estado_suc
        if accao is not None:
            self.__tae[(estado_ant, evento)] = accao

    '''
    Método que processa um evento, atualiza o estado atual se existir uma transição válida, e retorna a ação correspondente
    '''
    def processar(self, evento: EV) -> AC:
        accao = self.__tae.get((self.__estado, evento))
        novo_estado = self.__tte.get((self.__estado, evento))
        if novo_estado is not None:
            self.__estado = novo_estado
        
        return accao