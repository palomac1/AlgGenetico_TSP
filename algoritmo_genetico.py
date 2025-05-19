
import random
from utils import  calcular_distancia
import math

class AlgoritmoGenetico:
    def __init__(self, cidades, usar_haversine=False, tamanho_populacao=200, geracoes=500,
                 chance_mutacao=0.05, chance_crossover=0.8):
        self.cidades = cidades
        self.usar_haversine = usar_haversine
        self.tamanho_pop = tamanho_populacao
        self.max_geracoes = geracoes
        self.chance_mutacao = chance_mutacao
        self.chance_crossover = chance_crossover

    def calcular_distancia(self, rota):
        distancia = 0
        for i in range(len(rota)):
            cidade_atual = self.cidades[rota[i]]
            proxima_cidade = self.cidades[rota[(i + 1) % len(rota)]]
            distancia += calcular_distancia(cidade_atual, proxima_cidade, self.usar_haversine)
        return distancia

    def criar_individuo(self): # Função para criar um indivíduo aleatório
        # Um indivíduo é representado por uma lista de índices que representam a ordem das cidades
        # A função random.sample garante que as cidades não se repitam 
        return random.sample(range(len(self.cidades)), len(self.cidades))

    def criar_populacao(self): # Função para criar a população inicial
        # A população é uma lista de indivíduos, onde cada indivíduo é uma permutação aleatória das cidades
        return [self.criar_individuo() for _ in range(self.tamanho_pop)]

    def selecionar_pai(self, populacao): # Função para selecionar um pai usando torneio
        # Seleciona aleatoriamente 3 indivíduos da população e retorna o de menor distância
        participantes = random.sample(populacao, 3)
        return min(participantes, key=self.calcular_distancia)

    def cruzar(self, pai1, pai2): # Função para cruzar dois pais e gerar um filho
        # O cruzamento é feito com base na chance de crossover definida
        # Se o crossover não ocorrer, retorna uma cópia do pai1
        # Isso garante que a diversidade genética seja mantida na população
        if random.random() > self.chance_crossover:
            return pai1.copy()

        # Order Crossover (OX)
        tamanho = len(pai1)
        filho = [-1] * tamanho
        ponto1, ponto2 = sorted(random.sample(range(tamanho), 2))
        filho[ponto1:ponto2] = pai1[ponto1:ponto2]

        preenchidos = set(filho[ponto1:ponto2]) # Cidades já preenchidas
        # Preenche o restante do filho com genes do pai2, mantendo a ordem relativa e evitando duplicatas
        pos = ponto2 % tamanho
        for i in range(tamanho):
            gene = pai2[(ponto2 + i) % tamanho]
            if gene not in preenchidos:
                filho[pos] = gene
                pos = (pos + 1) % tamanho
        return filho

    def mutar(self, individuo, geracao_atual=None): # Função para mutar um indivíduo
        # A taxa de mutação aumenta com o número de gerações, isso ajuda a evitar a convergência prematura e permite uma exploração mais ampla do espaço de busca
        # A taxa de mutação é limitada a 0.3 para evitar mutações excessivas e garantir que a população não se torne homogênea
        taxa = self.chance_mutacao + (geracao_atual or 0) * 0.0002
        taxa = min(taxa, 0.3)
        if random.random() < taxa:
            i, j = random.sample(range(len(individuo)), 2)
            individuo[i], individuo[j] = individuo[j], individuo[i]

    def executar(self): # Função principal que executa o algoritmo genético
        # Inicializa a população com indivíduos aleatórios, onde cada indivíduo é uma permutação aleatória das cidades
        # A população é uma lista de indivíduos, onde cada indivíduo é representado por uma lista de índices que representam a ordem das cidades
        populacao = self.criar_populacao()
        historico = []

        for geracao in range(self.max_geracoes): # Loop principal do algoritmo
            # Seleciona o melhor indivíduo da população atual
            melhor_atual = min(populacao, key=self.calcular_distancia)
            distancia = self.calcular_distancia(melhor_atual)
            historico.append(distancia)

            nova_populacao = []
            for _ in range(self.tamanho_pop): # Cria nova população
                # Seleciona dois pais e cria um filho através do cruzamento
                # O cruzamento é feito com base na chance de crossover definida
                # A mutação é aplicada ao filho com base na chance de mutação
                pai1 = self.selecionar_pai(populacao)
                pai2 = self.selecionar_pai(populacao)
                filho = self.cruzar(pai1, pai2)
                self.mutar(filho, geracao)
                nova_populacao.append(filho)

            # Elitismo: substitui primeiro indivíduo pelo melhor da geração anterior
            nova_populacao[0] = melhor_atual
            populacao = nova_populacao

            if geracao % 10 == 0: # Imprime o progresso a cada 10 gerações 
                print(f"Geração {geracao}: ")
                print(f"Melhor distância = {distancia:.2f}\n")

        melhor_final = min(populacao, key=self.calcular_distancia) # Melhor indivíduo da última geração
        return melhor_final, historico
