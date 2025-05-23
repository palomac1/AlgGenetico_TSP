import time 
from carregador_tsp import carregar_cidades
from algoritmo_genetico import AlgoritmoGenetico
from graficos import plotar_evolucao, plotar_tempos

def testar_instancia(nome_arquivo, nome_instancia): # Função para testar uma instância do TSP 
    cidades, usar_haversine = carregar_cidades(f"dados/{nome_arquivo}")

    ag = AlgoritmoGenetico( # Cria uma instância do Algoritmo Genético
        cidades=cidades, 
        usar_haversine=usar_haversine, 
        tamanho_populacao=200,
        geracoes=500,
        chance_mutacao=0.05,
        chance_crossover=0.8
    )

    melhor_rota, historico_distancias = ag.executar()  # Executa o algoritmo genético e obtém a melhor rota e o histórico de distâncias
    plotar_evolucao(historico_distancias, nome_instancia) # Plota a evolução das distâncias

    distancia = ag.calcular_distancia(melhor_rota) # Calcula a distância da melhor rota
    print(f"Melhor distância encontrada para {nome_instancia}: {distancia:.2f}") # Exibe a melhor distância encontrada
    return distancia

def main():
    print("\n=== Algoritmo Genético para TSP ===")

    # Dicionário de instâncias para testar 
    problemas = {
        "burma14": "burma14.tsp",
        "ch130": "ch130.tsp",
        "pr439": "pr439.tsp"
    }

    tempos_execucao = {}
    resultados = {}

    for nome, arquivo in problemas.items(): # Dicionário com os nomes e arquivos das instâncias
        print(f"\n=== Processando {nome} ===")
        inicio = time.time()


        distancia = testar_instancia(arquivo, nome)
        resultados[nome] = distancia

        # Calcula o tempo de execução
        fim = time.time() 
        tempo = fim - inicio 
        tempos_execucao[nome] = tempo
        print(f"Tempo de execução: {tempo:.2f} segundos")

    print("\n=== Resultados Finais ===")
    for nome, distancia in resultados.items():
        print(f"{nome}: {distancia:.2f} (em {tempos_execucao[nome]:.2f}s)")

    plotar_tempos(tempos_execucao) 

if __name__ == "__main__":
    main()