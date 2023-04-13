class DisjointSet:    # Classe para representar um conjunto disjunto

    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}

    def makeSet(self, n):  # executa a operação MakeSet
        # cria conjuntos disjuntos n (um para cada vértice)
        for i in range(int(n)):
            self.parent[i] = i

    def find(self, k):  # Encontra a raiz do conjunto ao qual o elemento k pertence
        # se `k` for root
        if self.parent[k] == k:
            return k

        # recursão até encontrarmos a raiz
        return self.find(self.parent[k])

    def union(self, a, b):  # Realiza união de dois subconjuntos
        # encontra a raiz dos conjuntos aos quais os elementos x e y pertencem
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y
