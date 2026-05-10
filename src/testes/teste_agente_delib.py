from lib.mod.problema import Problema
from lib.mod.estado import Estado
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

'''
Script principal para testar os mecanismos de procura da Parte 3
'''
def main():
    # 1. Instanciar o estado inicial e o problema (requer classes concretas no futuro)
    # estado_inicial = MeuEstadoConcreto(...)
    # problema = MeuProblemaConcreto(estado_inicial, operadores)
    
    # 2. Escolher o mecanismo de procura pretendido
    # mecanismo = ProcuraProfundidade()
    # mecanismo = ProcuraLargura()
    # mecanismo = ProcuraCustoUnif()
    mecanismo = ProcuraAA()
    
    # 3. Executar a procura (para procuras informadas, injetar a heurística)
    # heuristica = MinhaHeuristicaConcreta()
    # solucao = mecanismo.procurar(problema, heuristica)
    
    # Exemplo genérico sem heurística para testes iniciais
    # solucao = mecanismo.procurar(problema)
    
    # 4. Avaliar a solução encontrada
    '''
    if solucao is not None:
        print(f"Solução encontrada com dimensão: {solucao.dimensao} e custo: {solucao.custo}")
        for passo in solucao:
            print(f"Operador: {passo.operador}, Estado Resultante: {passo.estado.id_valor()}")
    else:
        print("Nenhuma solução foi encontrada.")
    '''
    pass

if __name__ == '__main__':
    main()