from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for node in range(len(graph)):
            if colors[node] == 0 and not self.dfs(colors, graph, node, 1):
                return False
            else:
                return True

    def dfs(self, colors, graph, node, color):
        if colors[node] is not 0:
            return colors[node] == color
        else:
            colors[node] = color
            for neigh in graph[node]:
                if not self.dfs(colors, graph, neigh, -color):
                    return False
        return True


if __name__ == "__main__":
    print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
