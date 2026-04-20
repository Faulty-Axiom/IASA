from jogo.agente.agente_jogo import AgenteJogo
from jogo.ambiente.ambiente_jogo import AmbienteJogo
from jogo.personagem.controlo_personagem import ControloPersonagem

'''
Classe que representa a personagem principal do jogo, atuando como um agente
'''
class Personagem(AgenteJogo):
    '''
    Método que inicializa a personagem associando-lhe o ambiente de jogo e instanciando o seu controlo específico
    '''
    def __init__(self, ambiente: AmbienteJogo):
        controlo = ControloPersonagem()
        super().__init__(ambiente, controlo)

    '''
    Método que imprime na consola o estado atual em que a personagem se encontra
    '''
    def mostrar(self) -> None:
        estado = self._controlo.estado
        print(f"Estado: {estado.name}")