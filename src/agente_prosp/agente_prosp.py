from agente.controlo import Controlo
from lib.agente.accao import Accao
from lib.agente.agente import Agente
from lib.agente.percepcao import Percepcao
from sae.agente.transdutor import Transdutor

'''
Classe que implementa o agente prospetor responsável por interagir com o ambiente de simulação
'''
class AgenteProsp(Agente):
    
    '''
    Método que recolhe a perceção atual do ambiente através do transdutor
    '''
    def _percepcionar(self) -> Percepcao:
        transdutor = Transdutor(self.ambiente)
        return transdutor.percepcionar()
        
    '''
    Método que recebe uma ação do controlo reativo e a executa no ambiente
    '''
    def _actuar(self, accao: Accao):
        if accao is not None:
            transdutor = Transdutor(self.ambiente)
            
            if hasattr(accao, 'obter_movimento'):
                movimento = accao.obter_movimento()
                transdutor.actuar(movimento)
            else:
                transdutor.actuar(accao)