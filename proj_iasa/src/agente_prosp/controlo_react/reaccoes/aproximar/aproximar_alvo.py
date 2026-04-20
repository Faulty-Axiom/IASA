from lib.ecr.prioridade import Prioridade
from sae import Direccao

from src.agente_prosp.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir

class AproximarAlvo(Prioridade):
    def __init__(self):
        comportamentos = \
        [
            AproximarDir(Direccao.NORTE),
            AproximarDir(Direccao.SUL),
            AproximarDir(Direccao.ESTE),
            AproximarDir(Direccao.OESTE)
        ]
        
        super().__init__(comportamentos)