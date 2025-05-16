
import random
import math

class AlgoritmoGenetico:
    def __init__(self, cidades, tamanho_populacao=200, geracoes=500,
                 chance_mutacao=0.05, chance_crossover=0.8):
        self.cidades = cidades
        self.tamanho_pop = tamanho_populacao
        self.max_geracoes = geracoes
        self.chance_mutacao = chance_mutacao
        self.chance_crossover = chance_crossover

    def calcular_distancia(self, rota):
        distancia = 0
        for i in range(len(rota)):
            cidade_atual = self.cidades[rota[i]]
            proxima_cidade = self.cidades[rota[(i + 1) % len(rota)]]
            dx = cidade_atual[0] - proxima_cidade[0]
            dy = cidade_atual[1] - proxima_cidade[1]
            distancia += math.sqrt(dx*dx + dy*dy)
        return distancia

    def criar_individuo(self):
        return random.sample(range(len(self.cidades)), len(self.cidades))

    def criar_populacao(self):
        return [self.criar_individuo() for _ in range(self.tamanho_pop)]

    def selecionar_pai(self, populacao):
        participantes = random.sample(populacao, 3)
        return min(participantes, key=self.calcular_distancia)

    def cruzar(self, pai1, pai2):
        if random.random() > self.chance_crossover:
            return pai1.copy()

        # Order Crossover (OX)
        tamanho = len(pai1)
        filho = [-1] * tamanho
        ponto1, ponto2 = sorted(random.sample(range(tamanho), 2))
        filho[ponto1:ponto2] = pai1[ponto1:ponto2]

        preenchidos = set(filho[ponto1:ponto2])
        pos = ponto2 % tamanho
        for i in range(tamanho):
            gene = pai2[(ponto2 + i) % tamanho]
            if gene not in preenchidos:
                filho[pos] = gene
                pos = (pos + 1) % tamanho
        return filho

    def mutar(self, individuo, geracao_atual=None):
        taxa = self.chance_mutacao + (geracao_atual or 0) * 0.0002
        taxa = min(taxa, 0.3)
        if random.random() < taxa:
            i, j = random.sample(range(len(individuo)), 2)
            individuo[i], individuo[j] = individuo[j], individuo[i]

    def executar(self):
        populacao = self.criar_populacao()
        historico = []

        for geracao in range(self.max_geracoes):
            melhor_atual = min(populacao, key=self.calcular_distancia)
            distancia = self.calcular_distancia(melhor_atual)
            historico.append(distancia)

            nova_populacao = []
            for _ in range(self.tamanho_pop):
                pai1 = self.selecionar_pai(populacao)
                pai2 = self.selecionar_pai(populacao)
                filho = self.cruzar(pai1, pai2)
                self.mutar(filho, geracao)
                nova_populacao.append(filho)

            # Elitismo: substitui primeiro indivíduo pelo melhor da geração anterior
            nova_populacao[0] = melhor_atual
            populacao = nova_populacao

            if geracao % 10 == 0:
                print(f"Geração {geracao}: ")
                print(f"Melhor distância = {distancia:.2f}\n")

        melhor_final = min(populacao, key=self.calcular_distancia)
        return melhor_final, historico
