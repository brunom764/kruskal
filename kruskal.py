# Uma classe para representar um conjunto disjunto
class DisjointSet:
    parent = {}

    # executa a operação MakeSet
    def makeSet(self, n):
        # cria conjuntos disjuntos `n` (um para cada vértice)
        for i in range(n):
            self.parent[i] = i

    # Encontre a raiz do conjunto ao qual o elemento `k` pertence
    def find(self, k):
        # se `k` for root
        if self.parent[k] == k:
            return k

        # recorrente para o pai até encontrarmos a raiz
        return self.find(self.parent[k])

    # Realiza união de dois subconjuntos
    def union(self, a, b):
        # encontra a raiz dos conjuntos aos quais os elementos `x` e `y` pertencem
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y


# Função para construir MST usando o algoritmo de Kruskal
def runKruskalAlgorithm(edges, n):
    # armazena as arestas presentes no MST
    MST = []

    # Inicializa a classe `DisjointSet`.
    # Crie um conjunto singleton para cada elemento do universo.
    ds = DisjointSet()
    ds.makeSet(n)

    index = 0

    # classifica as arestas aumentando o peso
    edges.sort(key=lambda x: x[2])

    # MST contém exatamente bordas `V-1`
    while len(MST) != n - 1:

        # considera a próxima aresta com peso mínimo do gráfico
        (src, dest, weight) = edges[index]
        index = index + 1

        # encontre a raiz dos conjuntos para os quais dois terminais
        # vértices da próxima aresta pertencem
        x = ds.find(src)
        y = ds.find(dest)

        # se ambos os terminais tiverem pais diferentes, eles pertencem a
        # diferentes componentes conectados e podem ser incluídos no MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST



# (u, v, w) tripleto representam a borda não direcionada de
# vértice `u` para vértice `v` com peso `w`
edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]

 # número total de nós no gráfico (rotulado de 0 a 6)
n = 7

# gráfico de construção
e = runKruskalAlgorithm(edges, n)

print(e)

