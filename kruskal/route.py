from kruskal import kruskal


# Cria grafo e retorna a mst
def route(nodes, lines):
    grafo = {}
    for line in lines:
        if line.startswith('*'):
            continue
        orig, dest, peso = line.split()
        if orig not in grafo:
            grafo[orig] = {}
        if dest not in grafo:
            grafo[dest] = {}
        grafo[orig][dest] = peso
        grafo[dest][orig] = peso

    # Converter grafo em uma uma lista de vertices
    # (u, v, w) triples representam: vértice de partida `u` -> vértice de chegada `v` com peso `w`
    arestas = []
    for orig, neighbors in grafo.items():
        for dest, peso in neighbors.items():
            arestas.append((int(orig), int(dest), int(peso)))
    # Kruskal
    mst = kruskal(arestas, int(nodes))

    # Output
    return mst