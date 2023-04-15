class DisjointSet:    # Classe para representar um conjunto disjunto

    def __init__(self, n):
        # cria conjuntos disjuntos n (um para cada vértice)
        self.pai = {i: i for i in range(1, n + 1)}

    def Find(self, k):  # Encontra a raiz do conjunto ao qual o elemento k pertence
        # se `k` for raiz
        if self.pai[k] == k:
            return k

        # recursão até encontrar a raiz
        return self.Find(self.pai[k])

    def Union(self, a, b):  # Realiza união de dois subconjuntos
        # encontra a raiz dos conjuntos aos quais os elementos x e y pertencem
        x = self.Find(a)
        y = self.Find(b)

        self.pai[x] = y
