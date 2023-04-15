from disjointSet import DisjointSet


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
        (orig, dest, peso) = edges[index]
        index += 1

        # encontra a raiz dos conjuntos para os quais dois
        # vértices da aresta pertencem
        x = ds.Find(orig)
        y = ds.Find(dest)

        # se ambos os vertices tiverem pais diferentes, eles pertencem a
        # diferentes componentes conectados e podem ser incluídos no MST
        if x != y:
            MST.append((orig, dest, peso))
            ds.Union(x, y)

    return MST


