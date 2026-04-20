from enum import Enum

'''
Classe que representa as ações a serem executadas pela personagem
'''

class ComandoJogo(Enum):
    PROCURAR = 1
    APROXIMAR = 2
    OBSERVAR = 3
    FOTOGRAFAR = 4

    '''
    Método que mostra na consola o evento que foi selecionado
    '''
    def mostrar(self) -> None:
        print(f"Ação: {self.name}")