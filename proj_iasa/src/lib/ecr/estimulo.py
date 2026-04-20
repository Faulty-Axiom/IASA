from abc import ABC, abstractmethod
from lib.agente.percepcao import Percepcao

class Estimulo(ABC):
    @abstractmethod
    def detectar(self, percepcao: Percepcao) -> float:
        pass