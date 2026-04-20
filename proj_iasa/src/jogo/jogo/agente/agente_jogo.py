from lib.agente.accao import Accao
from lib.agente.agente import Agente
from lib.agente.controlo import Controlo
from lib.agente.percepcao import Percepcao
from jogo.agente.percepcao_jogo import PercepcaoJogo
from jogo.ambiente.ambiente_jogo import AmbienteJogo

'''
Classe que implementa um agente de jogo
'''
class AgenteJogo(Agente):
    '''
    Método que inicializa o agente de jogo com o respetivo ambiente e controlo
    '''
    def __init__(self, ambiente: AmbienteJogo, controlo: Controlo):
        super().__init__(controlo)
        self.__ambiente = ambiente
        
    '''
    Método que observa o ambiente atual e devolve a perceção de jogo correspondente
    '''
    def _percepcionar(self) -> Percepcao:
        evento = self.__ambiente.observar()
        return PercepcaoJogo(evento)
    
    '''
    Método que executa o comando associado à ação fornecida no ambiente de jogo
    '''
    def _actuar(self, accao: Accao) -> None:
        if accao is not None:
            comando = accao.comando
            self.__ambiente.executar(comando)