from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []
        self.queue = []

    def addEdge(self, u , v):
        self.graph[u].append(v)

    def bfs(self):
        data = self.queue.pop(0)
        if data not in self.visited:
            print(data)
            self.visited.append(data)
            for i in self.graph[data]:
                self.queue.append(i)
                self.bfs()

    def bfs_st(self, data):
        self.queue.append(data)
        self.bfs()


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.bfs_st(2)

