class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    def DFS(self, v, discovered):
        discovered[v] = True
        for u in self.adjList[v]:
            if not discovered[u]:
                self.DFS(u, discovered)