class Graph:
    def __init__(self, v):
        self.v = v
        self.g = [[0 for x in range(v)] for x in range(v)]

    def get_min(self, key, mstSet):
        min_val = float("inf")
        min_index = None
        for i in range(self.v):
            if key[i] < min_val and not mstSet[i]:
                min_val = key[i]
                min_index = i
        return min_index

    def primMst(self):
        # act like min heap to find the minimum value
        key = [float("inf")] * self.v
        key[0] = 0
        # store the constructed mst
        parent = [None] * self.v
        parent[0] = -1
        mstSet = [False] * self.v
        result = [None] * self.v
        for count in range(self.v):
            index = self.get_min(key, mstSet)
            mstSet[index] = True
            result[index] = parent[index]
            neigh = self.g[index]
            for vertex, weight in enumerate(neigh):
                if weight is not 0:
                    if key[vertex] > weight and not mstSet[vertex]:
                        key[vertex] = weight
                        parent[vertex] = [vertex, count]

        print(result)


if __name__ == "__main__":
    graph = Graph(5)
    graph.g = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    graph.primMst()
