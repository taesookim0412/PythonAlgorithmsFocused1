from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    islands += 1
        return islands
    def dfs(self, grid, i, j):
        if grid[i][j] != "1":
            return
        grid[i][j] = "0"
        if i> 0:
            self.dfs(grid, i-1, j)
        if i < len(grid) - 1:
            self.dfs(grid, i+1, j)
        if j > 0:
            self.dfs(grid, i, j-1)
        if j < len(grid[0]) - 1:
            self.dfs(grid, i, j+1)