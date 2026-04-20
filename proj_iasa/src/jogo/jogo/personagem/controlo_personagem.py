from lib.agente.accao import Accao
from lib.agente.controlo import Controlo
from lib.agente.percepcao import Percepcao
from jogo.agente.accao_jogo import AccaoJogo
from jogo.ambiente.comando_jogo import ComandoJogo
from jogo.ambiente.evento_jogo import EventoJogo
from jogo.personagem.estado_personagem import EstadoPersonagem
from lib.maqest.maquina_estados import MaquinaEstados

'''
Classe que implementa o controlo da personagem através de uma máquina de estados
'''
class ControloPersonagem(Controlo):
    '''
    Método que inicializa o controlo da personagem, definindo as ações possíveis, as transições e instanciando a máquina de estados
    '''
    def __init__(self):
        procurar = AccaoJogo(ComandoJogo.PROCURAR)
        aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        observar = AccaoJogo(ComandoJogo.OBSERVAR)
        fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)

        transicoes = \
        [
            # Transições a partir do estado PROCURA
            (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, aproximar),
            (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, procurar),
            (EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),

            # Transições a partir do estado INSPECCAO
            (EstadoPersonagem.INSPECCAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, None),
            (EstadoPersonagem.INSPECCAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, procurar),
            (EstadoPersonagem.INSPECCAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),

            # Transições a partir do estado OBSERVACAO
            (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, observar),
            (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECCAO, None),

            # Transições a partir do estado REGISTO
            (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA, None),
            (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA, None),
            (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, fotografar)
        ]
        
        self._maq_est: MaquinaEstados = MaquinaEstados(EstadoPersonagem.PROCURA, transicoes)
        
    '''
    Propriedade que devolve o estado atual da máquina de estados da personagem
    '''
    @property
    def estado(self) -> EstadoPersonagem:
        return self._maq_est.estado
        
    '''
    Método que processa uma perceção, atualiza a máquina de estados com o evento recebido e retorna a ação resultante
    '''
    def processar(self, percepcao: Percepcao) -> Accao:
        evento = percepcao.evento
        
        accao = self._maq_est.processar(evento)
        
        return accao