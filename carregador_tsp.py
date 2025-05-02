def carregar_cidades(caminho_arquivo):
    """Carrega as coordenadas das cidades de um arquivo TSP"""
    cidades = []

    with open(caminho_arquivo, 'r') as arquivo:
        ler_coordenadas = False

        for linha in arquivo:
            linha = linha.strip()

            if linha == "NODE_COORD_SECTION": # Início da seção de coordenadas para leitura
                ler_coordenadas = True
                continue
            elif linha == "EOF":
                break

            if ler_coordenadas:
                partes = linha.split()
                if len(partes) == 3:  # ID, X, Y (ID é ignorado pois não é necessário)
                    # Ignora o ID da cidade (partes[0]) e tenta converter as coordenadas X e Y para float
                    # Se falhar, ignora a linha e continua com a próxima
                    try:
                        x = float(partes[1])
                        y = float(partes[2])
                        cidades.append((x, y))
                    except ValueError:
                        continue

    print(f"\nQuantidade de cidades carregadas: {len(cidades)} \n")
    return cidades