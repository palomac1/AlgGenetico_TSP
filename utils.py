from math import sqrt

def calcular_distancia(cidade1, cidade2):
    return sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

def calcular_distancia_total(caminho, cidades):
    distancia = 0
    for i in range(len(caminho)):
        # Certifique-se de que caminho[i] é um índice inteiro
        cidade_atual = cidades[caminho[i]]
        cidade_proxima = cidades[caminho[(i + 1) % len(caminho)]]
        distancia += calcular_distancia(cidade_atual, cidade_proxima)
    return distancia