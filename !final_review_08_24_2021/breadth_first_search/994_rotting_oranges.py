import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges.append([i, j])
        #ULDR
        y_dirs = [1, 0, -1, 0]
        x_dirs = [0, -1, 0, 1]
        minutes = 0
        while fresh_oranges:
            minutes += 1
            new_grid = [row.copy() for row in grid]
            if self.iterate_fresh_oranges_and_return_same_length(fresh_oranges, grid, new_grid, y_dirs, x_dirs):
                return -1
            grid = new_grid
        return minutes

    def iterate_fresh_oranges_and_return_same_length(self, fresh_oranges, grid, new_grid, y_dirs, x_dirs):
        '''Returns whether we found a rotten orange or not'''
        fresh_orange_sz = len(fresh_oranges)
        for _ in range(fresh_orange_sz):
            orange_i, orange_j = fresh_oranges.popleft()
            found_rotten = False
            for i in range(len(y_dirs)):
                new_y, new_x = orange_i + y_dirs[i], orange_j + x_dirs[i]
                if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                    if grid[new_y][new_x] == 2:
                        found_rotten = True
                        break
            if found_rotten is False:
                fresh_oranges.append([orange_i, orange_j])
            else:
                new_grid[orange_i][orange_j] = 2
        return fresh_orange_sz == len(fresh_oranges)

s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
