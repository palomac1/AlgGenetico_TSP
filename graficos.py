import matplotlib.pyplot as plt

#Faz o import do matplotlib para plotar os gráficos e do numpy para manipulação de arrays, assim como o time para calcular o tempo de execução
def plotar_evolucao(distancias, nome_instancia):
    """Plota o gráfico de evolução das distâncias"""
    plt.figure(figsize=(10, 5))
    plt.plot(distancias, 'b-', linewidth=1)
    plt.title(f"Evolução da Distância - {nome_instancia}")
    plt.xlabel("Geração")
    plt.ylabel("Distância da Melhor Rota")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(f"{nome_instancia}_evolucao.png")
    plt.close()
    
def plotar_tempos(tempos):
    """Plota o gráfico de tempos de execução"""
    nomes = list(tempos.keys())
    valores = list(tempos.values())

    # Ordena os tempos de execução
    plt.figure(figsize=(10, 5))
    plt.bar(nomes, valores, color=['blue', 'green', 'red'])
    plt.title("Tempo de Execução por Instância")
    plt.xlabel("Instância TSP")
    plt.ylabel("Tempo (segundos)")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Adiciona os valores em cima das barras
    for i, v in enumerate(valores):
        plt.text(i, v + 0.1, f"{v:.2f}s", ha='center')
    plt.tight_layout()
    plt.savefig("tempos_execucao.png")
    plt.close()
