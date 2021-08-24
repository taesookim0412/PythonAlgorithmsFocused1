from typing import List

# a) 99.23% runtime 75% memory
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                self.dfs(isConnected, i, visited)
        return provinces
    def dfs(self, isConnected, cityIndex, visited):
        for j in range(len(isConnected[cityIndex])):
            if isConnected[cityIndex][j] == 1 and j not in visited:
                visited.add(j)
                self.dfs(isConnected, j, visited)

#b) 82% runtime 75% memory
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, city in enumerate(isConnected):
            for j, connection in enumerate(city):
                if connection == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(graph, i, visited)
                provinces += 1
        return provinces

    def dfs(self, graph, src, visited):
        if src in visited:
            return
        visited.add(src)
        for dest in graph[src]:
            self.dfs(graph, dest, visited)


# (identical to a) 180 ms 14.6 MB, 90% runtime / 90%
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                self.dfs(isConnected, i, visited)
                provinces += 1
        return provinces

    def dfs(self, isConnected, i, visited):
        for j in range(len(isConnected[i])):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                isConnected[i][j] = 0
                self.dfs(isConnected, j, visited)

# c) 284 ms	18.4 MB, 15% runtime
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    self.dfs(isConnected, i, j)
                    provinces += 1
        return provinces
    def dfs(self, isConnected, i, j):
        if isConnected[i][j] != 1:
            return
        for new_j in range(len(isConnected[i])):
            if isConnected[i][new_j] == 1:
                isConnected[i][new_j] = 0
                self.dfs(isConnected, new_j, i)
