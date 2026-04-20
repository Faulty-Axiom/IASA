from lib.agente.accao import Accao
from lib.agente.controlo import Controlo
from lib.agente.percepcao import Percepcao
from lib.ecr.comportamento import Comportamento

class ControloReact(Controlo):
    def __init__(self, comportamento: Comportamento):
        self.__comportamento = comportamento

    def processar(self, percepcao: Percepcao) -> Accao:
        return self.__comportamento.activar(percepcao)