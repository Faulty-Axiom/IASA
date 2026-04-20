from enum import Enum, auto

'''
Enumeração que define os possíveis estados da personagem durante a execução do jogo
'''
class EstadoPersonagem(Enum):
    PROCURA = auto()
    INSPECCAO = auto()
    OBSERVACAO = auto()
    REGISTO = auto()