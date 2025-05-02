def carregar_arquivo_tsp(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        secao_coordenadas = False
        cidades = []

        for linha in linhas:
            if "NODE_COORD_SECTION" in linha:
                secao_coordenadas = True
                continue
            if secao_coordenadas:
                if "EOF" in linha:
                    break
                partes = linha.strip().split()
                if len(partes) == 3:
                    cidades.append((float(partes[1]), float(partes[2])))
        return cidades