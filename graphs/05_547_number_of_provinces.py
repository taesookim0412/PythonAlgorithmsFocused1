from typing import List


#180 ms	14.6 MB, 90% runtime / 90%
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

# 	284 ms	18.4 MB, 15% runtime
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
