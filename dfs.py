from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, data):
        if data not in self.visited:
            self.visited.append(data)
            for i in self.graph[data]:
                self.dfs(i)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.graph)
    g.dfs(0)
