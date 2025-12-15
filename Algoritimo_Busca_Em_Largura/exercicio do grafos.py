

#Aqui temos uma matriz que representa as conexões de um grafo.
#Caso exista valor 1 quer dizer que a uma conexão com o proximo nivel.
A = [#A B  C  D  E
    [0, 1, 0, 0, 0],#A  
    [1, 0, 1, 1, 0],#B 
    [0, 1, 0, 1, 0],#C 
    [0, 1, 1, 0, 1],#D  
    [0, 0, 0, 1, 0] #E 
    ]

# Aqui cada indice representa uma letra, poderiam ser cidades também.
nomes_cidades = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E"
}

def obter_vizinhos(cidade_indice, matriz_adjacencia):
    """Usamos essa função para achar vizinhos do nivel, por exemplo o vizinho de 0(A) é apenas o 1(B)"""
    vizinhos = []
    num_cidades = len(matriz_adjacencia)
    for i in range(num_cidades):
        # Se existir um vizinho ele é adicionado na lista de viznhos
        if matriz_adjacencia[cidade_indice][i] == 1:
            vizinhos.append(i)
    return vizinhos



from collections import deque

def busca_largura(inicio, destino, matriz_adjacencia, nomes_cidades):
    if inicio == destino:
        return [nomes_cidades[inicio]]

    # 1. Fila de nós a serem visitados
    fila = deque([[inicio]])

    # 2. Conjunto de nós já visitados para evitar ciclos e reprocessamento
    visitados = {inicio}

    while fila:
        print(fila)
        caminho_atual = fila.popleft() #popleft toma o primeiro e retrona uma lista
        print(caminho_atual)
        no_atual = caminho_atual[-1] #o ultimo elemento
        

        for vizinho in obter_vizinhos(no_atual, matriz_adjacencia):
            if vizinho not in visitados:
                #anota tal caminho ainda não percorrido
                caminho_percorrido = list(caminho_atual)
                caminho_percorrido.append(vizinho)

                # Se o vizinho é o destino, finaliza
                if vizinho == destino:
                    # Mapeia os índices para nomes de cidades antes de retornar
                    return [nomes_cidades[c] for c in caminho_percorrido]

                # Marca como visitado e adiciona à fila para exploração futura
                visitados.add(vizinho)
                fila.append(caminho_percorrido)
                

    # Se a fila esvaziar e o destino não for encontrado
    return None

# Cidades de teste: A (0) -> E (4)
inicio_teste = int(input("Digite numero da cidade que a encomenda irá sair: "))
destino_teste = int(input("Digite o número da cidade que irá receber a encomenda: "))

print(f"--- Busca em Largura (BFS) de {nomes_cidades[inicio_teste]} para {nomes_cidades[destino_teste]} ---")
caminho_bfs = busca_largura(inicio_teste, destino_teste, A, nomes_cidades)

if caminho_bfs:
    print(f" Caminho BFS encontrado (o mais curto): {' -> '.join(caminho_bfs)}")
else:
    print(" Nenhum caminho encontrado por BFS.")
