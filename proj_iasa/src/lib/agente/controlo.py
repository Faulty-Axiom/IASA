from abc import ABC, abstractmethod

from lib.agente.agente import Accao, Percepcao

'''
Classe abstrata que define o controlo da personagem
'''
class Controlo(ABC):
    @abstractmethod
    def processar(self, percepcao: Percepcao) -> Accao:
        pass