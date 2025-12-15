A = [
    [0, 1, 0, 0, 0],  
    [1, 0, 1, 1, 0],  
    [0, 1, 0, 1, 0],  
    [0, 1, 1, 0, 1],  
    [0, 0, 0, 1, 0]   
    ]

# Mapeamento para nomes de cidades (para facilitar a leitura da saída)
nomes_cidades = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E"
}

for i in range(len(A)):
    print("------------------------------------------------------")
    for j in range(len(A)):
        if A[i][j] == 1:
            print(f"{nomes_cidades[i]} está conectado a {nomes_cidades[j]}")
    print("------------------------------------------------------")        


def obter_vizinhos(cidade_indice, matriz_adjacencia):
    """Retorna uma lista de índices dos vizinhos de uma cidade."""
    vizinhos = []
    num_cidades = len(matriz_adjacencia)
    for i in range(num_cidades):
        # Se há uma conexão (valor 1)
        if matriz_adjacencia[cidade_indice][i] == 1:
            vizinhos.append(i)
    return vizinhos




def busca_profundidade(inicio, destino, matriz_adjacencia, nomes_cidades):
    if inicio == destino:
        return [nomes_cidades[inicio]]

    # 1. Fila de nós a serem visitados
    pilha = [[inicio]]

    # 2. Conjunto de nós já visitados para evitar ciclos e reprocessamento
    visitados = {inicio}

    while pilha:
        caminho_atual = pilha.pop() 
        no_atual = caminho_atual[-1] #o ultimo elemento de 

        for vizinho in obter_vizinhos(no_atual, matriz_adjacencia):
            if vizinho not in visitados:
                #anota tal caminho ainda não percorrido
                caminho_percorrido = list(caminho_atual)
                caminho_percorrido.append(vizinho)

                # Se o vizinho é o destino, finaliza
                if vizinho == destino:
                    # Mapeia os índices para nomes de cidades antes de retornar
                    return [nomes_cidades[c] for c in caminho_percorrido]

                # Marca como visitado e adiciona à pilha para exploração futura
                visitados.add(vizinho)
                pilha.append(caminho_percorrido)

    # Se a pilha esvaziar e o destino não for encontrado
    return None

# Cidades de teste: A (0) -> E (4)
inicio_teste = int(input("Digite numero da cidade que a encomenda irá sair: "))
destino_teste = int(input("Digite o número da cidade que irá receber a encomenda: "))

print(f"--- Busca em Largura (DFS) de {nomes_cidades[inicio_teste]} para {nomes_cidades[destino_teste]} ---")
caminho_bfs = busca_profundidade(inicio_teste, destino_teste, A, nomes_cidades)

if caminho_bfs:
    print(f" Caminho DFS encontrado (o mais curto): {' -> '.join(caminho_bfs)}")
else:
    print(" Nenhum caminho encontrado por DFS.")



