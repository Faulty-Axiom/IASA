from typing import List
from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao
from lib.ecr.comportamento import Comportamento

'''
Classe que define um comportamento composto, atuando como um contentor para agregar múltiplos comportamentos
'''
class ComportComp(Comportamento):
    '''
    Método que inicializa o comportamento composto com uma lista de comportamentos dependentes
    '''
    def __init__(self, comportamentos: List[Comportamento]):    
        self._comportamentos = comportamentos

    '''
    Método que processa a perceção, ativa os comportamentos internos e devolve a ação final selecionada
    '''
    def activar(self, percepcao: Percepcao) -> Accao:
        accoes = \
        [
        ]
        
        for comportamento in self._comportamentos:
            accao = comportamento.activar(percepcao)
            if accao is not None:
                accoes.append(accao)
                
        if accoes:
            return self.seleccionar_accao(accoes)
            
        return None

    '''
    Método que avalia e seleciona uma única ação a partir de uma lista de ações propostas pelos comportamentos internos
    '''
    def seleccionar_accao(self, accoes: List[Accao]) -> Accao:
        pass