import random
from utils import calcular_distancia_total

class AlgoritmoGeneticoTSP:
    def __init__(self, cidades, tamanho_populacao, geracoes, taxa_mutacao, taxa_crossover):
        self.cidades = cidades
        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover

    def inicializar_populacao(self):
        # Gera uma lista de índices das cidades
        num_cidades = len(self.cidades)
        return [random.sample(range(num_cidades), num_cidades) for _ in range(self.tamanho_populacao)]

    def avaliar_fitness(self, cromossomo):
        return calcular_distancia_total(cromossomo, self.cidades)

    def selecao_por_torneio(self, populacao):
        torneio = random.sample(populacao, 5)
        return min(torneio, key=self.avaliar_fitness)

    def crossover(self, pai1, pai2):
        tamanho = len(pai1)
        inicio, fim = sorted(random.sample(range(tamanho), 2))
        filho = [-1] * tamanho
        filho[inicio:fim] = pai1[inicio:fim]

        ponteiro = 0
        for gene in pai2:
            if gene not in filho:
                while filho[ponteiro] != -1:
                    ponteiro += 1
                filho[ponteiro] = gene
        return filho

    def mutar(self, cromossomo):
        i, j = random.sample(range(len(cromossomo)), 2)
        cromossomo[i], cromossomo[j] = cromossomo[j], cromossomo[i]

    def evoluir(self):
        populacao = self.inicializar_populacao()
        melhores_distancias = []

        for _ in range(self.geracoes):
            nova_populacao = []
            for _ in range(self.tamanho_populacao):
                pai1 = self.selecao_por_torneio(populacao)
                pai2 = self.selecao_por_torneio(populacao)

                if random.random() < self.taxa_crossover:
                    filho = self.crossover(pai1, pai2)
                else:
                    filho = pai1.copy()

                if random.random() < self.taxa_mutacao:
                    self.mutar(filho)

                nova_populacao.append(filho)

            populacao = nova_populacao
            melhor_atual = min(populacao, key=self.avaliar_fitness)
            melhores_distancias.append(self.avaliar_fitness(melhor_atual))

        melhor_solucao = min(populacao, key=self.avaliar_fitness)
        return melhor_solucao, melhores_distancias