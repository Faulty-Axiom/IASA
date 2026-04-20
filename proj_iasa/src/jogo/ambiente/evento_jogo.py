from enum import Enum

'''
Classe que representa os eventos possíveis que podem existir no jogo
'''

class EventoJogo(Enum):
    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'o'
    TERMINAR = 't'

    '''
    Método que mostra na consola o evento que foi selecionado
    '''
    def mostrar(self) -> None:
        print(f"\nEvento: {self.name}")