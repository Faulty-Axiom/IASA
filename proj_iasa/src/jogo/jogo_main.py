from jogo.ambiente.ambiente_jogo import AmbienteJogo
from jogo.ambiente.evento_jogo import EventoJogo
from jogo.personagem.personagem import Personagem

'''
Classe principal que inicializa e executa o ciclo de vida do jogo
'''
class Jogo:
    '''
    Método que inicializa o jogo, instanciando o ambiente e a personagem principal
    '''
    def __init__(self):
        self._ambiente = AmbienteJogo()
        self._personagem = Personagem(self._ambiente)

    '''
    Método que contém o ciclo principal do jogo, atualizando o ambiente e a personagem até que o evento terminar seja detetado
    '''
    def executar(self) -> None:
        self._personagem.mostrar()
        
        while self._ambiente.observar() != EventoJogo.TERMINAR:
            self._ambiente.evoluir()
            self._personagem.executar()
            self._personagem.mostrar()

    '''
    Método estático que serve para iniciar a execução do jogo
    '''
    @staticmethod
    def main() -> None:
        jogo = Jogo()
        jogo.executar()

if __name__ == '__main__':
    Jogo.main()