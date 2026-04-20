from lib.agente.percepcao import Percepcao
from jogo.ambiente.evento_jogo import EventoJogo

'''
Classe que implementa uma perceção
'''

class PercepcaoJogo(Percepcao):
    
    def __init__(self, evento):
        self._evento = evento
    
    @property
    def evento(self) -> EventoJogo:
        return self._evento