from lib.agente.accao import Accao
from jogo.ambiente.comando_jogo import ComandoJogo

'''
Classe que implementa uma ação 
Representa a ação tomada pela personagem após receber um comando
'''
class AccaoJogo(Accao):
    def __init__(self, comando: ComandoJogo):
        self._comando = comando
        
    @property
    def comando(self) -> ComandoJogo:
        return self._comando