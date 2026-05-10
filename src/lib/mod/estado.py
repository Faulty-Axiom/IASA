from abc import ABC, abstractmethod

'''
Classe abstrata que representa um estado no espaço do problema, garantindo a sua identificação única
'''
class Estado(ABC):
    '''
    Método abstrato que devolve o valor de identificação única do estado
    '''
    @abstractmethod
    def id_valor(self) -> int:
        pass

    '''
    Método que garante que o estado atua como um elemento "hashable", utilizando o seu id_valor
    '''
    def __hash__(self) -> int:
        return hash(self.id_valor())

    '''
    Método que permite a comparação de igualdade entre estados através do seu id_valor
    '''
    def __eq__(self, outro: object) -> bool:
        if isinstance(outro, Estado):
            return self.id_valor() == outro.id_valor()
        return False