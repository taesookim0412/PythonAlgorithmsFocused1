from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = [row.copy() for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and new_matrix[i][j] == 0:
                    self.setZero(matrix, i, j)
    def setZero(self, matrix, i, j):
        for iter_i in range(len(matrix)):
            matrix[iter_i][j] = 0
        for iter_j in range(len(matrix[0])):
            matrix[i][iter_j] = 0