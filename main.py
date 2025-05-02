import time
from carregador_tsp import carregar_arquivo_tsp
from algoritmo_genetico import AlgoritmoGeneticoTSP
from graficos import plotar_distancias, plotar_tempos_execucao

def testar_instancia(nome_arquivo, nome_instancia):
    cidades = carregar_arquivo_tsp(f"dados/{nome_arquivo}")
    ag = AlgoritmoGeneticoTSP(
        cidades=cidades,
        tamanho_populacao=100,
        geracoes=500,
        taxa_mutacao=0.02,
        taxa_crossover=0.9
    )
    melhor_rota, distancias = ag.evoluir()
    plotar_distancias(distancias, nome_instancia)
    return ag.avaliar_fitness(melhor_rota)

def main():
    instancias = {
        "burma14": "burma14.tsp",
        "ch130": "ch130.tsp",
        "pr439": "pr439.tsp"
    }

    tempos = {}

    for nome, arquivo in instancias.items():
        print(f"Testando instância: {nome}")
        inicio = time.time()
        melhor_distancia = testar_instancia(arquivo, nome)
        fim = time.time()
        tempos[nome] = fim - inicio
        print(f"{nome} - Melhor distância encontrada: {melhor_distancia:.2f}\n")

    plotar_tempos_execucao(tempos)

if __name__ == "__main__":
    main()
