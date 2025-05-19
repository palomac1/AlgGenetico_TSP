from math import sqrt, radians, sin, cos, asin

def haversine(cidade1, cidade2): # Função para calcular a distância entre duas cidades usando a fórmula de Haversine 
    lon1, lat1 = cidade1
    lon2, lat2 = cidade2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def calcular_distancia(cidade1, cidade2, usar_haversine=False): # Função para calcular a distância entre duas cidades
    if usar_haversine:
        return haversine(cidade1, cidade2)
    return sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

def calcular_distancia_total(caminho, cidades, usar_haversine=False): # Função para calcular a distância total de um caminho
    distancia = 0
    for i in range(len(caminho)):
        cidade_atual = cidades[caminho[i]]
        cidade_proxima = cidades[caminho[(i + 1) % len(caminho)]]
        distancia += calcular_distancia(cidade_atual, cidade_proxima, usar_haversine)
    return distancia
