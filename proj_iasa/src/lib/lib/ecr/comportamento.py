from abc import ABC, abstractmethod
from lib.agente.percepcao import Percepcao
from lib.ecr.accao import Accao

class Comportamento(ABC):
    @abstractmethod
    def activar(self, percepcao: Percepcao) -> Accao:
        pass