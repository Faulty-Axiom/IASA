from lib.sae.simulador import Simulador

from agente_prosp.agente_prosp import AgenteProsp
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.recolher.recolher import Recolher

def main():
    '''
    Função que inicializa a hierarquia de comportamentos, o controlo, o agente e o simulador
    '''
    # 1. Definir o comportamento de topo (Hierarquia Recolher)
    comportamento = Recolher()
    
    # 2. Injetar o comportamento no controlo reativo
    controlo = ControloReact(comportamento)
    
    # 3. Criar o agente com o controlo configurado
    agente = AgenteProsp(controlo)
    
    # 4. Inicializar o simulador (o primeiro argumento é o número do ambiente, ex: 1)
    simulador = Simulador(1, agente)
    
    # 5. Iniciar o ciclo de execução do simulador
    simulador.executar()

if __name__ == '__main__':
    main()