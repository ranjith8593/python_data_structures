from collections import defaultdict


class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCycleUtil(self, node, visited, parent):
        visited[node] = True
        for neigh in self.graph[node]:
            if not visited[neigh]:
                if self.isCycleUtil(neigh, visited, node):
                    return True
            elif parent is not neigh:
                return True
        return False

    def isCycle(self):
        visited = [False] * self.v
        for node in range(self.v):
            if not visited[node]:
                if self.isCycleUtil(node, visited, -1):
                    return True

        return False


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    if g.isCycle():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")

    g1 = Graph(3)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)

    if g1.isCycle():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")

