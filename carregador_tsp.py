def carregar_cidades(caminho_arquivo):
    cidades = []
    usar_haversine = "burma14" in caminho_arquivo.lower()
 
    with open(caminho_arquivo, 'r') as arquivo: # Abre o arquivo para leitura
        # Lê o arquivo linha por linha
        # e ignora linhas em branco
        ler_coordenadas = False
        for linha in arquivo:
            linha = linha.strip()
            if linha == "NODE_COORD_SECTION":
                ler_coordenadas = True
                continue
            elif linha == "EOF": # Finaliza a leitura ao encontrar EOF
                break
            if ler_coordenadas:
                partes = linha.split()
                if len(partes) == 3: # Verifica se a linha contém 3 partes
                    # A primeira parte é o índice da cidade (não utilizado)
                    # A segunda e terceira partes são as coordenadas x e y
                    try:
                        x = float(partes[1]) 
                        y = float(partes[2])
                        cidades.append((x, y))
                    except ValueError:
                        continue

    print(f"\nQuantidade de cidades carregadas: {len(cidades)} \n")
    return cidades, usar_haversine
