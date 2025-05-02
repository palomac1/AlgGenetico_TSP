import matplotlib.pyplot as plt

def plotar_distancias(distancias, nome_instancia):
    plt.plot(distancias)
    plt.title(f"Evolução da Distância - {nome_instancia}")
    plt.xlabel("Geração")
    plt.ylabel("Distância")
    plt.grid(True)
    plt.savefig(f"{nome_instancia}_evolucao.png")
    plt.close()

def list(param):
    pass

def plotar_tempos_execucao(tempos):
    instancias = list(tempos.keys())
    tempos = list(tempos.values())
    plt.bar(instancias, tempos)
    plt.title("Tempo de Execução por Instância")
    plt.xlabel("Instância")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.savefig("tempos_execucao.png")
    plt.close()