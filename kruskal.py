from disjoinSet import DisjointSet

# Função para construir a MST usando o algoritmo de Kruskal
def kruskal(edges, n):
    MST = []  # armazena as arestas presentes no MST
    index = 0

    # Inicializa a classe DisjointSet e cria um conjunto disjunto para cada elemento
    ds = DisjointSet(n)

    # classifica as arestas aumentando o peso
    edges.sort(key=lambda x: x[2])

    # MST contém n-1 bordas
    while len(MST) != n - 1:

        # considera a próxima aresta com peso mínimo do gráfo
        (src, dest, weight) = edges[index]
        index = index + 1

        # encontra a raiz dos conjuntos para os quais dois
        # vértices da aresta pertencem
        x = ds.find(src)
        y = ds.find(dest)

        # se ambos os vertices tiverem pais diferentes, eles pertencem a
        # diferentes componentes conectados e podem ser incluídos no MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST


# Parte principal

if __name__ == "__main__":
    # Abrir a base de dados
    with open('jazzNew.net') as f:
        lines = f.readlines()

    # guardar numero de vertices
    _, nodes = lines[0].split()

    # Criar grafo
    graph = {}
    for line in lines:
        if line.startswith('*'):
            continue

        src, dest, weight = line.split()
        if src not in graph:
            graph[src] = {}
        if dest not in graph:
            graph[dest] = {}
        graph[src][dest] = weight
        graph[dest][src] = weight

    # Converter grafo em uma uma lista de vertices
    edges = []

    # (u, v, w) triples representam: vértice `u` -> vértice `v` com peso `w`
    for src, neighbors in graph.items():
        for dest, weight in neighbors.items():
            edges.append((int(src), int(dest), int(weight)))

    # Kruskal
    mst = kruskal(edges, int(nodes))

    # Output
    sumKm = 0
    for edge in mst:
        print(f'Pedro se deslocou da loja {edge[0]} até a loja {edge[1]} e percorreu {edge[2]}km.')
        sumKm += int(edge[2])
    print()
    print(f'No total, Pedro percorreu {sumKm}km.')

