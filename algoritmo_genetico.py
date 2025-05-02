import random
import math

# Algoritmo Genético para o Problema do Caixeiro Viajante (TSP)
class AlgoritmoGenetico:
    def __init__(self, cidades, tamanho_populacao=50, geracoes=100,
                 chance_mutacao=0.05, chance_crossover=0.8):
        self.cidades = cidades # Lista de coordenadas (x, y) das cidades
        self.tamanho_pop = tamanho_populacao # Tamanho da população
        self.max_geracoes = geracoes # Número máximo de gerações
        self.chance_mutacao = chance_mutacao # Probabilidade de mutação
        self.chance_crossover = chance_crossover # Probabilidade de crossover

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
        return random.sample(range(len(self.cidades)), len(self.cidades)) # Permutação aleatória das cidades para criar uma rota

    def criar_populacao(self):
        """Cria a população inicial"""
        return [self.criar_individuo() for _ in range(self.tamanho_pop)] # Lista de indivíduos (rotas)

    def selecionar_pai(self, populacao):
        """Seleção por torneio simples"""
        participantes = random.sample(populacao, 3)  # Torneio com 3 participantes por vez
        return min(participantes, key=self.calcular_distancia)

    def cruzar(self, pai1, pai2):
        """Crossover PMX (Partially Mapped Crossover)""" # Crossover parcialmente mapeado para preservar a ordem dos genes
        if random.random() > self.chance_crossover: # Verifica se o crossover deve ser realizado, se não, retorna o pai1
            return pai1.copy()  # Sem crossover

        tamanho = len(pai1) # Seleciona o tamanho do pai para o crossover
        ponto1, ponto2 = sorted(random.sample(range(tamanho), 2)) # Seleciona dois pontos de crossover aleatórios para o PMX

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
        """Mutação por swap de duas cidades""" # Troca aleatória de duas cidades na rota
        # Verifica se a mutação deve ser realizada
        if random.random() < self.chance_mutacao:
            i, j = random.sample(range(len(individuo)), 2)
            individuo[i], individuo[j] = individuo[j], individuo[i]

    def executar(self): 
        """Executa o algoritmo genético""" # Inicializa a população e o histórico de distâncias a medida que as gerações são processadas
        # Inicializa a população e o histórico de distâncias
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