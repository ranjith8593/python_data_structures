from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCycleUtil(self, g, node, visited, stack):
        visited[node] = True
        stack[node] = True
        for neigh in g[node]:
            if not visited[neigh]:
                if self.isCycleUtil(g, neigh, visited, stack):
                    return True
            elif stack[neigh]:
                return True
        stack[node] = False
        return False

    def isCycle(self):
        visited = [False] * self.v
        recStack = [False] * self.v
        for node in range(self.v):
            if not visited[node]:
                if self.isCycleUtil(self.graph, node, visited, recStack):
                    return True
        return False


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    if g.isCycle():
        print("Cycle present")
    else:
        print("Cycle not present")
