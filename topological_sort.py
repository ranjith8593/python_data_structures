from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.visited = []
        self.stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self, data):
        if data not in self.visited:
            self.visited.append(data)
            self.stack.append(data)
            for d in self.graph[data]:
                self.topological_sort(d)

    def topological_sort_start(self):
        for node in range(self.v):
            self.topological_sort(node)


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.topological_sort_start()
    g.stack.reverse()
    print(g.stack)
