from math import sqrt

# Usado para calcular a distância entre duas cidades 
def calcular_distancia(cidade1, cidade2):
    return sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

# Usado para calcular a distância total de um caminho entre cidades
def calcular_distancia_total(caminho, cidades):
    distancia = 0
    for i in range(len(caminho)):
        # Calcula a distância entre a cidade atual e a próxima para cada cidade no caminho
        cidade_atual = cidades[caminho[i]]
        cidade_proxima = cidades[caminho[(i + 1) % len(caminho)]]
        distancia += calcular_distancia(cidade_atual, cidade_proxima)
    return distancia