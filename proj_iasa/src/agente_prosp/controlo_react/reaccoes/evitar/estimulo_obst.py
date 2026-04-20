from lib.agente.percepcao import Percepcao
from lib.ecr.estimulo import Estimulo

'''
Classe que define o estímulo para detetar um obstáculo no ambiente
'''
class EstimuloObst(Estimulo):
    INTENS_OBST = 1.0

    '''
    Método que calcula a intensidade do estímulo com base na deteção de um obstáculo na perceção
    '''
    def detectar(self, percepcao: Percepcao) -> float:
        if percepcao.contacto_obst():
            return self.INTENS_OBST
            
        return 0.0