from typing import List

from jogo.ambiente.comando_jogo import ComandoJogo
from jogo.ambiente.evento_jogo import EventoJogo

'''
Classe que define o ambiente de jogo onde os eventos serão enviados pelo jogador para a personagem
'''
class AmbienteJogo:
    '''
    Método que inicializa o ambiente de jogo com os eventos possíveis
    '''
    def __init__(self):
        self.__eventos = \
        {
            evento.value: evento for evento in EventoJogo
        }
        self.__evento: EventoJogo = None
        
    '''
    Propriedade que devolve o evento atual do ambiente
    '''
    @property
    def evento(self) -> EventoJogo:
        return self.__evento
    
    '''
    Método que faz o ambiente evoluir, gerando e apresentando um novo evento
    '''
    def evoluir(self) -> None:
        self.__evento = self._gerar_evento()
        
        if self.__evento is not None:
            self.__evento.mostrar()

    '''
    Método que permite observar o evento atual no ambiente
    '''
    def observar(self):
        return self.__evento

    '''
    Método que executa e mostra o comando fornecido no ambiente
    '''
    def executar(self, comando: ComandoJogo):
        comando.mostrar()

    '''
    Método que pede o input do jogador
    Retorna o evento escolhido pelo jogador
    '''
    def _gerar_evento(self) -> EventoJogo:
        print("\nEscolha um evento a executar:")
        print("[s - Silêncio, r - Ruído, a - Animal, f - Fuga, o - Fotografia, t - Terminar]")
        text = input("Evento: ")
        return self.__eventos.get(text)