from lib.ecr.hierarquia import Hierarquia
from src.agente_prosp.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from src.agente_prosp.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from src.agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar

'''
Classe que executa o processo de recolha através de comportamentos ordenados hierarquicamente
'''
class Recolher(Hierarquia):
    '''
    Método que inicializa o comportamento de recolha, instanciando e ordenando as reações por nível de competência
    '''
    def __init__(self):
        comportamentos = \
        [
            AproximarAlvo(),
            EvitarObst(),
            Explorar()
        ]
        
        super().__init__(comportamentos)