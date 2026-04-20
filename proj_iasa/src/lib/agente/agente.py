from abc import abstractmethod

from lib.agente.accao import Accao
from lib.agente.percepcao import Percepcao
from lib.agente.controlo import Controlo


'''
Classe que define um agente
'''
class Agente:
    '''
    Método que inicializa o agente com o seu respetivo controlo
    '''
    def __init__(self, controlo: Controlo):
        self._controlo = controlo
        
    '''
    Método abstrato que permite ao agente obter uma perceção do ambiente
    '''
    @abstractmethod
    def _percepcionar(self) -> Percepcao:
        pass
    
    '''
    Método abstrato que permite ao agente executar uma dada ação
    '''
    @abstractmethod
    def _actuar(self, accao: Accao):
        pass
    
    '''
    Método que executa uma percepção e uma ação correspondente por parte do agente
    '''
    def executar(self):
        percepcao = self._percepcionar()
        accao = self._controlo.processar(percepcao)
        if accao is not None:
            self._actuar(accao)