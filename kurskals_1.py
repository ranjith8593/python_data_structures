class KursKals:
    def __init__(self, v):
        self.v = v
        self.g = []

    def addEdge(self, u,v,w):
        self.g.append([u,v,w])

    def find(self,parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        parent[xroot] = yroot

    def Mst(self):
        result = [] # Minimum Spanning tree
        self.g = sorted(self.g, key=lambda item: item[2])

        # Create v subsets
        parent = []
        rank = []
        for node in range(self.v):
            parent.append(node)

        i = 0
        e = 0

        while e < self.v - 1:
            u,v,w = self.g[i]
            i+=1
