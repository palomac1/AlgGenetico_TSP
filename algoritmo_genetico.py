import random
import math

class AlgoritmoGenetico:
    def __init__(self, cidades, tamanho_populacao=50, geracoes=100,
                 chance_mutacao=0.05, chance_crossover=0.8):
        self.cidades = cidades
        self.tamanho_pop = tamanho_populacao
        self.max_geracoes = geracoes
        self.chance_mutacao = chance_mutacao
        self.chance_crossover = chance_crossover

    def calcular_distancia(self, rota):
        """Calcula a distância total de uma rota"""
        distancia = 0
        for i in range(len(rota)):
            cidade_atual = self.cidades[rota[i]]
            proxima_cidade = self.cidades[rota[(i + 1) % len(rota)]]
            dx = cidade_atual[0] - proxima_cidade[0]
            dy = cidade_atual[1] - proxima_cidade[1]
            distancia += math.sqrt(dx*dx + dy*dy)
        return distancia

    def criar_individuo(self):
        """Cria um indivíduo (rota) aleatório"""
        return random.sample(range(len(self.cidades)), len(self.cidades))

    def criar_populacao(self):
        """Cria a população inicial"""
        return [self.criar_individuo() for _ in range(self.tamanho_pop)]

    def selecionar_pai(self, populacao):
        """Seleção por torneio simples"""
        participantes = random.sample(populacao, 3)  # Torneio com 3 participantes
        return min(participantes, key=self.calcular_distancia)

    def cruzar(self, pai1, pai2):
        """Crossover PMX (Partially Mapped Crossover)"""
        if random.random() > self.chance_crossover:
            return pai1.copy()  # Sem crossover

        tamanho = len(pai1)
        ponto1, ponto2 = sorted(random.sample(range(tamanho), 2))

        # Cria filho com segmento do pai1
        filho = [-1] * tamanho
        filho[ponto1:ponto2] = pai1[ponto1:ponto2]

        # Preenche o resto com genes do pai2
        for i in list(range(0, ponto1)) + list(range(ponto2, tamanho)):
            if pai2[i] not in filho:
                filho[i] = pai2[i]

        # Preenche os genes faltantes
        for i in range(tamanho):
            if filho[i] == -1:
                for gene in pai2:
                    if gene not in filho:
                        filho[i] = gene
                        break

        return filho

    def mutar(self, individuo):
        """Mutação por swap de duas cidades"""
        if random.random() < self.chance_mutacao:
            i, j = random.sample(range(len(individuo)), 2)
            individuo[i], individuo[j] = individuo[j], individuo[i]

    def executar(self):
        """Executa o algoritmo genético"""
        populacao = self.criar_populacao()
        historico = []

        for geracao in range(self.max_geracoes):
            # Avalia a população
            melhor_atual = min(populacao, key=self.calcular_distancia)
            distancia = self.calcular_distancia(melhor_atual)
            historico.append(distancia)

            # Cria nova população
            nova_populacao = []
            for _ in range(self.tamanho_pop):
                pai1 = self.selecionar_pai(populacao)
                pai2 = self.selecionar_pai(populacao)
                filho = self.cruzar(pai1, pai2)
                self.mutar(filho)
                nova_populacao.append(filho)

            populacao = nova_populacao

            # Mostra progresso a cada 10 gerações
            if geracao % 10 == 0:
                print(f"Geração {geracao}: ")
                print(f"Melhor distância = {distancia:.2f}\n")

        melhor_final = min(populacao, key=self.calcular_distancia)
        return melhor_final, historico